<script setup>
const config = useRuntimeConfig()
const shopStore = useShopStore()
const props = defineProps(['contacts',])

const client = ref({
  name: null,
  contact: null
})
const file = ref(null)

const onFileChange = (event) => {
  file.value = event.target.files[0]
  console.log(event)
}

const currentData = new Date().getFullYear()

const sendOrder = async () => {
    if ( ( client.value.name ) && ( client.value.contact ) && ( file.value ) ) {
      console.log(file.value)

      const formData = new FormData()
      formData.append("name", client.value.name)
      formData.append("contact", client.value.contact)
      formData.append("image_for_custom", file.value)

      const { data: response } = await useFetch(`${ config.public.baseURL }s/order/`, {
        method: 'POST',
        body: formData        
      });

      shopStore.addToast("Ваш заказ успешно принят!", 'success')
      file.value = null

    } else {
      shopStore.addToast("Заполните контактные данные и прикрипите изображение", 'error')
    }
  }

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: "smooth", })
  }

</script>


<template>
  <div class=" select-none">
    <footer class=" bg-gray-900/60 border-t border-white/10">
      <div id="get-custom-shevron" class="mx-auto px-8 max-w-screen-lg text-center">
        
        <div class=" py-8">
          <div class="flex justify-center items-center text-2xl font-semibold text-gray-500 dark:text-gray-500">
              <button @click="scrollToTop">Псков Шеврон</button>
          </div>

          <p class="my-4 text-gray-400 dark:text-gray-400 select-none">Не нашли что искали? Мы изготовим шеврон по вашему дизайну. Для этого заполните форму ниже и мы с вами свяжемся!</p>

        </div>
          
        <div class="grid grid-cols-1 md:grid-cols-2 items-center gap-8 py-4">

          <div class="">
            <label for="email-address-icon" class="block mb-2 text-sm font-medium text-gray-500 select-none">Как вас зовут?</label>
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
            <label for="email-address-icon" class="block mb-2 text-sm font-medium text-gray-500 select-none">Как с вами связаться?</label>
            <div class="relative">
              <div class="absolute inset-y-0 left-0 flex items-center pl-3.5 pointer-events-none">
                <div class="w-4 h-4 text-gray-500 dark:text-gray-400 mdi mdi-contacts mb-1.5"></div>
              </div>
              <input v-model="client.contact" type="text" id="email-address-icon" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-500 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@mail.ru или 89121234567">
            </div>
          </div>

        </div>

        <div class="flex items-center justify-center ">
          <div class="my-4 w-full md:w-2/3">
            <label class="block mb-2 text-sm font-medium text-gray-500" for="user_avatar">Изображение вашего дизайна</label>
            <input @change="onFileChange" class="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" aria-describedby="user_avatar_help" id="user_avatar" type="file">
          </div>
        </div>



        <div class="my-4">
          <button @click="sendOrder()" class="bg-gradient-to-br from-sky-700 to-sky-600 px-24 py-2 rounded-3xl font-semibold">Отправить</button>
        </div>
      </div>

      <div class="flex items-center justify-center py-4 gap-1">
        <p class="text-xs text-gray-100 mdi mdi-copyright">{{ currentData }} </p>
        <p class="text-xs"> PskovShevron.ru<span class="mx-2">|</span></p>
        <div class="flex justify-center items-center text-xs text-gray-100">
          <a href="mailto:zakaz@pskovshevron.ru">{{ props.contacts.email }}</a>
        </div>
      </div>

    </footer>
  </div>
</template>