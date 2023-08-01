<template>
  <div class="">
    <header>
      <nav class="bg-gray-900/40 border-b border-white/10">
        <div class="flex justify-between items-center mx-auto max-w-screen-xl">
          <div class="py-2">
            <nuxt-link :to="{ name: 'index' }" class="grid grid-cols-1 border-l-4 border-sky-500 px-2">
              <p class="font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-sky-500 to-sky-400 text-[26px] uppercase se lect-none">
                pskovshevron.ru
              </p>
              <p class="text-sm text-gray-300 ">Шевроны в Пскове по вашему дизайну</p>
            </nuxt-link>

          </div>

          <div class="flex gap-6 items-center">
            <div class="">
              <button data-modal-target="staticModal" data-modal-toggle="staticModal" class="text-sm font-semibold uppercase" type="button">
                Корзина
              </button>
            </div>

            <div class="bg-gradient-to-br from-sky-700 to-sky-600 px-6 py-1.5 rounded-3xl">
              <nuxt-link :to="{ name: 'index', hash: '#get-custom-shevron', }" class="text-center text-base font-semibold">Заказать свой дизайн</nuxt-link>
            </div>

          </div>


        </div>
      </nav>
    </header>
  </div>
</template>