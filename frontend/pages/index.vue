<script setup>
  const config = useRuntimeConfig()
  const route = useRoute()
  const router = useRouter()

  const { data: categories } = await useFetch(`${ config.public.baseURL }s/ct/`)
  const { data: products } = await useFetch(`${ config.public.baseURL }s/prods/`)
  // const { data: products1 } = await useFetch(`${ config.public.baseURL }s/prods/`)
  // const { data: products2 } = await useFetch(`${ config.public.baseURL }s/prods/`)
  // const { data: products3 } = await useFetch(`${ config.public.baseURL }s/prods/`)
  // const { data: products4 } = await useFetch(`${ config.public.baseURL }s/prods/`)
  // const { data: products5 } = await useFetch(`${ config.public.baseURL }s/prods/`)


  const scrollToTop = () => {
      window.scrollTo({ top: 0 })
    }

    watch(() => route.fullPath, async (fullPath) => {
        const { data: prods }  = await useFetch(`${ config.public.baseURL }s/prods/`, { params: route.query })
        products.value = ( await prods.value )
        scrollToTop()
      }
    )


  const current = computed(() => route.query.page || 1 )
  const pages = computed(() => {
    if (current.value < 7) {
      return Array.from({length: Math.ceil(products.value.count/36)}, (v, k) => k + 1).slice(0, 7)
    } else {
      return Array.from({length: Math.ceil(products.value.count/36)}, (v, k) => k + 1).slice(Number(current.value) - 4, Number(current.value) + 3)
    }
  })

</script>


<template>
  <div class="min-h-screen">

    <div class="container mx-auto max-w-screen-xl">
      <div class="py-4">
        <div class="flex flex-wrap gap-x-4 gap-y-2 justify-start">
          
          <button class="bg-gray-700 rounded-2xl px-16 py-1">
            <p class="text-sm text-gray-100">Все шевроны</p>
          </button>

          <button v-for="category in categories" :key="category.id" class="bg-gray-700 rounded-2xl px-16 py-1">
            <p class="text-sm text-gray-100">Категория {{ category.title }} </p>
          </button>


        </div>
      </div>
    </div>



    <div class="container mx-auto max-w-screen-xl">
      <div v-if="pages.length > 1" class="">

        <ul class="flex items-center gap-0.5 font-semibold">
          <li>
            <nuxt-link :to="{ name: 'index', query: {...route.query, page: 1 }}" class="w-8 h-8 flex items-center justify-center text-gray-500  rounded-l-sm border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
              &lt;
            </nuxt-link>
          </li>
          <li v-for="(page, pk) in pages" :key="pk">
            <nuxt-link :to="{ name: 'index', query: { ...route.query, page: page }}">
              <div v-if="Number(current) === Number(page)" class="w-8 h-8 flex items-center justify-center text-gray-700 bg-blue-50 border border-gray-300 hover:bg-blue-100 hover:text-gray-900 dark:border-gray-600 dark:bg-gray-700 dark:text-white">{{ page }}</div>
              <div v-else class="w-8 h-8 flex items-center justify-center text-gray-500  rounded-r-sm border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">{{ page }}</div>
            </nuxt-link>
          </li>
          <li>
            <nuxt-link :to="{ name: 'index', query: {...route.query, page: Math.ceil(products.count/36)}}" class="w-8 h-8 flex items-center justify-center text-gray-500  rounded-r-sm border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
              &gt;
            </nuxt-link>
          </li>
        </ul>

        </div>
    </div>



    <div class="container mx-auto max-w-screen-xl">
      <div class="py-8">
        <div class="grid grid-cols-4 gap-2">
          <transition-group name="fade">
            <div v-for="product in products.results" :key="product.id">
              <div class="w-full max-w-sm border rounded-lg shadow bg-gray-800 border-gray-700">
                
                <a href="#">
                  <img v-if="product.product_images.length > 0" class=" rounded-t-lg" :src="product.product_images[0].image" alt="product image" />
                  <div v-else class=" rounded-t-lg h-[312px]"></div>
                </a>

                <div class="py-2 px-2">

                    <nuxt-link :to="{ name: 'prod-id', params: { id: product.id}}" class="text-lg font-semibold tracking-tight">{{ product.title }}</nuxt-link>
                  
                </div>

                <div class="px-2">
                  <div :class="'text-xs ' + `text-[${textColor}]` " v-html="product.description.slice(0, 160)"></div>
                </div>

                <div class="px-5 py-4">

                  <div class="flex items-center justify-between">
                      <span class="text-3xl font-bold text-white mdi mdi-currency-rub"> {{ product.price.toLocaleString() }}</span>
                      <a href="#" class="text-white bg-gradient-to-br from-sky-700 to-sky-600 font-semibold focus:ring-0 focus:outline-none focus:ring-blue-300/0 rounded-lg text-sm px-6 py-2 text-center transition-all">В корзину</a>
                  </div>
                </div>

              </div>
            </div>
          </transition-group>
        </div>
      </div>
    </div>

    <div v-if="pages.length > 1" class="">

      <ul class="flex items-center gap-0.5 font-semibold">
        <li>
          <nuxt-link :to="{ name: 'index', query: {...route.query, page: 1 }}" class="w-8 h-8 flex items-center justify-center text-gray-500  rounded-l-sm border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
            &lt;
          </nuxt-link>
        </li>
        <li v-for="(page, pk) in pages" :key="pk">
          <nuxt-link :to="{ name: 'index', query: { ...route.query, page: page }}">
            <div v-if="Number(current) === Number(page)" class="w-8 h-8 flex items-center justify-center text-gray-700 bg-blue-50 border border-gray-300 hover:bg-blue-100 hover:text-gray-900 dark:border-gray-600 dark:bg-gray-700 dark:text-white">{{ page }}</div>
            <div v-else class="w-8 h-8 flex items-center justify-center text-gray-500  rounded-r-sm border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">{{ page }}</div>
          </nuxt-link>
        </li>
        <li>
          <nuxt-link :to="{ name: 'index', query: {...route.query, page: Math.ceil(products.count/36)}}" class="w-8 h-8 flex items-center justify-center text-gray-500  rounded-r-sm border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
            &gt;
          </nuxt-link>
        </li>
      </ul>

    </div>

  </div>
</template>