# Week 3 — Responsive Shopping Cart (CSS3, Flex & Grid)

**Aim:** Build a responsive web application for a shopping cart with Registration, Login, Catalog and Cart pages using CSS3 features, Flex and Grid.

## Steps

1. **Create the folder layout:**

   ```text
   week3/
   ├── index.html
   ├── login.html
   ├── registration.html
   ├── assets/css/style.css
   └── images/      dress1.jfif, item-2.jpeg, dress3.jfif, cart.jfif, cart-icon.png
   ```

   Put any three product photos and a cart icon in `images/` with those names.
2. **Write the catalog page** [index.html](open:week03-shopping-cart-ui/index.html). It loads Bootstrap 4 from a CDN and has:
   - a dark header and a collapsible navbar (Catalog, Login, Register, Cart)
   - a Bootstrap grid row with three product cards: `col-sm-12 col-md-6 col-xl-4` gives 1, 2 or 3 cards per row depending on screen width
   - each *Add to Cart* button carries `data-name` and `data-price`
3. **Add the cart modal.** The `#cartModal` dialog lists the items in `#cartItems` and the total in `#cartTotal`.
4. **Add the script** at the end of `index.html`:
   - clicking *Add to Cart* pushes `{name, price}` into the `cart` array, calls `updateCart()` and opens the modal
   - `updateCart()` rebuilds the list and the total with `toFixed(2)`
   - *Checkout* shows the order summary, empties the cart and closes the modal
5. **Write the stylesheet** [assets/css/style.css](open:week03-shopping-cart-ui/assets/css/style.css): card image wrap, rating labels, the cart badge, the `.zoom:hover { transform: scale(1.05) }` effect and the toast keyframe animations.
6. **Add the Login and Registration pages** [login.html](open:week03-shopping-cart-ui/login.html) and [registration.html](open:week03-shopping-cart-ui/registration.html). The navbar links to them, but the manual does not print them; these versions centre the card with Flexbox and use CSS Grid for two-column fields.
7. **Test it.** Open `index.html`, add items, open the cart and check out. Compare with [catalog](open:week03-shopping-cart-ui/output/catalog.jpg), [cart](open:week03-shopping-cart-ui/output/cart-modal.jpg) and [checkout summary](open:week03-shopping-cart-ui/output/checkout-summary.jpg).
