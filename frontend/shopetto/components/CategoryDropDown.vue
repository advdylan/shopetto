<template>
  <div
  v-if="categoryStore.dropdownHover"
  @mouseenter="categoryStore.onMouseEnter"
  @mouseleave="categoryStore.onMouseLeave()"
  class="bg-stone-100 w-320 h-85 shadow-lg mt-2 rounded-md flex place-items-start gap-4 px-2 py-2"
>
  <!-- Left Column -->
  <div class="w-1/4 h-full border-r border-solid border-stone-300">
    <ul class="list-inside  mx-3">
      <li
        v-for="category in parentCategories"
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
      class="p-2"
    >
      <span class="inline-block border-b border-stone-300 shadow rounded-sm p-1 w-full">
        {{ category.name }}
      </span>
    </li>
  </ul>
</div>

  <!-- Right Column -->
  <div class="w-2/4 h-full mr-10">Right</div>
</div>
</template>

<script setup lang="ts">
import { componentNames } from '#components'
import { useCategoryStore } from '~/stores/products'
import type { Category } from '~/types/category'
import type { Product } from '~/types/product'



const categoryStore = useCategoryStore()
const {categories, chosenCategory} = storeToRefs(categoryStore)

const parentCategories = computed(() => {
  return categories.value.filter(category => category.parent === null)
})

const childCategoryMap = computed(() => {
  const map = new Map<number, Category[]>()
  for (const cat of categories.value) {
    const parentId = cat.parent?.id
    if (parentId != null) {
      if (!map.has(parentId)) {
        map.set(parentId, [])
      }
      map.get(parentId)!.push(cat)
    }
  }
  return map
})

function getChildrenOf(category: Category | null) {
  return category ? childCategoryMap.value.get(category.id) || [] : []
}

const productMap = computed(() => {
  return 0
})

function getProductOf(product: Product | null) {
  return 0
}

const active = computed(() => (category: Category) => {
  return category?.id === chosenCategory.value?.id ? 'bg-stone-400' : ''
})


onMounted(() => {
  if (categoryStore.categories.length === 0) {
    categoryStore.fetchCategories()
  }
  
})
</script>