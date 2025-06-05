// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from "@tailwindcss/vite"
export default defineNuxtConfig({

  compatibilityDate: '2025-05-15',
  devtools: { enabled: true },
  css: [`~/assets/css/main.css`],
  
  icon: {
    mode: 'css',
    cssLayer: 'base'
  },

  vite: {
    plugins: [
    ],
  },
  postcss: {
    plugins: {
    '@tailwindcss/postcss': {},
    autoprefixer: {}
  }
  },
  
  modules: ["@pinia/nuxt", "@nuxt/icon"],

  runtimeConfig: {
    public: {
      apiBase: 'http://127.0.0.1:8000'
    }
  }
})