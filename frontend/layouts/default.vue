<script setup>
import { initFlowbite } from 'flowbite'

// initialize components based on data attribute selectors
onMounted(() => {
    initFlowbite();
})

</script>


<template>
  <div class="">
    <AppHeader/>
    <slot />
    <AppFooter />
  </div>
</template>