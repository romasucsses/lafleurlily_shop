from django.apps import apps
from products.serializers import *
from orders.serializers import *


def get_model_by(db, table_name_start, app_name):
    model_name = None
    if db == 'bastina':
        model_name = f'{table_name_start}Bastina'
    elif db == 'da':
        model_name = f'{table_name_start}DA'
    elif db == 'lily':
        model_name = f'{table_name_start}Lily'

    return apps.get_model(app_name, model_name)



def get_serializer(db, table_name_start):
    serializer_map = {
        'Product': {
            'bastina': ProductBastinaSerializer,
            'da': ProductDASerializer,
            'lily': ProductLilySerializer,
        },
        'Reviews': {
            'bastina': ReviewsBastinaSerializer,
            'da': ReviewsDASerializer,
            'lily': ReviewsLilySerializer,
        },
        'OrderInfo': {
            'bastina': OrderInfoBastinaSerializer,
            'da': OrderInfoDASerializer,
            'lily': OrderInfoLilySerializer,
        },
        'Stores': {
            'bastina': StoresBastinaSerializer,
            'da': StoresDASerializer,
            'lily': StoresLilySerializer,
        }

    }
    serializers_for_table = serializer_map.get(table_name_start)

    if serializers_for_table:
        return serializers_for_table.get(db, None)
    else:
        return "Some error with get_serializer data"
