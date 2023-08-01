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


export const useShopStore = defineStore('ShopStore', {
    state: () => ({
      cart: [ { "id": 7, "product_images": [ { "id": 7, "image": "http://127.0.0.1:8000/files/product/images/IMG_20230731_001155_edit_146438912129292.webp" } ], "product_properties": [ { "id": 19, "name": "Свойство 1", "value": "Значение 1" }, { "id": 20, "name": "Свойство 2", "value": "Значение 2" }, { "id": 21, "name": "Свойство 3", "value": "Значение 3" } ], "activated": true, "title": "Шеврон 7", "wildberries": null, "price": 160, "description": "<p>Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. Lorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а также реальное распределение букв и пробелов в абзацах, которое не получается при простой дубликации &quot;Здесь ваш текст.. Здесь ваш текст.. Здесь ваш текст..&quot; Многие программы электронной вёрстки и редакторы HTML используют Lorem Ipsum в качестве текста по умолчанию, так что поиск по ключевым словам &quot;lorem ipsum&quot; сразу показывает, как много веб-страниц всё ещё дожидаются своего настоящего рождения.</p>", "last_update": "2023-07-31T10:37:01.125143+03:00", "category": [], "quantity": 1 } ] as Product[],
      city: 'Псков',
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

      /// Изменение кол-ва товаров в корзине
      changeQuantity( product: any, action: string ) {
        const cartProduct = this.cart.find((item) => item.id === product.id)
        if ( cartProduct &&  cartProduct.quantity > 1 && action === 'del' ) {
          cartProduct.quantity--
        } else if ( cartProduct && action === 'add') {
          cartProduct.quantity++
        }
      },
    },
  })