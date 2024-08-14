import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
from celery import shared_task
from .serializers import OrdersSerializer
from users.models import User
from orders.serializers import ShippingAddressSerializer
from dotenv import load_dotenv

load_dotenv()

smtp_port = os.getenv('smtp_port')
smtp_server = os.getenv('smtp_server')
email_from = os.getenv('email_from')
pswd = os.getenv('pswd')

@shared_task
def send_emails_task(emails_list, title, msg):
    time.sleep(1)

    # Connect with the server
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, int(smtp_port))
    TIE_server.starttls()
    TIE_server.login(email_from, pswd)
    print("Successfully connected to server")
    print()


    def sender_func(person):
        body = msg

        # Make a MIME object to define parts of the email
        email_msg = MIMEMultipart()
        email_msg['From'] = email_from
        email_msg['To'] = person
        email_msg['Subject'] = title

        # Attach the body of the message
        email_msg.attach(MIMEText(body, 'plain'))

        # Cast as string
        text = email_msg.as_string()

        # Send email
        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

    if len(list(emails_list)) > 1:
        emails_list.split(',')
        for person in emails_list:
            sender_func(person)
    else:
        sender_func(emails_list)

    # Close the server connection
    TIE_server.quit()


# manage email sending
@shared_task
def send_email_to_admin_and_client_task(client_email, order_data):
    emails_list = ['acanalofmoney2020@gmail.com', 'bcanalofmoney2020@gmail.com']
    title = 'New Order on La Fleur Lily website'
    msg = (
        f'order data: Cart data - {order_data.cart_data} '
        f'Shipping data - {order_data.shipping_data}'
    )
    send_emails_task.delay(emails_list=emails_list, title=title, msg=msg)
    title = 'Thank You for Making Order at LaFleurLily'
    msg = (
        f'Hi {order_data.shipping_data.first_name}, your Order have been placed'
        f'ID Order is : #{order_data.id}'
        f'you also can call us : +1234253265 or email: supportLily@gmail.com'
    )
    send_emails_task.delay(emails_list=[f"{client_email}",], title=title, msg=msg)

    return "emails was sent"


# create new order
@shared_task
def create_new_order_task(request_data, user_id, db):
    try:
        user = User.objects.using(db).get(id=user_id)
        if user.is_authenticated:
            new_order = OrdersSerializer(data=request_data)

            if new_order.is_valid():
                shipping_address = user.user_shipping_address

                if shipping_address is None:
                    return {'message': 'Your Shipping Address is None', 'isShippingAddress': False}
                order = new_order.save(user=user, shipping_data=user.user_shipping_address, using=db)
                send_email_to_admin_and_client_task(user.user_shipping_address.email, order)
                return {'message': 'Order was successfully created', 'order_id': order.id}

            else:
                return {'error': 'Some error with data', 'details': new_order.errors}

        else:
            shipping_address = request_data.get('shipping_data', None)

            if not shipping_address:
                return {'error': 'Missing data about shipping address'}

            new_shipping_address = ShippingAddressSerializer(data=shipping_address)

            if new_shipping_address.is_valid():
                address = new_shipping_address.save(using=db)
                new_order_data = request_data.copy()
                new_order_data['shipping_data'] = address.id
                new_order = OrdersSerializer(data=new_order_data, using=db)

                if new_order.is_valid():
                    order = new_order.save(using=db)
                    send_email_to_admin_and_client_task(address.email, order)
                    return {'message': 'New Order has been created for Guest', 'order_id': order.id}
                return {'error': 'Some problems with order data', 'details': new_order.errors}
            return {'error': 'Some problems with Shipping Address data', 'details': new_shipping_address.errors}

    except Exception as e:
        return e
