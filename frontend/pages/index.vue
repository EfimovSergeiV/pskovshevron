<script setup>
  const config = useRuntimeConfig()
  const route = useRoute()
  const router = useRouter()

  const { data: products } = await useFetch(`${ config.public.baseURL }s/prods/`)
  const { data: products1 } = await useFetch(`${ config.public.baseURL }s/prods/`)
  const { data: products2 } = await useFetch(`${ config.public.baseURL }s/prods/`)
  const { data: products3 } = await useFetch(`${ config.public.baseURL }s/prods/`)
  const { data: products4 } = await useFetch(`${ config.public.baseURL }s/prods/`)
  const { data: products5 } = await useFetch(`${ config.public.baseURL }s/prods/`)

  const textColor = ref('#111827')

// const scrollToTop = () => {
//     window.scrollTo({ top: 0 })
//   }

//   watch(() => route.fullPath, async (fullPath) => {
//       const { data: prods }  = await useFetch(`${ config.public.baseURL }c/prods/`, { params: route.query })
//       const { data: crumbs } = await useFetch(`${ config.public.baseURL }c/breadcrumb/`, { params: route.query })
//       products.value = ( await prods.value )
//       breadcrumbs.value = ( await crumbs.value )
//       scrollToTop()
//     }
//   )
</script>


<template>
  <div class="min-h-screen">


    <div class="container mx-auto max-w-screen-xl">
      <div class="py-8">
        <div class="grid grid-cols-4 gap-8">
          <div v-for="product in products.results" :key="product.id">
            <div class="w-full max-w-sm border rounded-lg shadow bg-gray-800 border-gray-700">
              
              <a href="#">
                <img class=" rounded-t-lg" :src="product.product_images[0].image" alt="product image" />
              </a>

              <div class="py-2 px-2">
                <button >
                  <nuxt-link :to="{ name: 'prod-id', params: { id: product.id}}" class="text-lg font-semibold tracking-tight">{{ product.title }}</nuxt-link>
                </button>                    
              </div>

              <div class="px-2">
                <div :class="'text-xs ' + `text-[${textColor}]` " v-html="product.description.slice(0, 160)"></div>
              </div>

              <div class="px-5 py-4">

                <div class="flex items-center justify-between">
                    <span class="text-3xl font-bold text-white mdi mdi-currency-rub"> {{ product.price.toLocaleString() }}</span>
                    <a href="#" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-0 focus:outline-none focus:ring-blue-300/0 font-medium rounded-lg text-sm px-6 py-2 text-center transition-all">В корзину</a>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>