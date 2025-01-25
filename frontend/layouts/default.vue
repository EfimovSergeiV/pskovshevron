<script setup>
  import { initFlowbite } from 'flowbite'
  import { Modal } from 'flowbite'
  
  const config = useRuntimeConfig()

  const { data: contacts } = await useFetch(`${ config.public.baseURL }contacts/`)

  const shopStore = useShopStore()
  // initialize components based on data attribute selectors
  onMounted(() => {
      initFlowbite();
  })


  // onMounted(() => {
  //   if ("geolocation" in navigator) {
  //     /* местоположение доступно */
  //     navigator.geolocation.getCurrentPosition(position => {
  //       let location = {
  //         "latitude": position.coords.latitude, 
  //         "longitude": position.coords.longitude 
  //       }

  //       // shopStore.sendCoordinates(location)

  //       // this.sendCoordinates(location)
  //     });
  //   } else {
  //     /* местоположение НЕ доступно */
  //   }

  // })

  const client = ref({
    name: null,
    contact: null,
  })

  const alert = ref(false)
  const order = ref(false)
  

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

      shopStore.clearProducts()
      order.value = true

    } else {
      alert.value = true
    }
  }

</script>


<template>
  <div class="bg-gradient-to-br from-gray-900 via-gray-800 to-gray-700 min-h-screen text-gray-100 select-none">

    <div class="fixed my-2 mx-1 right-0 z-20">
      <transition-group name="fade">
        <div class="" v-for="toast in shopStore.toasts" :key="toast.id">
          
          <div v-if="toast.type === 'success'" id="toast-success" class=" flex items-center w-full max-w-xs p-4 mb-4 text-gray-500 bg-white rounded-lg shadow dark:text-gray-400 dark:bg-gray-800" role="alert">
            <div class="inline-flex items-center justify-center flex-shrink-0 w-8 h-8 text-green-500 bg-green-100 rounded-lg dark:bg-green-800 dark:text-green-200">
                <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z"/>
                </svg>
                <span class="sr-only">Check icon</span>
            </div>
            <div class="ml-3 text-sm font-normal">{{ toast.message }}</div>
            <!-- <button type="button" class="ml-auto -mx-1.5 -my-1.5 bg-white text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700" data-dismiss-target="#toast-success" aria-label="Close">
                <span class="sr-only">Close</span>
                <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                </svg>
            </button> -->
          </div>

          <div v-if="toast.type === 'error'" id="toast-danger" class="flex items-center w-full max-w-xs p-4 mb-4 text-gray-500 bg-white rounded-lg shadow dark:text-gray-400 dark:bg-gray-800" role="alert">
            <div class="inline-flex items-center justify-center flex-shrink-0 w-8 h-8 text-red-500 bg-red-100 rounded-lg dark:bg-red-800 dark:text-red-200">
                <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 11.793a1 1 0 1 1-1.414 1.414L10 11.414l-2.293 2.293a1 1 0 0 1-1.414-1.414L8.586 10 6.293 7.707a1 1 0 0 1 1.414-1.414L10 8.586l2.293-2.293a1 1 0 0 1 1.414 1.414L11.414 10l2.293 2.293Z"/>
                </svg>
                <span class="sr-only">Error icon</span>
            </div>
            <div class="ml-3 text-sm font-normal">{{ toast.message }}</div>
            <!-- <button type="button" class="ml-auto -mx-1.5 -my-1.5 bg-white text-gray-400 hover:text-gray-900 rounded-lg focus:ring-2 focus:ring-gray-300 p-1.5 hover:bg-gray-100 inline-flex items-center justify-center h-8 w-8 dark:text-gray-500 dark:hover:text-white dark:bg-gray-800 dark:hover:bg-gray-700" data-dismiss-target="#toast-danger" aria-label="Close">
                <span class="sr-only">Close</span>
                <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                </svg>
            </button> -->
          </div>
        </div>
      </transition-group>


    </div>


    <AppHeader :contacts="contacts" />
    <slot />
    <AppFooter :contacts="contacts" />


    <div id="cartmodal" data-modal-backdrop="static" tabindex="-1" aria-hidden="true" class="fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full">
        <div class="relative w-full max-w-2xl max-h-full">
            <!-- Modal content -->
            <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                <!-- Modal header -->
                <div class="flex items-start justify-between p-4 border-b rounded-t dark:border-gray-600">
                    <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                        <!-- {{ shopStore.city }} -->
                    </h3>
                    <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ml-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-hide="cartmodal">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                        </svg>
                        <span class="sr-only">Close modal</span>
                    </button>
                </div>
                <!-- Modal body -->
                <div class="p-6 space-y-6">
                  <transition name="fade">
                    <div v-if="order" class="text-gray-700">
                      <div class="flex items-center justify-center">
                        <p class="">Ваш заказ успешно принят! </p>
                      </div>
                    </div>
                    <div v-else class="w-full">
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
                                    <div class="w-4 h-4 text-gray-500 dark:text-gray-400 mdi mdi-account mb-1.5"></div>
                                  </div>
                                </div>
                                <input v-model="client.name" type="text" id="email-address-icon" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-500 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Иван Иванов">
                              </div>              
                            </div>

                            <div class="">
                              <label for="email-address-icon" class="block mb-2 text-sm font-medium text-gray-500">Как с вами связаться?</label>
                              <div class="relative">
                                <div class="absolute inset-y-0 left-0 flex items-center pl-3.5 pointer-events-none">
                                  <div class="w-4 h-4 text-gray-500 dark:text-gray-400 mdi mdi-contacts mb-1.5"></div>
                                </div>
                                <input v-model="client.contact"  type="text" id="email-address-icon" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-500 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@mail.ru или 89121234567">
                              </div>
                            </div>

                          </div>
                          <p v-if="alert" class="text-semibold text-sm text-red-600">* Заполните все поля</p>
                        </div>


                      </div>
                    </div>
                  </transition>



                
                </div>

                <div class="flex items-center justify-end p-6 space-x-2 border-t border-gray-200 rounded-b dark:border-gray-600">
                  <button v-if="order === false" @click="sendOrder()" type="button" class="text-white bg-gradient-to-br from-sky-700 to-sky-600 font-medium rounded-lg text-sm px-5 py-2.5 text-center transition-all">Отправить</button>                
                </div>
            </div>
        </div>
    </div>







  </div>
</template>