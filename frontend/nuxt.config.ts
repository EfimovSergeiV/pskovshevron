// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  app: {
    head: {
      title: 'Псков Шеврон - Шевроны в Пскове по вашему дизайну',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { 
          hid: 'description', 
          name: 'description', 
          content: 'pskovshevron - Купить и изготовить шевроны во Пскове' 
        },
        { 
          hid: 'keywords', 
          name: 'keywords', 
          content: 'Псков, Шевроны, Купить, Изготовить' 
        },
        { name: 'format-detection', content: 'telephone=yes' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.png' }
      ]
    },

    pageTransition: { name: 'page', mode: 'out-in' },

  },

  modules: [
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt',
    '@artmizu/yandex-metrika-nuxt',
  ],

  yandexMetrika: {
    id: '94554922'
  },

  pinia: {
    autoImports: [
      // automatically imports `defineStore`
      'defineStore', // import { defineStore } from 'pinia'
      ['defineStore', 'definePiniaStore'], // import { defineStore as definePiniaStore } from 'pinia'
    ],
  },

  imports: {
    dirs: ['stores'],
  },

  css: [
    '~/assets/css/main.css',
    '~/assets/css/tailwind.css',
    '@mdi/font/css/materialdesignicons.min.css',
  ],

  runtimeConfig: {
    public: {
      baseURL: process.env.BASE_URL || 'https://api.pskovshevron.ru/',
      // baseURL: process.env.BASE_URL || 'http://127.0.0.1:8000/',
    },
  },

})
