<script setup>
    import { RouterLink } from 'vue-router';
    import axios from 'axios';
    import {ref, onMounted, watchEffect} from 'vue';
    import { DOMAIN_NAME } from '../utils/api_links.js';
    import { computed } from 'vue';

    const products = ref({});
    const isLoading = ref(true);
    const hasError = ref(false);

    const finalEndpoint = DOMAIN_NAME + 'products/';

    onMounted(()=>{
        getProducts();
    })


    async function getProducts() {
        try {
            await axios.get(finalEndpoint)
                .then(
                    (responese) => {
                        products.value = responese.data;
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

    //Sorting

    const SelectedSort = ref('default')

    function CallSorting(){
        axios.get(finalEndpoint, {
            params : { 'action': 'ordering', 'ordering_by': SelectedSort.value}
        })
        .then( 
            (response) => {
                products.value = response.data;
                
            }
            
        )
        .catch(
            (errors) => {
                console.log(errors);
            }
        )
    };

   
    watchEffect(() => {
        CallSorting();
    })

    //Searching
    
    const searchQuery = ref('');

    
    const SearchComp = computed(() => {
        if (searchQuery.value) {
            return products.value.filter((item)=>{
                return searchQuery.value.toLowerCase().split(' ').every(v => item.name.toLowerCase().includes(v))
            })
        }else{
            return products.value;
        }

        })
    
    
    

    watchEffect(() => {
        SearchComp.value;
    });

   
    
</script>

<template>
    <div>

        <div class="main-content">
            <div class="left-block">
                <div class="search-prod-form">
                    <input v-model="searchQuery" @input="SearchComp" id="search-prod" placeholder="Search products..">
                </div>
                <div class="categories">
                    <p class="title">Categories</p>

                    <RouterLink :to="{name: 'shop'}">
                        <p class="wine-cat">Sparkling</p>
                    </RouterLink>
                </div>
            </div>
            <div class="right-block-products">
                <div class="head-rightcolum">
                    <p class="results">Showing all {{ products.length }} results</p>

                    <form class="ordering-form" method="get" action="#">
                        <select name="ordering-by" class="sorting" v-model="SelectedSort" @change="CallSorting()">
                            <option value="default" selected="selected">Sorting by Default</option>
                            <option value="popularity">By popularity</option>
                            <option value="price-up">By Price Low -> High</option>
                            <option value="price-down">By Price High -> Low</option>
                        </select>

                    </form>
                </div>
                <div v-if="isLoading.value">Loading...</div>
                <div v-else-if="hasError.value">There was an error loading the products. Please try again later.</div>
                <div v-else class="proucts-shop">

                    <div v-for="product in products" :key="product.id" class="product">
                        <RouterLink :to="{name:'product_detail', params:{slug: product.slug_url}}">
                            <img :src="product.img_url" alt="Wait please" />
                        </RouterLink>
                        <div class="info-product-shop">
                            <h2 class="product-name">{{ product.name }} </h2>
                            <p class="product-category">
                                <span v-if="product.category == 1 ">Wine</span>
                                <span v-else>Sparkling</span>
                            </p>
                            <p class="product-price">${{ product.price }}.00</p>
                            <div class="review">

                                <div class="stars-img">
                                    <img v-for="item in 5" :key="item"
                                        src="../../public/pages/images/site-img/star-photo-review.svg" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>


    </div>
</template>

<style scoped>
.main-content{
    display: flex;
    justify-content: space-between;
    max-width: 85%;
}


.left-block{
    margin-left: 16px;
    max-width: 300px;
}

.search-prod-form input {
    margin-top: 15%;
    height: 40px;
    width: 95%;
    font-size: 17px;
    padding: 0 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    outline: none;
    transition: border-color 1s, box-shadow 1s;
   
}


.search-prod-form input:focus {
    border-color: rgba(102, 34, 47, 1);
    box-shadow: 0 0 8px rgba(52, 152, 219, 0.5);
}


.categories{
    margin-top: 70px;
    padding-bottom: 9px;
}
.categories .title{
    font-size: 28px;
}

.categories .wine-cat,
.categories .sparkling-cat{
    font-size: 18px;
}


.right-block-products{
    background-color: #FFFFFF;
    width: 1110px;
}
.head-category {
    margin: 30px;
    padding: 30px;
}

.head-category h1 {
    font-weight: 300;
    font-size: 60px;
}

.head-category p {
    font-size: 19px;
    line-height: 1.7;
}

.head-rightcolum{
    display: flex;
    justify-content: space-between;
    margin: 50px;

}

.head-rightcolum p{
    font-size: 18px;
    color: #666;
}

.head-rightcolum select{
    background-color: transparent;
    border: transparent;
    border-radius: 2px;
    color: #666;
    width: 210px;
    height: 50px;
    font-size: 16px;
    border-color: #666;
    box-shadow: #666;
    
}

.proucts-shop{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    max-width: 100%;
    margin-top: 100px;
    padding: 15px;
    width: 100%;
    max-width: 900px;
}


.product {
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
  width: 220px;
  padding: 15px;
  margin: 20px;
  text-align: center;
}

.product:hover {
  transform: translateY(-5px);
}

.product img {
  height: 200px;
  width: auto;
  object-fit: cover;
  border-radius: 10px;
}

.info-product-shop {
  margin-top: 15px;
}

.product-name {
  font-size: 18px;
  font-weight: bold;
  color: #333;
}

.product-category {
  font-size: 14px;
  color: #888;
  margin-top: 5px;
}

.product-price {
  font-size: 22px;
  font-weight: bold;
  color: #d32f2f;
  margin-top: 10px;
}

.review {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}

.stars-img img {
  width: 18px;
  height: 18px;
  margin: 0 2px;
}


/* Responsive adjustments */
@media screen and (max-width: 768px) {
    .main-content {
        flex-direction: column;
        align-items: center;
        padding: 0 15px;
    }

    .left-block {
        width: 100%;
        max-width: 100%;
        margin-left: 0;
        margin-bottom: 20px;
    }

    .right-block-products {
        width: 100%;
        max-width: 100%;
        margin-top: 20px;
    }

    .head-rightcolum {
        flex-direction: column;
        align-items: center;
        margin: 20px 0;
    }

    .head-rightcolum p {
        margin-bottom: 10px;
    }

    .head-rightcolum select {
        width: 100%;
    }

    .proucts-shop {
        flex-direction: column;
        align-items: center;
        width: 92%;
       

        
    }
    .product {
        width: 85%;
        /* padding: 10px 5px; */
        background-color: rgb(250, 250, 250);
        /* margin: 10px; */
        text-align: center;
    }

    .product img {
        width: 180px;
        height: 180px;

    }

    .search-prod-form input{
        width: 90%;
    }

    .stars-img img {
        width: 10px;
        height: 10px;
        bottom: 0;
        padding: 1px;
        margin: 1px;
        margin-top: 9px;

    }
}
</style>