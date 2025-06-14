<template>
  <div
  v-if="categoryStore.dropdownHover"
  @mouseenter="categoryStore.onMouseEnter"
  @mouseleave="categoryStore.onMouseLeave()"
  class="absolute z-20  top-14  bg-stone-200 w-320 h-85 shadow-lg mt-2 rounded-md flex place-items-start gap-4 px-2 py-2"
>
  <!-- Left Column -->
  <div class="w-1/4 h-full border-r border-solid border-stone-300">
    <ul class="list-inside  mx-3">
      <li
        v-for="category in parentCategories"
        :key="category.id"
        class="p-2 cursor-pointer"
        href="/product-list"
        @mouseenter="() => chosenCategory = category">

        <button class="inline-block border-b border-stone-300 shadow rounded-sm p-1 w-full hover:bg-stone-300 transition-colors duration-100"
              :class="active(category)">
          {{ category.name }}
    </button>  
      </li>
    </ul>
  </div>

  <!-- Middle Column -->
   <div class="w-1/4 h-full border-r border-solid border-stone-300">
  <ul class="list-inside mx-3">
    <li
      v-for="category in getChildrenOf(chosenCategory)"
      :key="category.id"
      class="p-2 cursor-pointer"
      @mouseenter="() => chosenSubCategory = category"
    >
      <button class="inline-block border-b border-stone-300 shadow rounded-sm p-1 w-full  hover:bg-stone-300 transition-colors duration-100"
      :class="activeSub(category)">
        {{ category.name }}
  </button>
    </li>
  </ul>
</div>

  <!-- Right Column -->
      <div class="w-1/2 h-full">
    <div class="grid grid-cols-6 gap-6 gap-y-10 pt-2">
      <div
        v-for="product in chosenProducts"
        :key="product.id"
        class="w-full h-20 bg-stone-300 flex flex-col justify-center items-center rounded-sm"
      >
        <div class="w-full bg-sky-50 h-2/3 flex justify-center items-center shadow rounded-sm cursor-pointer">
          IMG 
        </div>
       
        <div class="bg-stone-100 w-full h-1/3 flex justify-center items-center shadow rounded-sm cursor-pointer">{{product.price}} PLN</div>
    </div>
    </div>
      
    

  </div>

</div>
</template>

<script setup lang="ts">
import { componentNames } from '#components'
import { useCategoryStore } from '~/stores/products'
import type { Category } from '~/types/category'
import type { Product } from '~/types/product'



const categoryStore = useCategoryStore()
const {categories, products, chosenCategory, chosenSubCategory, childCategoryMap, parentCategories, chosenProducts } = storeToRefs(categoryStore)
const { getChildrenOf } = categoryStore

const active = computed(() => (category: Category) => {
  return category?.id === chosenCategory.value?.id ? 'bg-stone-300' : ''
})
const activeSub = computed(() => (category: Category) => {
  return category?.id === chosenSubCategory.value?.id ? 'bg-stone-300' : ''
})


onMounted(() => {
  if (categoryStore.categories.length === 0) {
    categoryStore.fetchCategories()
  }

  if(categoryStore.products.length ===0) {
    categoryStore.fetchProducts()
  }
})
</script>