<script setup>
  import { RouterLink } from 'vue-router'
  import { onMounted, ref, computed } from 'vue';
  import axios from 'axios';
  import { DOMAIN_NAME } from '@/utils/api_links';

  const products = ref({});
  const isLoading = ref(true);
  const hasError = ref(false);

  const finalEndpoint = DOMAIN_NAME + 'products/';

  onMounted(async () => {
      await getProducts();
  });


  async function getProducts() {
      try {
          await axios.get(finalEndpoint)
              .then(
                  (response) => {
                    
                    products.value = response.data.slice(0, 4);
                    console.log(products.value);
                    
                      
                  }
              )
              .catch((error) => {
                  console.log(error);
              })
      } catch (error) {
          console.log("some errors with backend server", error)
          hasError.value = true;
      } finally {
          isLoading.value = false;
          console.log(hasError)
      }
      
  }


 const items = [
    {
        image: "/pages/images/block3_first_img.jpg",
        p_text: "To provide you with the best wine and service is our primary goal.",
        a_text: "OUR WINES",
        link: "/shop/wine"
    },
    {
        image: "/pages/images/block3_second_img.jpg",
        p_text: "La Fleur Lily is love in a glass.",
        a_text: "OUR SPARKLING",
        link: "/shop/sparkling"
    },
    {
        image: "/pages/images/block3_three_img.jpg",
        p_text: "La Fleur Lily - wine born with love and passion.",
        a_text: "OUR STORY",
        link: "/about-us"
    }

]



</script>

<template>
  <div style="margin: 0; padding: 0;" class="max-width">
    <div class="first-block">

      <div class="buttons">
        <button class="block1-btn1">
          <RouterLink to="/shop"><a class="block1-a1">SHOP NOW</a></RouterLink>
        </button>
        <button class="block1-btn2">
          <RouterLink to="/about-us"><a class="block1-a2">ABOUT US</a></RouterLink>
        </button>
      </div>
    </div>
    <div class="two-block">
      <video src="../../public/pages/videos/first_video_two-block.mp4" width="580" height="300" autoplay muted loop
        controls="false">
        Your browser does not support the video
      </video>
      <p>
        Welcome to La Fleur Lily, where organic wines<br>
        are crafted with soul.Our vineyards thrive<br>
        under the nurturing touch of nature, yielding<br>
        grapes bursting with vibrant flavors.<br>
        Experience the essence of our handcrafted<br>
        wines, made with love and care, and embark<br>
        on a journey of pure delight for your senses.
      </p>
    </div>
    <div class="three-block">
      <div class="card" v-for="item in items" :key="item.image">
        <img :src="item.image" class="block3-first-img" />
        <div class="act-on-content">
          <p class="block3-p1">{{ item.p_text }}</p>
          <button class="block3-btn1">
            <RouterLink :to="item.link"><a>{{ item.a_text }}</a></RouterLink>
          </button>
        </div>
      </div>
    </div>
    <div class="home-products-h">
      <h2 class="featured-prod-h">Featured Products</h2>
      <div class="products-h">
        <div v-for="product in products" :key="product.id" class="product-h">
          <RouterLink :to="{name:'product_detail', params:{slug: product.slug_url}}">
            <img :src="product.img_url" alt="Wait please" />
          </RouterLink>
          <div class="info-product-shop-h">
            <h2 class="product-name-h">{{ product.name }} </h2>
            <p class="product-category-h">
              <span v-if="product.category == 1 ">Wine</span>
              <span v-else>Sparkling</span>
            </p>
            <p class="product-price-h">${{ product.price }}.00</p>
            <div class="review-h">

              <div class="stars-img-h">
                <img v-for="item in 5" :key="item"
                  src="../../public/pages/images/site-img/star-photo-review.svg" />
              </div>
            </div>
          </div>
        </div>
      </div>
      <RouterLink :to="{name: 'shop'}">
        <button class="products-btn-h"><a>VIEW ALL PRODUCTS</a></button>
      </RouterLink>
    </div>
  </div>


</template>

<style scoped>

.first-block {
  position: relative;
  height: 470px;
  background-image: url(../../public/pages/images/first-background-img.jpg);
  background-size: cover;
  background-attachment: fixed;
}
.first-block button {
  margin-top: 15%;
  font-size: larger;
  margin-left: 45px;
}


button a {
  text-decoration: none;
}

.block1-btn1 {
  width: 180px;
  height: 50px;
  background-color: white;
  border: 0;
}

.block1-btn1 a {
  color: black;
}

.block1-btn1:hover {
  background-color: black;
  border: 0;
}

.block1-btn1:hover a {
  color: white;
}

.block1-btn2 {
  width: 165px;
  height: 50px;
  border: 6%;
  border-color: white;
  background-color: rgba(0, 0, 0, 0);
}

.block1-btn2 a {
  color: white;
}

.block1-btn2:hover {
  background-color: white;
  border: 0;
}

.block1-btn2:hover a {
  color: black;
}

.block1-p1 {
  font-size: xxx-large;
  color: #ffffff;
  margin-left: 5%;
  border: 10px;
  border-color: #000000;
}


.two-block {
  display: flex;
  justify-content: center;

  width: 85%;
}


.two-block video::-webkit-media-controls-panel {
  display: none;
}

.two-block video::-webkit-media-controls {
  display: none;
}

.two-block video {
  margin-top: 30px;
  margin-right: 10%;
  padding-left: 0%;
  padding-right: 0%;
}

.two-block p {
  text-align: left;
  width: 350px;
  margin-top: 75px;
  margin-left: 40px;
  font-style:  sans-serif;
  font-size: medium;
  line-height: 32px;
}

.three-block {
  display: flex;
  margin-top: 75px;
  justify-content: center;
  width: 95%;
}

.three-block img {
  width: 300px;
  height: 450px;
  position: relative;
  object-fit: cover;
}

.card{
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 10px;
  margin: 3%;
  position: relative;
  height: 480px;
}

.act-on-content {
  position: absolute;
  bottom: 0;
  left: 0;
  margin-bottom: 90px;
  margin-left: 40px;
}

.three-block button {
  width: 180px;
  height: 50px;
  background-color: white;
  border: 0;
}
.three-block button a {
  color: black;
  font-size: large;
}

.three-block button:hover {
  background-color: black;
}

.three-block button:hover a {
  color: white;
}

.three-block p {
  font-size: xx-large;
  width: 240px;
  color: white;
  background-color: rgb(181, 170, 170);
}

.home-products-h {
  text-align: center;
  padding: 20px;
  background-color: #f9f9f9;
}

.featured-prod-h {
  font-size: 28px;
  color: #333;
  font-family: 'Montserrat', sans-serif;
  margin-bottom: 30px;
}

.products-h {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 20px;
  max-width: 100%;
}

.product-h {
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
  width: 220px;
  padding: 15px;
  margin: 20px;
  text-align: center;
}

.product-h:hover {
  transform: translateY(-5px);
}

.product-h img {
  height: 200px;
  width: auto;
  object-fit: cover;
  border-radius: 10px;
}

.info-product-shop-h {
  margin-top: 15px;
}

.product-name-h {
  font-size: 18px;
  font-weight: bold;
  color: #333;
}

.product-category-h {
  font-size: 14px;
  color: #888;
  margin-top: 5px;
}

.product-price-h {
  font-size: 22px;
  font-weight: bold;
  color: #d32f2f;
  margin-top: 10px;
}

.review-h {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}

.stars-img-h img {
  width: 18px;
  height: 18px;
  margin: 0 2px;
}

.products-btn-h {
  margin-top: 90px;
  width: 80%;
  height: 50px;
  background-color: rgba(0, 0, 0, 0);
  border: 10%;
  border-color: black;
}

.products-btn-h a {
  color: black;
  font-size: larger;
}

.products-btn-h:hover {
  background-color: black;
}

.products-btn-h:hover a {
  color: white;
} 


@media (max-width: 768px) {
  .max-width{
    max-width: 100%;
  }

  .first-block {
    height: 300px;
    background-attachment: scroll;
    width: 100%;
  }

  .first-block button {
    margin-top: 60%;
    font-size: medium;
    margin-left: 10%;
  }

  .block1-btn1,
  .block1-btn2 {
    width: 140px;
    height: 40px;
  }

  .two-block {
    display: block;
    width: 100%;
  }

  .two-block video {
    width: 80%;
    height: auto;
    margin: 0 auto;
    display: block;
    margin-top: 10%;
  }

  .two-block p {
    text-align: center;
    width: auto;
    margin: 5px;
    font-size: small;
  }

  .three-block {
    display: block;
    margin: 20px auto;
    justify-content: center;
    text-align: center;
  }

  .three-block img {
    width: 100%;
    height: 350px;
  }

  .card {
    width: 90%;
    height: auto;
  }

  .act-on-content {
    margin: 0 auto;
    bottom: 10px;
    left: 50%;
    transform: translateX(-50%);
   
  }

  .three-block button {
    width: 100%;
    height: 40px;
    font-size: medium;
    margin-bottom: 30px;
  }

  .three-block p {
    font-size: large;
    width: 90%;
    margin: 0 auto;
    margin-bottom: 50px;
  }

  .products {
    margin: 0 auto;
    margin-left: 7%;
  } 

  
}
</style>
