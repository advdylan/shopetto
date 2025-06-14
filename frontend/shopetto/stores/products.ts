import { defineStore } from 'pinia'
import CategoryDropDown from '~/components/CategoryDropDown.vue'
import type { Category } from '~/types/category'
import type { Product } from '~/types/product'

export const useCategoryStore = defineStore('category', () => {
  const config = useRuntimeConfig()
  let timeout: ReturnType<typeof setTimeout> | null = null

  // State
  const categories = ref<Category[]>([])
  const products = ref<Product[]>([])
  const dropdownHover = ref(false)
  // Chosen categories for Navbar
  const chosenCategory = ref<Category | null>(null)
  const chosenSubCategory = ref<Category | null>(null)
  // Chosen categories for ProductList
  const chosenCategoryForList = ref<Category | null>(null)
  const chosenSubCategoryForList = ref<Category | null>(null)

  // Actions
  async function fetchCategories() {
    const url = `${config.public.apiBase}/api/categories/`

    try {
      const response = await fetch(url)
      if (!response.ok) throw new Error('Failed to fetch categories')

      const data: Category[] = await response.json()
      console.log('Fetched categories:', data)


      //temporary displaying the first categories with it's first subcategory
      categories.value = data
      chosenCategoryForList.value = categories.value[0]

      const childrens = getChildrenOf(chosenCategoryForList.value)
      chosenSubCategoryForList.value = childrens[0]
        

      
    } catch (error) {
      console.error('Failed to fetch categories', error)
    }
  }

  async function fetchProducts() {
    const url = `${config.public.apiBase}/api/products/`

    try {
      const response = await fetch(url)
      if (!response.ok) throw new Error('Failed to fetch products')

      const data: Product[] = await response.json()
      console.log(`Fetched products:`, data)
      products.value = data
    } catch(error) {
      console.error('Failed to fetch products', error)
    }
  }

  const chosenProducts = computed(() => {
    return products.value.filter(product => product.category?.id === chosenSubCategory.value?.id)
  })

  const parentCategories = computed(() =>
    categories.value
      .filter(cat => cat.parent === null)
  )
  
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

  

  function onMouseEnter() {
    if (timeout) clearTimeout(timeout)
    
    dropdownHover.value = true // activates the dropdown

    chosenCategory.value = categories.value[0] || null // choosing first category to highlight

    const children = getChildrenOf(categories.value[0])
    chosenSubCategory.value = children[0]
    //console.log(`childen: ${JSON.stringify(children[0])}`)
    //console.log(`firstSubCategories: ${firstSubCategories}`)
    //console.log(`ChosenSub: ${chosenSubCategory.value}`)
  }

  function onMouseLeave() {
    timeout = setTimeout(() => {
      dropdownHover.value = false
      chosenCategory.value = null
    }, 100)
  }

  function isParentCategory(category: Category) {
    if (category.parent === null) {
      console.log(`Parent Category Detected: ${category}`)
      return true
    }
    return false
  }

  return {
    categories,
    dropdownHover,
    chosenCategory,
    products,
    chosenSubCategory,
    childCategoryMap,
    parentCategories,
    chosenProducts,
    chosenCategoryForList,
    chosenSubCategoryForList,
    fetchCategories,
    fetchProducts,
    onMouseEnter,
    onMouseLeave,
    getChildrenOf,
    isParentCategory,
    
  }
})