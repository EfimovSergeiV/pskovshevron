export const useShopStore = defineStore('ShopStore', {
    state: () => ({
      shop: null,
      shops: [],
      city: 'Псков',
    }),
    // actions: {
    //   selectShop(shop: any) {
    //     this.shop = shop
    //   },
    //   selectCityMaps(city: any) {
    //     this.city = city
    //   },
    //   writeShops(shops: any) {
    //     this.shops = shops
    //     this.shop = shops.value[0]
    //   },
    //   async sendCoordinates(coordinates: any) {
    //     const config = useRuntimeConfig()
    //     const { data }: any = await useFetch(`${ config.public.baseURL }coordinates/`, {
    //       method: 'POST',
    //       body: coordinates
    //     });
    //     if (data.value) {
    //       this.city = data.value.at(-1)
    //       this.shops.forEach((el: any) => {
    //         if (el.city.toLowerCase() === this.city.toLowerCase()) {
    //           this.shop = el
    //         }
    //       })
    //     }
    //   }
    // },
  })