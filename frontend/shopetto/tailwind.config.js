module.exports = {
  content: [
    './components/**/*.{vue,js,ts}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './app.vue',
    './plugins/**/*.{js,ts}',
    './nuxt.config.{js,ts}'
  ],
  theme: {
    extend: {
      backgroundImage: {
        aluminum: 'linear-gradient(145deg, #d9d9d9, #f0f0f0, #c0c0c0)',
        'aluminum-radial': 'radial-gradient(circle at 30% 30%, #ffffff20, #d9d9d9 60%, #b0b0b0 100%)'
      },
      colors: {
        aluminum: {
          light: '#f0f0f0',
          DEFAULT: '#c0c0c0',
          dark: '#9e9e9e'
        }
      }
    }
  },
  plugins: []
}