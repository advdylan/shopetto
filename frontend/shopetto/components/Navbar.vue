<template>

  <nav class="bg-gradient-to-r from-ali2 from-10% via-ali1 via-30% to-ali2 to-90% shadow-lg px-4 py-3 rounded-br-md rounded-bl-md flex items-center justify-between">
    <div class="text-xl font-bold cursor-pointer"><NuxtLink to="/"> Shopetto </NuxtLink>
      
    </div>
    <div  @mouseenter="categoryStore.onMouseEnter" @mouseleave="categoryStore.onMouseLeave" class="absolute left-1/2 transform -translate-x-1/2 text-black font-bold hover:text-blue-600 cursor-pointer flex items-center justify-center gap-x-1 py-1">
      Shop
      <Icon size="1.5em" name="mdi-light:format-list-bulleted"/>
    </div>
    <div class="hidden md:flex space-x-4">
      <button href="/"
        class="text-black-700 hover:text-blue-600  cursor-pointer flex items-center justify-center gap-x-1 py-1">
        <Icon size="1.5em" name="mdi-light:home" />
        <NuxtLink to="/"> Home </NuxtLink>
      </button>
      <button href="/contact"
        class="text-black-700 hover:text-blue-600 cursor-pointer flex items-center justify-center gap-x-1 py-1">
        <Icon size="1.5em" name="mdi-light:phone" />
        Contact
      </button>
      <button href="/"
        class="text-black-700 hover:text-blue-600 cursor-pointer flex items-center justify-center gap-x-1 py-1">
        <Icon size="1.5em" name="mdi-light:cart" />
        Cart
      </button>
      
    </div>
    <button @click="mobileOpen = !mobileOpen" class="md:hidden">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"/>
      </svg>
    </button>

    <div v-if="mobileOpen" class="absolute top-16 left-0 w-full bg-white shadow-md md:hidden">
      <a href="/" class="block px-4 py-2 text-gray-700 hover:bg-gray-100">Home<Icon name="mdi-light:account"/> </a>
      <a href="/shop" class="block px-4 py-2 text-gray-700 hover:bg-gray-100">Shop</a>
      <a href="/contact" class="block px-4 py-2 text-gray-700 hover:bg-gray-100">Contact</a>
    </div>

    
    
    

  </nav>
  <div class="flex items-center justify-center">
    <CategoryDropDown/>
  </div>
  
  
  
</template>

<script setup lang="ts">

import { Icon } from '#components'
import { ref } from 'vue';
import CategoryDropDown from './CategoryDropDown.vue';
import { useCategoryStore } from '~/stores/products'

const mobileOpen = ref(false)
const categoryStore = useCategoryStore()


onMounted(() => {

})

</script>