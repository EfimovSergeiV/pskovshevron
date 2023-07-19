// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  app: {
    head: {
      title: 'pskovshevron.ru - Купить шевроны во Пскове',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { 
          hid: 'description', 
          name: 'description', 
          content: 'pskovshevron.ru - Купить шевроны во Пскове вдарыорвоарловыраыл' 
        },
        { name: 'format-detection', content: 'telephone=yes' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.png' }
      ]
    },

    pageTransition: { name: 'page', mode: 'out-in' },

    // pageTransition: {
    //   name: 'fade',
    //   mode: 'out-in' // default
    // },
    // layoutTransition: {
    //   name: 'slide',
    //   mode: 'out-in' // default
    // }
  },

  modules: [
    '@nuxtjs/tailwindcss'
  ],

  css: [
    '~/assets/css/main.css',
    '~/assets/css/tailwind.css',
    '@mdi/font/css/materialdesignicons.min.css',
  ],

  runtimeConfig: {
    public: {
      baseURL: process.env.BASE_URL || 'http://127.0.0.1:8000/',
    },
  },

})
