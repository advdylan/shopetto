<template>
  <div class="bg-stone-300 flex flex-col md:flex-row items-start justify-between gap-1 h-auto md:h-40 p-1">
    <!--PHOTO & ITEM DESCRIPTION-->
    <div class="bg-stone-200 flex flex-col gap-1 md:flex-row items-start justify-between h-auto md:h-full w-full md:w-3/4">
      <div class="bg-stone-50 h-40 md:h-full w-full md:w-1/4">IMG</div>
      <div class="bg-stone-50 h-40 md:h-full w-full md:w-3/4">OPIS</div>

    </div>

    <!--PRICE & DELIVERY & BUTTONS-->
    <div class="bg-stone-100 h-40 md:h-full w-full md:w-1/4">
      CENY
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