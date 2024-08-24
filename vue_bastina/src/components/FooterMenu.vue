<script setup>
import axios from 'axios'
import { DOMAIN_NAME } from '@/utils/api_links';

let email_user;
async function subscribePostRequest() {
  try {
    await axios.post(DOMAIN_NAME + 'orders/email-subscrube/', { email: email_user });
  } catch (error) {
    console.error("Error occurred:", error);
  }
}
</script>

<template>
  <div class="footer">
    <div class="left-column">
      <div class="icons-footer">
        <a href="https://www.instagram.com/lafleurlilywine/">
          <img src="../../public/pages/images/site-img/icons-footer/instagram-footer.png" />
        </a>
        <a href="https://www.facebook.com/lafleurlilywine/">
          <img src="../../public/pages/images/site-img/icons-footer/facebook-footer.svg" />
        </a>

        <a href="https://www.pinterest.com/lafleurlilywine/">
          <img src="../../public/pages/images/site-img/icons-footer/pinterest-footer.svg" />
        </a>
      </div>
      <p>Copyright © 2024 Bastina</p>
    </div>

    <div class="right-column">
      <h2>Subscribe</h2>
      <form method="post">
        <input type="email" id="subscration" v-model="email_user" name="email" placeholder="Your email adress..." />
        <button @click.prevent="subscribePostRequest()" type="submit" class="subs-btn" name="action"
          value="subscribe">Subscribe</button>
      </form>
    </div>
  </div>
</template>

<style scoped>

.footer {
  margin-top: 40px;
  display: flex;
  background-color: #ffffff;
  height: 260px;
  justify-content: space-between;
  width: 100%;
}

.icons-footer img {
  width: 18px;
  height: 18px;
}

.footer .left-column {
  margin-top: 3%;
  margin-left: 2%;
}

.footer .right-column {
  margin-top: 3%;
  margin-right: 6%;
  width: 35%;
}

.footer .right-column h2 {
  color: #000000;
  font-size: 1.375rem;
  font-weight: 400;
  margin-bottom: 1em;
  line-height: 1.5;
}

.footer button {
  width: 160px;
  height: 50px;
  background-color: rgba(102, 34, 47, 1);
  color: #ffff;
  border: 0;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding-top: 16px;
  padding-right: 28px;
  padding-bottom: 16px;
  padding-left: 28px;
}

.icons-footer {
  display: flex;
  justify-content: space-between;
  width: 80px;
}

#subscration {
  width: 390px;
  height: 45px;
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 2px;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .footer {
    flex-direction: column;
    align-items: center;
    height: auto;
    padding: 20px;
    width: 95%;
  }


  .footer .left-column,
  .footer .right-column {
    margin: 0;
    width: 100%;
    text-align: center;
  }

  .footer .right-column {
    margin-top: 20px;
  }

  .icons-footer {
    justify-content: center;
    gap: 20px;
    width: auto;
  }

  #subscration {
    width: 70%;
  }

  .footer button {
    width: 70%;
    margin-top: 10px;
  }
}
</style>
