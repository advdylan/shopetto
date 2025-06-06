<template>
  <div
  v-if="categoryStore.dropdownHover"
  @mouseenter="categoryStore.onMouseEnter"
  @mouseleave="categoryStore.onMouseLeave()"
  class="bg-gradient-to-r from-ali2 from-10% via-ali1 via-30% to-ali2 to-90% w-320 h-85 shadow-lg mt-2 rounded-md flex place-items-start gap-4 px-2 py-2"
>

HOLA AMIGO
</div>
</template>

<script setup lang="ts">
import { componentNames } from '#components'
import { useCategoryStore } from '~/stores/products'
import type { Category } from '~/types/category'
import type { Product } from '~/types/product'



const categoryStore = useCategoryStore()
const {categories, products, chosenCategory, chosenSubCategory, childCategoryMap, parentCategories } = storeToRefs(categoryStore)
const { getChildrenOf } = categoryStore



const chosenProducts = computed(() => {
  return products.value.filter(product => product.category?.id === chosenSubCategory.value?.id)

})


const active = computed(() => (category: Category) => {
  return category?.id === chosenCategory.value?.id ? 'bg-stone-400' : ''
})
const activeSub = computed(() => (category: Category) => {
  return category?.id === chosenSubCategory.value?.id ? 'bg-stone-400' : ''
})


onMounted(() => {
  
})
</script>