import { defineStore } from 'pinia'
import type { Category } from '~/types/category'

export const useCategoryStore = defineStore('category', () => {
  const config = useRuntimeConfig()
  let timeout: ReturnType<typeof setTimeout> | null = null

  // State
  const categories = ref<Category[]>([])
  const dropdownHover = ref(false)
  const chosenCategory = ref<Category | null>(null)
  const chosenSubCategory = ref<Category | null>(null)

  // Actions
  async function fetchCategories() {
    const url = `${config.public.apiBase}/api/categories/`

    try {
      const response = await fetch(url)
      if (!response.ok) throw new Error('Failed to fetch categories')

      const data: Category[] = await response.json()
      console.log('Fetched categories:', data)

      categories.value = data
    } catch (error) {
      console.error('Failed to fetch categories', error)
    }
  }

  function onMouseEnter() {
    if (timeout) clearTimeout(timeout)
    
    dropdownHover.value = true // activates the dropdown
    chosenCategory.value = categories.value[0] // choosing first category to highlight
  }

  function onMouseLeave() {
    timeout = setTimeout(() => {
      dropdownHover.value = false
      chosenCategory.value = null
    }, 100)
  }

  return {
    categories,
    dropdownHover,
    chosenCategory,
    fetchCategories,
    onMouseEnter,
    onMouseLeave
  }
})