<script setup>
import { initFlowbite } from 'flowbite'



const topLeft = ref('#111827')
const medCenter = ref('#1f2937')
const bottomRight = ref('#374151')

// initialize components based on data attribute selectors
onMounted(() => {
    initFlowbite();
})

</script>


<template>
  <div class="bg-gradient-to-br from-gray-900 via-gray-800 to-gray-700 min-h-screen">
    <AppHeader/>

    <div :class="'container mx-auto max-w-screen-xl ' + `text-[${textColor}]`">

      <div class="my-6">
        <div class="">
          <p>выбор цвета:</p>
        </div>
        <div class="">
          <a href="https://tailwindcss.com/docs/customizing-colors" target="blank" class="text-xs">(примеры)</a>
        </div>

        <div class="grid grid-cols-1 gap-4 my-6">

          <!-- <div class="">
            <p class="text-xs">Цвет текста</p>
            <input type="text" id="person" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-sm focus:ring-blue-500 focus:border-blue-500 block pl-2 py-1 w-[180px]  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Цвет текста">

          </div> -->
          <div class="">
            <p class="text-xs">Цвет градиента фона</p>
            <div class="flex gap-4">
              <input type="text" id="person" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-sm focus:ring-blue-500 focus:border-blue-500 block pl-2 py-1 w-[180px] my-1 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Фон верхий левый">

            </div>
            <div class="flex gap-4">

            </div>
            <input type="text" id="person" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-sm focus:ring-blue-500 focus:border-blue-500 block pl-2 py-1 w-[180px] my-1 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Фон нижний правый">



          </div>


        </div>




      </div>
    </div>

    <slot />
    <AppFooter />
  </div>
</template>