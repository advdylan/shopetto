<template>
  <div>
    <h1 class="text-2xl font-sans">Products</h1>
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

<script setup lang="ts">

type Product = {
  id: number,
  name: string,
  price: number
}

const { data: products, pending, error } = await useFetch<Product[]>('http://127.0.0.1:8000/api/product/')
</script>