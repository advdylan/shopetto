<template>

  
  
  <nav class="bg-white shadow px-4 py-3 flex items-center justify-between">
    <div class="text-xl font-bold">Shopetto</div>
    <div class="hidden md:flex space-x-4">
      <a href="/" class="text-gray-700 hover:text-blue-600">Home</a>
      <a href="/shop" class="text-gray-700 hover:text-blue-600">Shop</a>
      <a href="/contact" class="text-gray-700 hover:text-blue-600">Contact</a>
    </div>
    <button @click="mobileOpen = !mobileOpen" class="md:hidden">
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"/>
      </svg>
    </button>

    <div v-if="mobileOpen" class="absolute top-16 left-0 w-full bg-white shadow-md md:hidden">
      <a href="/" class="block px-4 py-2 text-gray-700 hover:bg-gray-100">Home <Icon name="mdi-light:account" style="color: black" /> </a>
      <a href="/shop" class="block px-4 py-2 text-gray-700 hover:bg-gray-100">Shop</a>
      <a href="/contact" class="block px-4 py-2 text-gray-700 hover:bg-gray-100">Contact</a>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { useCategoryStore } from '~/stores/products';
import { Icon } from '#components'
import { ref } from 'vue';

const mobileOpen = ref(false)
const categoryStore = useCategoryStore()



onMounted(() => {
  if(categoryStore.categories.length === 0) {
    categoryStore.fetchCategories()
  }
})

</script>