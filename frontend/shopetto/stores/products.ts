import {defineStore} from 'pinia'
import type { Category } from '~/types/category'


let timeout: ReturnType<typeof setTimeout> | null = null

export const useCategoryStore = defineStore('category', {
  state: () => ({
    categories: [] as Category[],
    dropdownHover: false,
    
  }),
  actions: {

    async fetchCategories() {
      const config = useRuntimeConfig()
      const url = `${config.public.apiBase}/api/categories/`

      try {
        const respond = await fetch(url)
        if (!respond.ok) throw new Error('Failed to fetch categories')

        const data: Category[] = await respond.json()
        console.log('Fetched categories:', data)

        this.categories = data
      } catch (error) {
        console.error('Failed to fetch categories', error)
      }
},
    onMouseEnter() {
      console.log("mouseEnter")
      if (timeout) clearTimeout(timeout)
      this.dropdownHover = true
    },
    onMouseLeave() {
      console.log(timeout)
      timeout = setTimeout(() => {
        this.dropdownHover = false
      }, 100)
    },

  }
})