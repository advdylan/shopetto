<template>
  <div
  v-if="categoryStore.dropdownHover"
  @mouseenter="categoryStore.onMouseEnter"
  @mouseleave="categoryStore.onMouseLeave()"
  class="bg-gradient-to-r from-ali2 from-10% via-ali1 via-30% to-ali2 to-90% w-320 h-85 shadow-lg mt-2 rounded-md flex place-items-start gap-4 px-2 py-2"
>
  <!-- Left Column -->
  <div class="w-1/4 h-full border-r border-solid border-stone-300">
    <ul class="list-inside  mx-3">
      <li
        v-for="category in parentCategories"
        :key="category.id"
        class="p-2 cursor-pointer "
        @mouseenter="() => chosenCategory = category">

        <span class="inline-block border-b border-stone-300 shadow rounded-sm p-1 w-full hover:bg-stone-400"
              :class="active(category)">
          {{ category.name }}
        </span>
        
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
      <span class="inline-block border-b border-stone-300 shadow rounded-sm p-1 w-full"
      :class="activeSub(category)">
        {{ category.name }}
      </span>
    </li>
  </ul>
</div>

  <!-- Right Column -->
      <div class="w-1/2 h-full">
    <div class="grid grid-cols-3 gap-2">
      <span
        v-for="product in chosenProducts"
        :key="product.id"
        class="w-full h-20 bg-gray-200 flex items-center justify-center rounded"
      >
        <div class=""></div>
      </span>
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
const {categories, products, chosenCategory, chosenSubCategory, childCategoryMap, } = storeToRefs(categoryStore)
const { getChildrenOf } = categoryStore

const parentCategories = computed(() =>
  categories.value
    .filter(cat => cat.parent === null)
)

const chosenProducts = computed(() => {
  return products.value.filter(product => product.category?.id === chosenSubCategory.value?.id)

})

const productMap = computed(() => {
  return 0
})

function getProductOf(product: Product | null) {
  return 0
}

const active = computed(() => (category: Category) => {
  return category?.id === chosenCategory.value?.id ? 'bg-stone-400' : ''
})
const activeSub = computed(() => (category: Category) => {
  return category?.id === chosenSubCategory.value?.id ? 'bg-stone-400' : ''
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