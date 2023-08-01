<script setup>
  const config = useRuntimeConfig()
  const route = useRoute()
  const router = useRouter()
  const shopStore = useShopStore()

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
  <div class="min-h-screen py-4">

    <div class="container mx-auto px-8 max-w-screen-xl">
      <div class="py-4">
        <div class="flex flex-wrap gap-x-4 gap-y-2 justify-start">
          
          <nuxt-link :to="{ name: 'index'}" class="bg-gray-700 rounded-2xl px-14 py-1">
            <p class="text-sm text-gray-100">Все шевроны</p>
          </nuxt-link>

          <nuxt-link :to="{ name: 'index', query: { ct: category.id ,page: 1}}" v-for="category in categories" :key="category.id" class="bg-gray-700 rounded-2xl px-12 py-1">
            <p class="text-sm text-gray-100">{{ category.title }} </p>
          </nuxt-link>


        </div>
      </div>
    </div>


    <div class="container mx-auto px-8 max-w-screen-xl">
      <div v-if="pages.length > 1" class="flex items-center justify-end">

        <ul class="flex items-center gap-0.5 font-semibold">
          <li>
            <nuxt-link :to="{ name: 'index', query: {...route.query, page: 1 }}" class="w-8 h-8 flex items-center justify-center  rounded-l-sm border  bg-gray-800 border-gray-700 text-gray-400 hover:bg-gray-700 hover:text-white">
              &lt;
            </nuxt-link>
          </li>
          <li v-for="(page, pk) in pages" :key="pk">
            <nuxt-link :to="{ name: 'index', query: { ...route.query, page: page }}">
              <div v-if="Number(current) === Number(page)" class="w-8 h-8 flex items-center justify-center  border border-gray-600 bg-gray-700 text-white">{{ page }}</div>
              <div v-else class="w-8 h-8 flex items-center justify-center  rounded-r-sm border  bg-gray-800 border-gray-700 text-gray-400 hover:bg-gray-700 hover:text-white">{{ page }}</div>
            </nuxt-link>
          </li>
          <li>
            <nuxt-link :to="{ name: 'index', query: {...route.query, page: Math.ceil(products.count/36)}}" class="w-8 h-8 flex items-center justify-center  rounded-r-sm border  bg-gray-800 border-gray-700 text-gray-400 hover:bg-gray-700 hover:text-white">
              &gt;
            </nuxt-link>
          </li>
        </ul>

        </div>
    </div>



    <div class="container mx-auto px-8 max-w-screen-xl">
      <div class="py-4">
        <div v-if="products.results.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
          <transition-group name="fade">
            <div v-for="product in products.results" :key="product.id">
              <div class="w-full md:max-w-sm border rounded-lg shadow bg-gray-800 border-gray-700">
                
                <nuxt-link :to="{ name: 'prod-id', params: { id: product.id}}">
                  <img v-if="product.product_images.length > 0" class=" rounded-t-lg select-none" :src="product.product_images[0].image" alt="product image" />
                  <div v-else class=" rounded-t-lg h-[312px]"></div>
                </nuxt-link>

                <div class="py-2 px-2">

                    <nuxt-link :to="{ name: 'prod-id', params: { id: product.id}}" class="text-lg font-semibold tracking-tight select-none">{{ product.title }}</nuxt-link>
                  
                </div>

                <div class="px-2 flex">
                  <div v-if="product.description.length > 160" class="text-xs select-none" v-html="product.description.slice(0, 160) + '...'"></div>
                  <div v-else class="text-xs" v-html="product.description"></div>
                </div>

                <div class="px-5 py-4">

                  <div class="flex items-center justify-between">
                      <span class="text-3xl font-bold text-white mdi mdi-currency-rub select-none"> {{ product.price.toLocaleString() }}</span>
                      <button @click="shopStore.addProduct(product)" class="text-white bg-gradient-to-br from-sky-700 to-sky-600 font-semibold focus:ring-0 focus:outline-none focus:ring-blue-300/0 rounded-lg text-sm w-28 py-2 text-center transition-all">
                        <transition name="fade" mode="out-in">
                          <div v-if="shopStore.productInCart(product.id)" class="">
                            <p class=" select-none">В корзине</p>
                          </div>
                          <div v-else class="">
                            <p class=" select-none">Купить</p>
                          </div>
                        </transition>
                        
                      </button>
                  </div>
                </div>

              </div>
            </div>
          </transition-group>
        </div>
        <div v-else class="flex min-h-screen items-center justify-center">
          <p class="text-2xl">Ничего не найдено</p>
        </div>
      </div>
    </div>

    <div class="container mx-auto px-8 max-w-screen-xl">
      <div v-if="pages.length > 1" class="flex items-center justify-end">

        <ul class="flex items-center gap-0.5 font-semibold">
          <li>
            <nuxt-link :to="{ name: 'index', query: {...route.query, page: 1 }}" class="w-8 h-8 flex items-center justify-center  rounded-l-sm border  bg-gray-800 border-gray-700 text-gray-400 hover:bg-gray-700 hover:text-white">
              &lt;
            </nuxt-link>
          </li>
          <li v-for="(page, pk) in pages" :key="pk">
            <nuxt-link :to="{ name: 'index', query: { ...route.query, page: page }}">
              <div v-if="Number(current) === Number(page)" class="w-8 h-8 flex items-center justify-center  border border-gray-600 bg-gray-700 text-white">{{ page }}</div>
              <div v-else class="w-8 h-8 flex items-center justify-center  rounded-r-sm border  bg-gray-800 border-gray-700 text-gray-400 hover:bg-gray-700 hover:text-white">{{ page }}</div>
            </nuxt-link>
          </li>
          <li>
            <nuxt-link :to="{ name: 'index', query: {...route.query, page: Math.ceil(products.count/36)}}" class="w-8 h-8 flex items-center justify-center  rounded-r-sm border  bg-gray-800 border-gray-700 text-gray-400 hover:bg-gray-700 hover:text-white">
              &gt;
            </nuxt-link>
          </li>
        </ul>

        </div>
    </div>
  </div>
</template>