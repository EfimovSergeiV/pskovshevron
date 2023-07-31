<script setup>
  const config = useRuntimeConfig()
  const route = useRoute()
  const router = useRouter()

  const { data: product } = await useFetch(`${ config.public.baseURL }s/prod/${route.params.id}`)

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
  <div class="min-h-screen flex items-center">


    <div class="container mx-auto max-w-screen-xl">


      <div class="flex items-start py-4">
        <nuxt-link :to="{ name: 'index'}">Вернуться назад</nuxt-link>
      </div>


      <div class="flex items-start">
        <div class="h-[28rem] w-[28rem]">
          <img :src="product.product_images[0].image" class="rounded-md h-[16rem] w-[16rem] border border-white/20" />
        </div>
        <div class=" w-full">
          <div class="grid grid-cols-1 gap-4">

            <div class="border rounded-lg shadow bg-gray-800 border-gray-700 px-4">
              <div class="py-4">
                <p class="text-2xl">{{ product.title }}</p>
              </div>
              <div class="" v-html="product.description"></div>
              <div class="flex justify-end my-4">
                <div class="flex items-center gap-20">
                  <p class="text-2xl mdi mdi-currency-rub">
                    {{ product.price }}
                  </p>
                  <button class="text-white uppercase font-semibold bg-gradient-to-br from-sky-700 to-sky-600 focus:ring-0 focus:outline-none focus:ring-blue-300/0 rounded-lg text-sm px-8 py-4 text-center transition-all">Добавить в корзину</button>

                </div>
              </div>
              <div class=" flex items-center justify-end py-6">
                <a href="#" target="_blank" class="flex items-center gap-4 group relative w-[14rem]">
                  <p class="text-sm uppercase font-semibold"> Приобрести на</p>
                  <img src="/wildberries.webp" class="w-[100px] group-hover:w-[105px] transition-all duration-300 absolute right-0" />
                </a>
              </div>              
            </div>

            <div class=" border rounded-lg shadow bg-gray-800 border-gray-700 px-4 py-4">
              <div class="my-6">

                <div v-for="property in product.product_properties" :key="property.id" class="flex items-center justify-between border-b border-gray-600 my-4">
                  <p class="text-sm">{{ property.name }}</p>
                  <p class="text-sm">{{ property.value }}</p>
                </div>

              </div>              
            </div>




          </div>

        </div>

      </div>


    </div>

    
    

  </div>
</template>