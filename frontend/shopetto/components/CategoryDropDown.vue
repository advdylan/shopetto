<template>
  <div
  v-if="categoryStore.dropdownHover"
  @mouseenter="categoryStore.onMouseEnter"
  @mouseleave="categoryStore.onMouseLeave"
  class="bg-stone-100 w-180 h-85 shadow-lg mt-2 rounded-md flex place-items-start gap-4 px-2 py-2"
>
  <!-- Left Column -->
  <div class="w-1/4 h-full border-r border-solid border-stone-300">
    <ul class="list-inside">
      <li
        v-for="category in parentCategories"
        class="p-2">

        <span class="inline-block border-b border-stone-300 shadow rounded-sm p-1 w-4/5">
          {{ category.name }}
        </span>
      </li>
    </ul>
    

  </div>

  <!-- Middle Column -->
  <div class="w-1/4 h-full border-r border-solid border-stone-300">Middle</div>

  <!-- Right Column -->
  <div class="w-2/4 h-full border-r border-solid border-stone-300">Right</div>
</div>
</template>

<script setup lang="ts">
import { useCategoryStore } from '~/stores/products'


const categoryStore = useCategoryStore()
const categories = storeToRefs(categoryStore)

const parentCategories = computed(() => {
  return categories.categories.value.filter(category => category.parent === null)
})


onMounted(() => {
  if (categoryStore.categories.length === 0) {
    categoryStore.fetchCategories()
  }
  
})
</script>