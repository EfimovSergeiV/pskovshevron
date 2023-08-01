<script setup>
  const config = useRuntimeConfig()
  const route = useRoute()
  const router = useRouter()

  const { data: categories } = await useFetch(`${ config.public.baseURL }s/ct/`)
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
  <div class="min-h-screen flex items-center py-8">


    <div class="container mx-auto max-w-screen-xl">


      <div class="flex items-start justify-between py-2">
        <div>
          <nuxt-link :to="{ name: 'index' }">Вернуться на главную</nuxt-link>
        </div>
        <div class="">
          <p class="text-2xl font-semibold">{{ product.title }}</p>
        </div>
      </div>

      <div class="flex items-center justify-end gap-0.5 py-2">
        <div v-for="category in categories" :key="category">
          <button  v-if="product.category.includes(category.id)" class="bg-gray-700 rounded-2xl px-10 py-1">
            <p class="text-sm">{{ category.title }}</p>
          </button>
          
        </div>
      </div>

      <div class="flex items-start">
        
        <div class="h-[28rem] w-[28rem]">
          <img :src="product.product_images[0].image" class="rounded-md h-[16rem] w-[16rem] border border-white/20" />
        </div>

        <div class=" w-full">
          <div class="grid grid-cols-1 gap-4">

            <div class="border rounded-lg shadow bg-gray-800 border-gray-700 px-4 py-4">
              <div class="" v-html="product.description"></div>
              <div class=" flex items-center justify-end py-6">
                <a href="#" target="_blank" class="flex items-center gap-4 group relative w-[14rem]">
                  <p class="text-sm uppercase font-semibold"> Приобрести на</p>
                  <img src="/wildberries.webp" class="w-[100px] group-hover:w-[105px] transition-all duration-300 absolute right-0" />
                </a>
              </div> 
              <div class="flex justify-end">
                <div class="flex items-center gap-20">
                  <div class="flex items-center gap-2">
                    <p class="text-2xl font-semibold">{{ product.price }}</p>
                    <div class=" mdi mdi-24px mdi-currency-rub"></div>
                  </div>
                  
                  
                  <button class="text-white uppercase font-semibold bg-gradient-to-br from-sky-700 to-sky-600 focus:ring-0 focus:outline-none focus:ring-blue-300/0 rounded-lg text-sm px-8 py-4 text-center transition-all">Добавить в корзину</button>
                </div>
              </div>
             
            </div>

            <div class=" border rounded-lg shadow bg-gray-800 border-gray-700 px-4 py-4">
              <div class="my-6">

                <div v-for="property in product.product_properties" :key="property.id" class="">
                  <div v-if="property.name && property.value" class="flex items-center justify-between border-b border-gray-600 my-4">
                    <p class="text-sm">{{ property.name }}</p>
                    <p class="text-sm">{{ property.value }}</p>
                  </div>
                  <div v-else class="flex items-center justify-between my-1">
                    <p v-if="property.name" class="text-base font-semibold">{{ property.name }}:</p>
                    <div v-else class=""></div>
                    <p class="text-sm">{{ property.value }}</p>
                  </div>


                </div>

              </div>              
            </div>




          </div>

        </div>

      </div>


    </div>

    
    

  </div>
</template>