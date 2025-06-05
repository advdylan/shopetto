import type { Category } from "./category"

export interface Product  {
  id: number,
  category: Category | null
  name: string,
  price: number
}