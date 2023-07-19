<script setup>
  const config = useRuntimeConfig()
  const route = useRoute()
  const router = useRouter()

  const { data: products } = await useFetch(`${ config.public.baseURL }s/prods/`)
  const { data: products1 } = await useFetch(`${ config.public.baseURL }s/prods/`)
  const { data: products2 } = await useFetch(`${ config.public.baseURL }s/prods/`)
  const { data: products3 } = await useFetch(`${ config.public.baseURL }s/prods/`)
  const { data: products4 } = await useFetch(`${ config.public.baseURL }s/prods/`)
  const { data: products5 } = await useFetch(`${ config.public.baseURL }s/prods/`)

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
  <div class="">
     <p>product name id</p>
     <p>{{ products }}</p>
  </div>
</template>