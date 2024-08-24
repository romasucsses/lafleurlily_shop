<script setup>
    const person_url =  "../../pages/images/team-photos/" ;

    const team_people = [
        { name: "Victor Costin", position: "CEO - Founder" },
        { name: "Lily Costin",position: "CFO" },
        { name: "Rachel Zain", position: "Marketing Head" },
        { name: "Roma Costin", position: "FullStack Devoloper" },
        { name: "Katrina Bennett", position: "Call Operator" },
        { name: "Eugen Pantus", position: "Designer" }
    ]
    
</script>

<template>
    
    <div>
      

      <div class="main-block">
        <h4 class="few-words">A Few Words About</h4>
        <div class="content">
          <div class="left-block">
            <h2>Who We Are</h2>
            <p>
              Bastina Wine is a brand born from the dreams of Victor and Lily,
              a young couple who left Europe for the United States in search 
              of a better life. Upon settling in New York, Lily began a quest
              to find the perfect semi-sweet wine that matched her taste. 
              Victor, who came from a long line of winemakers, was determined
              to find a pure, high-quality wine with no additives for his beloved. 
              Victor’s search took him across the globe, and in 2004, he met a 
              gifted winemaker who had inherited the craft from his parents. 
              This winemaker had created a unique wine that resonated with Lily's
              romantic and free-spirited nature. Victor tasted the wine and immediately
              knew it was what he had been searching for. Together, they named the wine
              Bastina, a name that would come to symbolize elegance and passion.
              The partnership between Victor and the winemaker flourished, and over
              the years, Bastina Wine expanded its portfolio to include 12 exceptional
              wines, each crafted with the same dedication to quality. In 2023, Bastina
              Wine earned an organic certification in France, a testament to their 
              unwavering commitment to excellence and environmental stewardship.
              Thanks to Victor’s vision and the winemaker’s talent, Bastina Wine has
              become not only Lily's favorite but also one of the most beloved wine 
              brands on the market, celebrated for its authenticity and rich flavors.
            </p>
          </div>
          <img src="../../public/pages/images/bender-back.jpeg" />
        </div>
      </div>
      <div class="our-team-block">
        <h2 class="header-team">Our Team</h2>
        <p class="title-team">
          At Bastina Wine, we believe in the power of collaboration, innovation,
          and a shared vision. Our diverse and talented team is the driving force
          behind our success, working together to create exceptional solutions and
          deliver outstanding results. Get to know the extraordinary individuals
          who make up our team and discover the passion, expertise, and dedication
          that sets us apart.
        </p>
        <div class="people">
          <div class="card" v-for="person in team_people" :key="person.name">
              <img :src="`${person_url}${team_people.indexOf(person) + 1}.png`">
              <h4 class="name">{{ person.name }}</h4>
              <p class="position">{{ person.position }}</p>
          </div>
        </div>
      </div>
    </div>
  
</template>

<style scoped>
.main-block{
    margin-top: 50px;
    margin: 40px;
    text-align: center;


}

.content{
    display: flex;
    justify-content: center;
    align-items: flex-end;
    padding: 5px;
    margin: 10px;
}
.main-block .left-block{
    font-size: 24px;
    max-width: 520px;
    margin-left: 50px;
}
.main-block .few-words{
    font-size: 40px;
    text-align: center;
    margin-bottom: 40px;
}
.left-block h2{
    font-size: 42px;
}
.left-block p{
    font-size: 16px;
    line-height: 1.9;

}

.main-block img{
    width: 400px;
    height: 450px;
    margin-right: 8%;
    margin-left: 8%;
    margin-bottom: 5%;
    object-fit: cover;
    object-position: right;

    
    
}


.our-team-block{
    margin-top: 100px;
    margin: 15px;
    text-align: center;

}


.header-team{
    margin-top: 40px;
    font-size: 42px;
    margin: 0 auto;
    margin-bottom: 30px;
}

.title-team{
    font-size: 16px;
    width: 600px;
    line-height: 1.5;

    margin: 0 auto;
}



.people{
    display: flex;
    justify-content: center;
    max-width: 55%;
    flex-wrap: wrap;
    margin: 0 auto;
    margin-top: 10%
}

.people .card{
    text-align: center;
    width: 260px;
    height: 250px;
    border-radius: 10px;
    background-color: #F5F7F9;
    margin: 20px;
}

.people .card img{
    margin-top: 15px;
    width: 90px;
    height: 90px;
}


/* Responsive adjustments */
@media (max-width: 768px) {
  .main-block {
    margin: 20px;
  }

  .content {
    flex-direction: column;
    align-items: center;
  }

  .main-block .left-block {
    margin-left: 0;
    font-size: 18px;
  }

  .main-block img {
    margin-right: 0;
    margin-bottom: 20px;
    width: 100%;
    height: auto;
  }

  .header-team,
  .left-block h2 {
    font-size: 32px;
  }

  .title-team {
    width: 100%;
    font-size: 14px;
  }

  .people .card {
    width: 100%;
    height: auto;
    margin: 10px 0;
  }

  .people .card img {
    width: 70px;
    height: 70px;
  }

  

  .center-links {
    width: 40%;
    height: 40%;
    margin-top: 30%;
    padding: 20px;
  }

  


    .social-media {
      display: flex;
      justify-content: center;
      
    }
  
    .social-media img {
      
      width: 25px;
      height: 25px;
      padding: 20px;
    }

    
}

</style>

