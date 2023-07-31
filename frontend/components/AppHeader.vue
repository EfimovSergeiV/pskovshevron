


<template>
  <div class="">
    <header>
      <nav class="bg-gray-900/40">
          <div class="flex justify-between items-center mx-auto max-w-screen-xl">
            <div class="py-2">
              <nuxt-link :to="{ name: 'index' }" class="grid grid-cols-1 border-l-4 border-cyan-700 px-4">
                <p class="font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-cyan-700 to-blue-500 text-[26px] uppercase se lect-none">
                  pskovshevron.ru
                </p>
                <p class="text-sm texs-gray-100">Шевроны во Пскове по вашему дизайну</p>
              </nuxt-link>

            </div>

            <div class="bg-blue-500 px-6 py-2 rounded-3xl">
              <nuxt-link :to="{ name: 'index', hash: '#get-custom-shevron', }" class="text-center text-sm font-semibold">Заказать свой дизайн</nuxt-link>
            </div>

          </div>
      </nav>
    </header>
  </div>
</template>