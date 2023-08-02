<script setup>
  import { initFlowbite } from 'flowbite'
  const config = useRuntimeConfig()
  const shopStore = useShopStore()
  // initialize components based on data attribute selectors
  onMounted(() => {
      initFlowbite();
  })

  // const shopStore = useShopStore()
  // shopStore.writeShops(shops)

  onMounted(() => {
    if ("geolocation" in navigator) {
      /* местоположение доступно */
      navigator.geolocation.getCurrentPosition(position => {
        let location = {
          "latitude": position.coords.latitude, 
          "longitude": position.coords.longitude 
        }

        // shopStore.sendCoordinates(location)

        // this.sendCoordinates(location)
      });
    } else {
      /* местоположение НЕ доступно */
    }

  })

  const client = ref({
    name: null,
    contact: null,
  })

  const sendOrder = async () => {
    if ( ( client.value.name ) && ( client.value.contact ) ) {
      const { data: response } = await useFetch(`${ config.public.baseURL }s/order/`, {
        method: 'POST',
        body: {
          name: client.value.name,
          contact: client.value.contact,
          products: shopStore.cart,
        }
        
      });

      // order.value = await response.value
      // productsStore.clearCartProducts()
      // clientStore.saveClientData(clientData)

    } else {
      console.log('message err ')
    }
  }

</script>


<template>
  <div class="bg-gradient-to-br from-gray-900 via-gray-800 to-gray-700 min-h-screen text-gray-100">
    <AppHeader/>
    <slot />
    <AppFooter />


    <div id="staticModal" data-modal-backdrop="static" tabindex="-1" aria-hidden="true" class="fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative w-full max-w-2xl max-h-full">
            <!-- Modal content -->
            <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                <!-- Modal header -->
                <div class="flex items-start justify-between p-4 border-b rounded-t dark:border-gray-600">
                    <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                        <!-- {{ shopStore.city }} -->
                    </h3>
                    <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ml-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-hide="staticModal">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
                <!-- Modal body -->
                <div class="p-6 space-y-6">

                  <div class="w-full">
                    <div class="text-gray-700">

                      <div class="grid gap-2 px-1 ">
                        <transition-group tag="div" name="fade">
                          <div v-for="product in shopStore.cart" :key="product.id" class="my-4">
                            <div class="flex items-center gap-2">
                              <div class="flex justify-center items-center w-24 bg-white rounded-sm">
                                <img :src="product.product_images[0].image" class="rounded-sm w-20" />
                              </div>
                              <div class="flex justify-center w-1/2">
                                <p class="text-sm">{{ product.title }}</p>
                              </div>
                              <div class="flex justify-center w-32">
                                <button  @click="shopStore.changeQuantity(product, 'del')" class="mdi mdi-minus cursor-pointer"></button>
                                <div class="mx-2"><p>{{ product.quantity }}</p></div>
                                <button @click="shopStore.changeQuantity(product, 'add')" class="mdi mdi-plus cursor-pointer"></button>
                              </div>

                              <div class="flex justify-center w-32"><p class="text-sm">{{ product.price.toLocaleString() }} руб/шт</p></div>
                              <div class="flex justify-center">
                                <button @click="shopStore.addProduct(product)" class="mdi mdi-24px mdi-close cursor-pointer"></button>
                              </div>
                              
                            </div>
                            
                          </div>
                        </transition-group>
                      </div>


                      <div class="">
                        <div class="grid grid-cols-1 md:grid-cols-2 items-center gap-8 py-4">

                          <div class="">
                            <label for="email-address-icon" class="block mb-2 text-sm font-medium text-gray-500">Как вас зовут?</label>
                            <div class="relative">
                              <div class="absolute inset-y-0 left-0 flex items-center pl-3.5 pointer-events-none">
                                <div class="absolute inset-y-0 left-0 flex items-center pl-3.5 pointer-events-none">
                                  <div class="w-4 h-4 text-gray-500 dark:text-gray-400 mdi mdi-contacts"></div>
                                </div>
                              </div>
                              <input v-model="client.name" type="text" id="email-address-icon" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-500 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Иван Иванов">
                            </div>              
                          </div>

                          <div class="">
                            <label for="email-address-icon" class="block mb-2 text-sm font-medium text-gray-500">Как с вами связаться?</label>
                            <div class="relative">
                              <div class="absolute inset-y-0 left-0 flex items-center pl-3.5 pointer-events-none">
                                <div class="w-4 h-4 text-gray-500 dark:text-gray-400 mdi mdi-contacts"></div>
                              </div>
                              <input v-model="client.contact"  type="text" id="email-address-icon" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-500 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@mail.ru или 89121234567">
                            </div>
                          </div>

                        </div>
                      </div>


                    </div>
                  </div>
                
                
                
                
                </div>

                <div class="flex items-center p-6 space-x-2 border-t border-gray-200 rounded-b dark:border-gray-600">
                    <button @click="sendOrder()" type="button" class="text-white bg-gradient-to-br from-sky-700 to-sky-600 focus:ring-0 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center transition-all">Отправить</button>
                    <button data-modal-hide="staticModal" type="button" class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600">Закрыть окно</button>
                </div>
            </div>
        </div>
    </div>


  </div>
</template>