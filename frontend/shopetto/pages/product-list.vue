<template>
 
      <div class="bg-stone-100 h-screen shadow-lg mt-2 rounded-md place-items-start gap-6 px-6 py-6">
        <!-- HEADER -->
        <div class="bg-stone-200 rounded-ms h-30 flex justify-between  place-items-start w-full ">
          <div class="flex flex-col justify-between w-1/2 h-full">
            <div class="text-xl px-8 py-4 block" >{{ chosenCategoryForList?.name }}</div>
            <div class="text-lg px-8 py-4 block"> {{chosenSubCategoryForList?.name}} </div>
          </div>

          <div class="flex flex-col justify-between place-items-end w-1/2 h-full">

            <div class="px-2 py-2" >
              <button class="flex items-center gap-2 bg-stone-50 text-stone-700 p-2 rounded-lg hover:bg-stone-200 transition-colors duration-200 shadow-sm cursor-pointer">
              <Icon size="1.5em" name="mdi-light:unfold-less-horizontal" />
              <span class="font-medium">Sort</span>
              </button>
            </div>

            <div class="px-2 py-2" >
              <button class="flex items-center gap-2 bg-stone-50 text-stone-700 p-2 rounded-lg hover:bg-stone-200 transition-colors duration-200 shadow-sm cursor-pointer">
              <Icon size="1.5em" name="mdi-light:heart" />
              <span class="font-medium">Save</span>
              </button>
            </div>
        
          </div>
        </div>
        
        <!--BODY-->
        <div class="bg-stone-200 overflow-y-auto flex justify-between place-items-start w-full gap-4 px-4 py-2 h-full">

          <!--LEFT CATEGORY PANEL-->
          <div class="bg-stone-100 flex flex-col rounded-md w-1/4 h-full" >
            <div class="font-semibold text-sm md:text-base lg:text-lg  px-4 py-2">Categories</div>
              <ul class="mx-3">
                <li
                  v-for="category in parentCategories"
                  :key="category.id"
                  class="p-2 cursor-pointer"
                  href="/product-list"
                  >

                  <button class="cursor-pointer flex gap-2"
                        @click="toggleCategory(category)"
                        :class="activeCategory(category, 'class')">
                    {{ category.name }} <span class="flex items-center">
                      <Icon size="1.1em" :name="activeCategory(category,'name')"></Icon>
                    </span>
                  </button>
                  <div v-if="category.id === chosenCategoryForList?.id">
                      <ul class="list-inside mx-3">
                        <li
                          v-for="category in getChildrenOf(chosenCategoryForList)"
                          @click="() => chosenSubCategoryForList = category"
                          :key="category.id"
                          class="p-2 cursor-pointer"
                          :class="activeSubCategory(category)">
                          {{ category.name }}
                      
                      </li>
                      </ul>
                     </div>
                    
                </li>
              </ul>
          </div>


          <!--RIGHT PRODUCT PANEL-->
          <div class="bg-stone-100 flex flex-col justify-between gap-1 rounded-md w-3/4 h-full">
            <div v-for="product in chosenProducts">
              <StoreProduct/>

            </div>
          </div>
        </div>
        

      </div>
 
  
</template>

<script setup lang="ts">
import StoreProduct from '~/components/microcomponents/StoreProduct.vue'
import { useCategoryStore } from '~/stores/products'
import type { Category } from '~/types/category'
import type { Product } from '~/types/product'



const categoryStore = useCategoryStore()
const {categories, products, childCategoryMap, parentCategories, chosenCategoryForList, chosenSubCategoryForList } = storeToRefs(categoryStore)
const { getChildrenOf } = categoryStore



const chosenProducts = computed(() => {
  return products.value.filter(product => product.category?.id === chosenSubCategoryForList.value?.id)

})


function activeCategory( category: Category,  kind: 'class' | 'name' ): string {

  const isActive = category.id === chosenCategoryForList.value?.id

  if (kind === 'class') {
    return isActive ? 'font-semibold underline' : ''
  }

  // kind === 'name'
  return isActive ? 'mdi-light:minus-box' : 'mdi-light:plus-box'
}
const activeSubCategory = computed(() => (category: Category) => {
  return category?.id === chosenSubCategoryForList.value?.id ? 'font-semibold underline' : ''
})




function toggleCategory(category: Category) {
  if (category?.id === chosenCategoryForList.value?.id) {
    console.log("Same category clicked")
    chosenCategoryForList.value = null
    return
  }

  chosenCategoryForList.value = category

}

onMounted(() => {

})
</script>