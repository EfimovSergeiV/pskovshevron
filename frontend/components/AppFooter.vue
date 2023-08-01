<template>
  <div class="">
    <footer class=" bg-gray-900/60 border-t border-white/10">
      <div id="get-custom-shevron" class="mx-auto px-8 max-w-screen-lg text-center">
        
        <div class=" py-8">
          <a href="#" class="flex justify-center items-center text-2xl font-semibold text-gray-500 dark:text-gray-500">
              <p class="">Псков Шеврон</p>
          </a>
          <p class="my-4 text-gray-400 dark:text-gray-400">Не нашли что искали? Мы изготовим шеврон по вашему дизайну. Для этого заполните форму ниже и мы с вами свяжемся!</p>

        </div>
          
        <div class="grid grid-cols-2 items-center gap-8 py-4">

          <div class="">
            <label for="email-address-icon" class="block mb-2 text-sm font-medium text-gray-500">Как вас зовут?</label>
            <div class="relative">
              <div class="absolute inset-y-0 left-0 flex items-center pl-3.5 pointer-events-none">
                <div class="absolute inset-y-0 left-0 flex items-center pl-3.5 pointer-events-none">
                  <div class="w-4 h-4 text-gray-500 dark:text-gray-400 mdi mdi-contacts"></div>
                </div>
              </div>
              <input type="text" id="email-address-icon" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-500 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@flowbite.com">
            </div>              
          </div>

          <div class="">
            <label for="email-address-icon" class="block mb-2 text-sm font-medium text-gray-500">Как с вами связаться?</label>
            <div class="relative">
              <div class="absolute inset-y-0 left-0 flex items-center pl-3.5 pointer-events-none">
                <div class="w-4 h-4 text-gray-500 dark:text-gray-400 mdi mdi-contacts"></div>
              </div>
              <input type="text" id="email-address-icon" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-500 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@flowbite.com">
            </div>
          </div>

        </div>

        <div class="flex items-center justify-center ">
          <div class="my-4 w-2/3">
            <label class="block mb-2 text-sm font-medium text-gray-500" for="user_avatar">Изображение вашего дизайна</label>
            <input class="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" aria-describedby="user_avatar_help" id="user_avatar" type="file">
          </div>
        </div>



        <div class="">
          <button class="bg-gradient-to-br from-sky-700 to-sky-600 px-24 py-2 rounded-3xl font-semibold">Отправить</button>
        </div>
      </div>

      <div class="flex items-center justify-center py-4">
        <p class="text-xs mdi mdi-copyright"> PskovShevron.ru | 2023</p>
      </div>

    </footer>
  </div>
</template>