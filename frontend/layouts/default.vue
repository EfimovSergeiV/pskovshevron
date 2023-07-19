<script setup>
import { initFlowbite } from 'flowbite'

// initialize components based on data attribute selectors
onMounted(() => {
    initFlowbite();
})

</script>


<template>
  <div class="bg-gradient-to-br from-gray-900 via-gray-800 to-gray-700 min-h-screen">
    <AppHeader/>
    <slot />
    <AppFooter />
  </div>
</template>