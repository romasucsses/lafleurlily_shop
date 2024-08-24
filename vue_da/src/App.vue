<script setup>
  import NavMenu from './components/NavMenu.vue'
  import FooterMenu from './components/FooterMenu.vue'
  import { RouterView } from 'vue-router'
</script>

<template>
  <NavMenu />
  <RouterView />
  <FooterMenu />
</template>
