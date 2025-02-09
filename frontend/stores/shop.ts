interface Product {
  id: number
  product_images: any
  product_properties: any
  title: string
  wildberries: string
  price: number
  description: string
  category: any
  quantity: number
}

interface Toast {
  id: number,
  type: string,
  message: string
}


export const useShopStore = defineStore('ShopStore', {
    state: () => ({
      cart: [] as Product[],
      toasts: [] as Toast[],
      cartmodal: false,
    }),
    getters: {
      productInCart: (state) => (id: number) => {
        return state.cart.find((item) => item.id === id);
      },
    },
    actions: {
      /// Добавление или удаление товара в корзину
      addProduct(payload: Product) {
        const product: Product = { ...payload}
        product.quantity = 1
        const index = this.cart.findIndex((item) => item.id === product.id)
        if (index === -1){
          this.cart.push(product)
        } else {
          this.cart.splice(index, 1)
        }

      },

      clearProducts() {
        this.cart = []
      },

      /// Изменение кол-ва товаров в корзине
      changeQuantity( product: any, action: string ) {
        const cartProduct = this.cart.find((item) => item.id === product.id)
        if ( cartProduct &&  cartProduct.quantity > 1 && action === 'del' ) {
          cartProduct.quantity--
        } else if ( cartProduct && action === 'add') {
          cartProduct.quantity++
        }
      },

      /// Уведомления
      addToast(message: string, type:string) {
        console.log(message, type)
        const mess = {
          "id": this.toasts.length + 1,
          "message": message,
          "type": type
        }
        this.toasts.push(mess)

        setTimeout(() => {
          this.toasts.shift()
        }, 5000)

      },

    },
  })