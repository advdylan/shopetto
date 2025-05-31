<template>
  <div>
    <h1 class="text-2xl font-bold mb-4">Products</h1>
    <div v-if="pending">Loading...</div>
    <div v-else>
      <ul>
        <li v-for="product in products" :key="product.id">
          {{ product.name }} - ${{ product.price }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
const { data: products, pending, error } = await useFetch('http://localhost:8000/api/products/')
</script>