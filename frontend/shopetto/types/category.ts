export interface Category {
  name: string
  slug: string
  parent: Category | null 
}