<script setup>
  const shopStore = useShopStore()
  const props = defineProps(['contacts',])

  const scrollToButtom = () => {
    window.scrollTo({ top: 800000, behavior: "smooth", })
  }
</script>

<template>
  <div class="">
    <header>
      <nav class="bg-gray-900/40 border-b border-white/10 py-4 md:py-2">
        <div class="grid grid-cols-1 gap-4 md:flex md:justify-between items-center mx-auto px-8 max-w-screen-xl">
          
          <div class="py-2 flex justify-center md:justify-start">
            <nuxt-link :to="{ name: 'index' }" class="grid grid-cols-1 md:border-l-4 md:border-sky-500 px-2">
              <p class="font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-sky-500 to-sky-400 text-[26px] uppercase select-none">
                pskovshevron.ru
              </p>
              <p class="text-sm text-gray-300 select-none">Шевроны в Пскове по вашему дизайну</p>
            </nuxt-link>
          </div>



          <div class="grid grid-cols-1 gap-2">
            <div class="flex gap-4 items-center justify-end">
              <div class="">
                <button data-modal-target="cartmodal" data-modal-toggle="cartmodal" class="text-sm font-semibold uppercase select-none" type="button">
                  Корзина
                </button>
              </div>

              <button @click="scrollToButtom()" class="bg-gradient-to-br from-sky-700 to-sky-600 px-6 py-1.5 rounded-3xl">
                <p class="text-center text-base font-semibold select-none">Заказать свой дизайн</p>
              </button>
            </div>

            <div class="">
              <div class="flex items-center justify-end gap-2">
                
                <a v-if="props.contacts.email" :href="`mailto:${props.contacts.email}`" target="_blank" class="bg-gradient-to-br from-sky-700 to-sky-600 rounded-3xl px-4 py-1.5">
                  <p class="text-center font-semibold">
                    {{ props.contacts.email }}
                  </p>
                </a>
                <a v-if="props.contacts.phone" :href="`tel:${props.contacts.phone.replace(/[()\-\s]/g, '')}`" target="_blank" class="bg-gradient-to-br from-sky-700 to-sky-600 rounded-3xl px-4 py-1.5">
                  <p class="text-center font-semibold">
                    {{ props.contacts.phone }}
                  </p>
                </a>

                <a v-if="props.contacts.wa" :href="`https://wa.me/${props.contacts.wa.replace(/[+\-\s()]/g, '')}`" target="_blank" class="bg-gradient-to-br from-sky-700 to-sky-600 rounded-3xl px-1.5">
                  <p class="text-center font-semibold mdi mdi-whatsapp mdi-24px"></p>
                </a>

                <a v-if="props.contacts.tg" :href="`https://t.me/${props.contacts.tg}`" target="_blank" class="bg-gradient-to-br from-sky-700 to-sky-600 rounded-3xl p-1.5">
                  <img src="/tg.png" class="h-[24px]" />
                </a>

              </div>
            </div>
          </div>



        </div>
      </nav>
    </header>
  </div>
</template>