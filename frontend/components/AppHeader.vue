<script setup>
  const shopStore = useShopStore()
  const scrollToButtom = () => {
    window.scrollTo({ top: 800000, behavior: "smooth", })
  }
</script>

<template>
  <div class="">
    <header>
      <nav class="bg-gray-900/40 border-b border-white/10 py-4 md:py-2">
        <div class="grid grid-cols-1 gap-4 md:flex md:justify-between items-center mx-auto px-8 max-w-screen-xl">
          <div class="py-2">
            <nuxt-link :to="{ name: 'index' }" class="grid grid-cols-1 border-l-4 border-sky-500 px-2">
              <p class="font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-sky-500 to-sky-400 text-[26px] uppercase select-none">
                pskovshevron.ru
              </p>
              <p class="text-sm text-gray-300 select-none">Шевроны в Пскове по вашему дизайну</p>
            </nuxt-link>

          </div>

          <div class="flex gap-6 items-center justify-end">
            <div class="">
              <button data-modal-target="cartmodal" data-modal-toggle="cartmodal" class="text-sm font-semibold uppercase select-none" type="button">
                Корзина ({{ shopStore.cart.length }})
              </button>
            </div>

            <button @click="scrollToButtom()" class="bg-gradient-to-br from-sky-700 to-sky-600 px-6 py-1.5 rounded-3xl">
              <p class="text-center text-base font-semibold select-none">Заказать свой дизайн</p>
            </button>

          </div>


        </div>
      </nav>
    </header>
  </div>
</template>