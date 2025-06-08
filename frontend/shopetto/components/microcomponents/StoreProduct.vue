<template>
  <div class="bg-stone-300 flex items-start justify-between gap-1 h-40 p-1">
    <!--PHOTO & ITEM DESCRIPTION-->
    <div class="bg-stone-200 flex items-start justify-between h-full w-3/4">
      <div class="bg-stone-50 h-full w-1/4">IMG</div>

    </div>

    <!--PRICE & DELIVERY & BUTTONS-->
    <div class="bg-stone-100 h-full w-1/4">

    </div>
  </div>

</template>

<script setup lang="ts">
import { useCategoryStore } from '~/stores/products'
import type { Product } from '~/types/product'

const categoryStore = useCategoryStore()
const {chosenProducts} = storeToRefs(categoryStore)

const props = defineProps<{
  product?: Product
}>()



</script>