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
  <div class="bg-gradient-to-br from-gray-900 via-gray-800 to-gray-700 min-h-screen text-gray-100">
    <AppHeader/>
    <slot />
    <AppFooter />
  </div>
</template>