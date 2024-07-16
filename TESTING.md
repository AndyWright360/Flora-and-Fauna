# **Flora & Fauna - Testing** <!-- omit in toc -->

![Flora & Fauna logo](media/docs/brand-logo.jpg)

## **Introduction** <!-- omit in toc -->

Welcome to the testing documentation for the Flora & Fauna e-commerce website. This document outlines the testing strategy and practices used to ensure the quality and reliability of the application.

The types of tests performed include automated testing using Django's built-in test suite. Code validation to ensure that the HTML, CSS, JavaScript, and Python code adhere to best practices and standards. Colour contrast checks to verify that the text is easily readable and meets accessibility standards. Additionally, site performance is assessed using Lighthouse testing, and thorough manual tests are conducted to identify and rectify any issues.

The goal of this approach is to deliver the highest quality website achievable within my capabilities.

[The full README is available here.](README.md)

![Flora & Fauna displayed on miltiple devices](media/docs/responsive-site.jpg)

[Click here to visit Flora & Fauna](https://flora-and-fauna-c279c1bad929.herokuapp.com/)

**By [Andrew Wright](https://github.com/AndyWright360)**

---

## **Contents** <!-- omit in toc --> 

- [**Automated Testing**](#automated-testing)
  - [**Django Testing**](#django-testing)
  - [**Code Validation**](#code-validation)
    - [**W3C HTML Validation**](#w3c-html-validation)
    - [**W3C CSS Validation**](#w3c-css-validation)
    - [**JSHint JavaScript Validation**](#jshint-javascript-validation)
    - [**Python Validation**](#python-validation)
  - [**WCAG Colour Contrast Checker**](#wcag-colour-contrast-checker)
  - [**Lighthouse Testing**](#lighthouse-testing)
- [**Manual Testing**](#manual-testing)
  - [**Testing User Stories**](#testing-user-stories)
  - [**Full Testing**](#full-testing)
  - [**Bugs & Fixes**](#bugs--fixes)
  - [**Known Bugs**](#known-bugs)

---

## **Automated Testing**

### **Django Testing**

This project marked my first experience with automated testing. As a beginner, I kept the tests straightforward to better understand this approach. I achieved 83% coverage across all apps, which I was pleased with given my experience level. The remaining testing was conducted manually.

I aimed to follow a test-driven development (TDD) approach, writing automated tests or manually checking the site functionality after adding new features. This experience highlighted the benefits of automated testing and improved my understanding of the process.

**Django Test Results**

![Total test results](media/docs/test-results.jpg)

**Total Test Coverage Results**

![Total test coverage results](media/docs/coverage-total.jpg)

**Test Coverage Results Per App**

<details><summary>Home App</summary>

<img src="media/docs/coverage-home.jpg">

</details>

<details><summary>Products App</summary>

<img src="media/docs/coverage-products.jpg">

</details>

<details><summary>Bag App</summary>

<img src="media/docs/coverage-bag.jpg">

</details>

<details><summary>Checkout App</summary>

<img src="media/docs/coverage-checkout.jpg">

</details>

<details><summary>Profiles App</summary>

<img src="media/docs/coverage-profiles.jpg">

</details>

<details><summary>Reviews App</summary>

<img src="media/docs/coverage-reviews.jpg">

</details>

<details><summary>Wishlist App</summary>

<img src="media/docs/coverage-wishlist.jpg">

</details>

---

#### **W3C HTML Validation**

[W3C](https://validator.w3.org/) was used to validate the HTML code.

| Page | Results |
| :--- | :--- |
| index.html | ![HTML Validation Result](media/docs/html-validation-index.jpg) |
| products.html | ![HTML Validation Result](media/docs/html-validation-products.jpg) |
| product_detail.html | ![HTML Validation Result](media/docs/html-validation-product-detail.jpg) |
| bag.html | ![HTML Validation Result](media/docs/html-validation-bag.jpg) |
| checkout.html | ![HTML Validation Result](media/docs/html-validation-checkout.jpg) |
| checkout_success.html | ![HTML Validation Result](media/docs/html-validation-checkout-success.jpg) |
| profile.html | ![HTML Validation Result](media/docs/html-validation-profile.jpg) |
| add_review.html | ![HTML Validation Result](media/docs/html-validation-add-review.jpg) |
| edit_review.html | ![HTML Validation Result](media/docs/html-validation-edit-review.jpg) |
| add_product.html | ![HTML Validation Result](media/docs/html-validation-add-product.jpg) |
| edit_product.html | ![HTML Validation Result](media/docs/html-validation-edit-product.jpg) |
| signup.html | ![HTML Validation Result](media/docs/html-validation-signup.jpg) |
| login.html | ![HTML Validation Result](media/docs/html-validation-login.jpg) |
| logout.html | ![HTML Validation Result](media/docs/html-validation-logout.jpg) |

I encountered several warnings while validating my HTML. These included missing `alt` tags for images, `<p>` elements nested within `<span>` elements, and duplicate `id` tags within the same document. Additionally, there were a few other minor issues that needed correction. Once these problems were addressed, all pages passed validation without any issues.

#### **W3C CSS Validation**

[W3C](https://jigsaw.w3.org/css-validator/) was used to validate the CSS code.

| Page | Results |
| :--- | :--- |
| base.css | ![CSS Validation Result](media/docs/css-results.jpg) |
| checkout.css | ![CSS Validation Result](media/docs/css-results.jpg) |

![CSS validation warning](media/docs/css-warnings.jpg)

The following warnings were flagged, all related to the use of vendor extensions, which I opted to disregard. I also replaced the deprecated `clip` property with the more commonly used `clip-path`.

#### **JSHint JavaScript Validation**

[JSHint](https://jshint.com/) was used to validate the JavaScript code.

| Page | Results |
| :--- | :--- |
| Quantity Input Script | ![JavaScript Validation Result](media/docs/js-validation-qty-input.jpg) |
| Update Bag Script | ![JavaScript Validation Result](media/docs/js-validation-update-bag.jpg) |
| New Image Script | ![JavaScript Validation Result](media/docs/js-validation-new-image.jpg) |
| Return To Top Button Script | ![JavaScript Validation Result](media/docs/js-validation-return-to-top-btn.jpg) |
| Wishlist Toast Script | ![JavaScript Validation Result](media/docs/js-validation-wishlist-toast.jpg) |
| Add/Remove Wishlist Item Script | ![JavaScript Validation Result](media/docs/js-validation-add-remove-wishlist.jpg) |
| Product Rage Tooltip Script | ![JavaScript Validation Result](media/docs/js-validation-tooltip.jpg) |
| Product Sort Script | ![JavaScript Validation Result](media/docs/js-validation-product-sorting.jpg) |
| Profile Form Update Script | ![JavaScript Validation Result](media/docs/js-validation-profile-form.jpg) |
| Product Review Rating Script | ![JavaScript Validation Result](media/docs/js-validation-rating.jpg) |
| stripe_elements.js | ![JavaScript Validation Result](media/docs/js-validation-stripe-elements.jpg) |

The only warnings found during JavaScript linting were missing semi-colons. After addressing these, all scripts passed without any issues

#### **Python Validation**

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code.

<details><summary>Main Directory</summary>

| Page | Results |
| :--- | :--- |
| `Main` |
| custom_storages.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| manage.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |

</details>

<details><summary>Project Directory</summary>

| Page | Results |
| :--- | :--- |
| `Flora_and_Fauna` |
| asgi.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| sttings.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| urls.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| wsgi.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |

</details>

<details><summary>Home App Directory</summary>

| Page | Results |
| :--- | :--- |
| `Home` |
| apps.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| test_views.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| urls.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| views.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |

</details>

<details><summary>Products App Directory</summary>

| Page | Results |
| :--- | :--- |
| `Products` |
| admin.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| apps.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| forms.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| models.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| test_forms.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| test_models.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| test_views.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| urls.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| views.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| widgets.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |

</details>

<details><summary>Bag App Directory</summary>

| Page | Results |
| :--- | :--- |
| `Bag` |
| bag_tools.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| apps.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| contexts.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| test_views.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| urls.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| views.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |

</details>

<details><summary>Checkout App Directory</summary>

| Page | Results |
| :--- | :--- |
| `Checkout` |
| admin.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| apps.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| forms.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| models.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| signals.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| test_forms.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| test_models.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| test_views.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| urls.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| views.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| webhook_handler.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| webhooks.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |

</details>

<details><summary>Profiles App Directory</summary>

| Page | Results |
| :--- | :--- |
| `Profiles` |
| apps.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| forms.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| models.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| test_forms.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| test_models.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| test_views.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| urls.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| views.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |

</details>

<details><summary>Reviews App Directory</summary>

| Page | Results |
| :--- | :--- |
| `Reviews` |
| admin.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| apps.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| forms.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| models.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| test_forms.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| test_models.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| test_views.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| urls.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| views.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |

</details>

<details><summary>Wishlist App Directory</summary>

| Page | Results |
| :--- | :--- |
| `Wishlist` |
| admin.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| apps.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| models.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| test_models.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| test_views.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| urls.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |
| views.py | ![Python Validation Result](media/docs/python-validation-results.jpg) |

</details>

<br>
I needed to make several adjustments to align my code with PEP8 standards. These changes mainly involved reformatting, such as shortening line lengths and eliminating excess white space. Once these modifications were applied, all pages passed without error.

---

### **WCAG Colour Contrast Checker**

A significant effort was made to create a strong contrast in the website's colour scheme. When selecting the primary colours for the site, I ensured that the complementary colours used for the text would also maintain clarity to enhance the user experience.

**Navbar**

![Colour contrast results](media/docs/contrast-navbar.jpg)

The chosen colour scheme serves as the primary theme for the navbar. A high contrast was selected to ensure users have maximum clarity when navigating the site and utilising the various product filtering features.

**Buttons**

![Colour contrast results](media/docs/contrast-green-btn.jpg)
![Colour contrast results](media/docs/contrast-blue-btn.jpg)
![Colour contrast results](media/docs/contrast-red-btn.jpg)

The green contrast acts as one of the primary button colours for the site and as the main colour scheme throughout. The blue colour scheme serves as an alternative styling option, while the red button is used specifically for delete options in user reviews and modals.

**Input Fields**

![Colour contrast results](media/docs/contrast-input.jpg)

The colour scheme for input fields was chosen for its high contrast to ensure readability and clarity when users input details on the site.

**Product Range Links**

![Colour contrast results](media/docs/contrast-aloe.jpg)
![Colour contrast results](media/docs/contrast-honey.jpg)
![Colour contrast results](media/docs/contrast-rose.jpg)
![Colour contrast results](media/docs/contrast-willow.jpg)

Each product range is represented by a colour associated with its key ingredient. I ensured the contrast was high enough to be legible while effectively communicating the desired colour scheme.

**Footer**

![Colour contrast results](media/docs/contrast-footer.jpg)

The footer's colour scheme was selected to be distinct while maintaining consistency with the rest of the site. Similar to the navbar, a high contrast was prioritised to ensure it stands out clearly.

---

### **Lighthouse Testing**

Lighthouse within Chrome Developer Tools was used to assess the website's performance, accessibility, adherence to best practices, and SEO.

| Page | Desktop Results | Mobile Results |
| :--- | :--- | :--- |
| index.html | ![Lighthouse desktop results](media/docs/lighthouse-home-dt.jpg) | ![Lighthouse mobile results](media/docs/lighthouse-home-mob.jpg) |
| products.html | ![Lighthouse desktop results](media/docs/lighthouse-products-dt.jpg) | ![Lighthouse mobile results](media/docs/lighthouse-products-mob.jpg) |
| product_detail.html | ![Lighthouse desktop results](media/docs/lighthouse-product-detail-dt.jpg) | ![Lighthouse mobile results](media/docs/lighthouse-product-detail-mob.jpg) |
| bag.html | ![Lighthouse desktop results](media/docs/lighthouse-bag-dt.jpg) | ![Lighthouse mobile results](media/docs/lighthouse-bag-mob.jpg) |
| checkout.html | ![Lighthouse desktop results](media/docs/lighthouse-checkout-dt.jpg) | ![Lighthouse mobile results](media/docs/lighthouse-checkout-mob.jpg) |
| checkout_success.html | ![Lighthouse desktop results](media/docs/lighthouse-checkout-success-dt.jpg) | ![Lighthouse mobile results](media/docs/lighthouse-checkout-success-mob.jpg) |
| profile.html | ![Lighthouse desktop results](media/docs/lighthouse-profile-dt.jpg) | ![Lighthouse mobile results](media/docs/lighthouse-profile-mob.jpg) |
| add_review.html | ![Lighthouse desktop results](media/docs/lighthouse-add-review-dt.jpg) | ![Lighthouse mobile results](media/docs/lighthouse-add-review-mob.jpg) |
| edit_review.html | ![Lighthouse desktop results](media/docs/lighthouse-edit-review-dt.jpg) | ![Lighthouse mobile results](media/docs/lighthouse-edit-review-mob.jpg) |
| add_product.html | ![Lighthouse desktop results](media/docs/lighthouse-add-product-dt.jpg) | ![Lighthouse mobile results](media/docs/lighthouse-add-product-mob.jpg) |
| edit_product.html | ![Lighthouse desktop results](media/docs/lighthouse-edit-product-dt.jpg) | ![Lighthouse mobile results](media/docs/lighthouse-edit-product-mob.jpg) |
| signup.html | ![Lighthouse desktop results](media/docs/lighthouse-signup-dt.jpg) | ![Lighthouse mobile results](media/docs/lighthouse-signup-mob.jpg) |
| login.html | ![Lighthouse desktop results](media/docs/lighthouse-login-dt.jpg) | ![Lighthouse mobile results](media/docs/lighthouse-login-mob.jpg) |
| logout.html | ![Lighthouse desktop results](media/docs/lighthouse-logout-dt.jpg) | ![Lighthouse mobile results](media/docs/lighthouse-logout-mob.jpg) |

---

## **Manual Testing**

### **Testing User Stories**

**Site User**

| Goals | How are they achieved? | Images |
| :--- | :--- | :--- |
| I want to understand the purpose of the site immediately upon entering. | The landing page of the website was designed to immediately convey to users that this is a skincare e-commerce site. This is achieved primarily through the use of a hero image that visually represents the brand. Additionally, a brief introduction clearly outlines the website's purpose and entices users to explore the product range | ![User story results](media/docs/stories-home-page.jpg) |
| I want to be able to navigate the site easily and intuitively. | The primary form of navigation is the navbar, which not only facilitates site navigation but also allows users to search and sort products. By keeping the navbar fixed at the top of the page, users always have quick access to these options. Additionally, various navigation options are available through the use of buttons, offering an extra layer of convenient and informative links throughout the site. | ![User story results](media/docs/stories-navbar.jpg) ![User story results](media/docs/stories-nav-buttons.jpg) |
| I want to use all features on the site on any device. | Each page of the website has been thoroughly tested to ensure a responsive layout across various screen sizes. A maximum width of 1600px is applied to the body to maintain visual consistency on wider screens, and the design adapts seamlessly down to 320px. This ensures the website remains visually appealing and functional across a wide range of devices. | ![User story results](media/docs/stories-wide-layout.jpg) ![User story results](media/docs/stories-narrow-layout.jpg) |
| I want to receive feedback when interacting with the site to know if my actions have been successful. | Toast messages are utilised to provide users with feedback when they interact with the site. Success messages confirm actions such as adding a product to the bag. Error messages notify users of any invalid input information. Additionally, info messages offer details, such as indicating which product is currently being edited. | ![User story results](media/docs/stories-messages.jpg) |

**Shopper**

| Goals | How are they achieved? | Images |
| :--- | :--- | :--- |
| I want to browse products easily, with options to filter and search to find what I need. | The navbar includes a search bar that displays products whose names or descriptions match the search term provided. Displayed products can also be sorted using the options within the navbar or by selecting a sorting option from the dropdown menu on the products page. | ![User story results](media/docs/stories-search.jpg) |
| I want to find detailed information about products. | Each product on the products page features a `VIEW` button. Clicking this button takes users to the product detail page, where they can access additional information about the product. This includes the product description, a list of ingredients, and any submitted reviews from other users. | ![User story results](media/docs/stories-details.jpg) |
| I want to see ratings and reviews of a product to know more about its quality and suitability for me. | Users with an account can submit reviews for products. Each review includes a title, a message, and a star rating out of five. The product shows an average rating calculated from all submitted reviews. This feature helps users make more informed purchasing decisions by providing valuable customer feedback. | ![User story results](media/docs/stories-reviews.jpg) |
| I want to be able to add multiple products and quantities to my shopping bag. | On the product detail page, users can specify the quantity of a product they wish to add to their bag using the quantity input field. The bag can hold multiple different products, allowing users to select and add a variety of items according to their preferences. | ![User story results](media/docs/stories-quantity.jpg) |
| I want to edit my shopping bag if I change my mind. | The shopping bag page enables users to adjust the quantity of items or remove them from their bag. Each item features `Update` and `Remove` buttons for these actions. | ![User story results](media/docs/stories-update-bag.jpg) |
| I want to know what I will be charged for delivery. | Each time a user adds an item to their bag, a message displays the additional amount needed to qualify for free delivery. The bag page provides a detailed breakdown of the order cost, including the `Bag Total`, `Delivery Cost`, and `Grand Total`. This ensures the user is fully aware of the cost before proceeding to checkout.  | ![User story results](media/docs/stories-order-total.jpg) |
| I want the option to purchase products without creating an account. | Users can purchase products without creating an account. However, creating an account offers additional features, such as a profile page to save contact details, the ability to submit product reviews, and the option to add products to a Wishlist. | ![User story results](media/docs/stories-checkout.jpg) |

**Account Holder**

| Goals | How are they achieved? | Images |
| :--- | :--- | :--- |
| I want my account to be secure and easy to set up. | User account creation and security are managed by the Allauth package. This provides users with a robust and secure account system that is feature-rich and far more secure than any system I could create independently. | ![User story results](media/docs/stories-signup.jpg) |
| I want to see my order history. | From their profile page, users can view a list of their previous orders. Each order number acts as a link that directs the user to a summary of the order, including the products ordered, delivery information, and total cost. | ![User story results](media/docs/stories-order-history.jpg) |
| I want to update and save my personal information. | The form on the profile page allows users to update and save their delivery information. This information will prepopulate the checkout form during their next purchase, ensuring a faster and more convenient checkout process. | ![User story results](media/docs/stories-user-details.jpg) |
| I want to leave reviews of products. | After creating an account, users can submit product reviews from the product details page. This allows them to share feedback and opinions about the product with other users. | ![User story results](media/docs/stories-add-review.jpg) |
| I want to edit and delete my reviews. | A list of the user’s submitted reviews is displayed on their profile page. From there, the user can also edit or delete a review. | ![User story results](media/docs/stories-update-review.jpg) |
| I want to add and remove products from my Wishlist. | For logged-in users, each product card contains a Wishlist button. This provides a quick and convenient way to add any product to their Wishlist. A notification is displayed on screen to inform the user if a product has been added to or removed from their Wishlist. The button icon also changes to a solid heart as a visual reminder of which products are currently in their Wishlist. The products in the user’s Wishlist are displayed on their profile page. | ![User story results](media/docs/stories-wishlist.jpg) |

**Administrator**

| Goals | How are they achieved? | Images |
| :--- | :--- | :--- |
| I want to add and edit products. | As an administrator, you have special privileges related to product management. From the user icon in the navbar, you can access the `Product Management` page, where you can add new products to the site. Additionally, each product listing includes `Edit` and `Delete` buttons. These buttons enable you to modify product details or remove products entirely. | ![User story results](media/docs/stories-add-product.jpg) |
| I want to remove products. | When an administrator selects the Delete button for a product, they are prompted to confirm the deletion. This extra confirmation step adds an additional layer of security, helping to prevent accidental deletions. Once confirmed, all details of the selected product are permanently removed from the database. | ![User story results](media/docs/stories-delete-product.jpg) |
| I want all admin controls to be simple to find and use. | Each product features `Edit` and `Delete` buttons for straightforward management. The option to add a product is accessible via the user icon in the fixed navbar, ensuring it's conveniently available from any page on the site. | ![User story results](media/docs/stories-admin-features.jpg) |

---

### **Full Testing**

Full testing was performed on the following devices:

- Laptop:
  - MSI Thin GF63 15-inch screen
- Mobile Device:
  - iPhone XR

The following browsers were tested using each device:

- Laptop:
  - Google Chrome
  - Mozilla Firefox
- Mobile:
  - Safari

Friends and family also tested the website using a variety of devices. No issues were reported.

| Feature | Expected Outcome | Testing Performed | Pass/Fail |
| :--- | :--- | :--- | :--- |
| `Navbar` |
| Max Width | Reaches maximum width at 1600px | View page using Chrome DevTools and expand width beyond 1600px |  |
| Min Width | All elements can be reduced to a screen width of 320px without distortion | View page using Chrome DevTools and reduce width to 320px |  |
| Logo Link | Clicking the logo navigates to the Home page | Click the logo |  |
| Hover Effect | Navigation links and icons become bold when hovered over with mouse | Hover over the navigation links and icons |  |
| Navigation Menus | Clicking the navigation links and `Account` icon opens the link options | Click each navigation link and the `Account` icon |  |
| Navigation Menu Hover Effect | Hovering over a navigation link in the dropdown menu highlights the option | Open each navigation dropdown menu and hover over each option |  |
| Search Bar Focus | When focusing within the search bar, the border triggers its focus state | Click inside the search bar input |  |
| Search Icon Hover Effect | Hovering over the search bar button icon triggers its hover state | Hover the mouse over the search bar button icon |  |
| Bag Total | The Bag icon displays the current bag total value | Add and remove products from the bag and check the displayed value is correct |  |
| Navigation Links | Each navigation link loads the expected page when clicked | Click each navigation link to check the relevant page is loaded |  |
| Search 'Empty Input' | A toast message notifies the user that no search criteria were entered | Click the search button with an empty input |  |
| Search 'No Results' | No products are displayed | Search for a keyword not found in any product |  |
| Search 'Results' | Only products relating to the search term are displayed | Search for a keyword that matches some products |  |
| Side Nav Expands | When the side nav button is displayed, clicking it reveals the navigation options | Click the side nav button |  |
| Fixed Navbar | When scrolling down the page, the navbar remains fixed to the top of the screen | Scroll down the page |  |
| `Footer` |
| Max Width | Reaches maximum width at 1600px | View page using Chrome DevTools and expand width beyond 1600px |  |
| Min Width | All elements can be reduced to a screen width of 320px without distortion | View page using Chrome DevTools and reduce width to 320px |  |
| Hover Effect | Icons change colour when hovered over with mouse | Hover over the footer icons |  |
| Navigation Links | Clicking the footer icons opens the relevant link in a new window | Click each footer icon |  |
| `Home Page` |
| Max Width | Reaches maximum width at 1600px | View page using Chrome DevTools and expand width beyond 1600px |  |
| Min Width | All elements can be reduced to a screen width of 320px without distortion | View page using Chrome DevTools and reduce width to 320px |  |
| Hover Effect | 'Explore Our Garden!' link becomes bold when hovered over with mouse | Hover over the navigation link |  |
| Navigation Link | Clicking the 'Explore Our Garden!' link navigates to the products page | Click the navigation link |  |
| `Products Page` |
| Max Width | Reaches maximum width at 1600px | View page using Chrome DevTools and expand width beyond 1600px |  |
| Min Width | All elements can be reduced to a screen width of 320px without distortion | View page using Chrome DevTools and reduce width to 320px |  |
| Hover Effects | Hovering over buttons and navigation links triggers their hover state | Hover over buttons and navigation links |  |
| Back To Top Button | Clicking the back to top button takes the user back to the top of the page | Scroll to the bottom of the page and click the button |  |
| Range Link Tooltip | The tooltip message is displayed when hovering over product range links | Hover over product range links |  |
| Range Link Navigation | Clicking the product range link displays all products from the range | Click each unique product range link option |  |
| Add Product Button | Clicking the `ADD` button for a product adds a quantity of 1 to the bag | Click the `ADD` product button |  |
| Update Bag Toast | Adding a product to the bag displays a confirmation toast message along with the current products in the bag | Add a product to the bag |  |
| View Product Button | Clicking the `VIEW` button navigates to the product detail page for the corresponding product | Click the `VIEW` product button |  |
| Product Sorting | Selecting an option from the product sort dropdown menu orders the displayed products according to the selection | Select each option from the product sorting dropdown menu |  |
| Wishlist Button Displayed | The Wishlist button is only displayed for users that have created an account | View the page while signed out and again while signed in |  |
| Wishlist Toast | A toast message is displayed when a product is added or removed from the Wishlist | Click the Wishlist button to add and remove a product |  |
| Wishlist Button Display Change | When adding a product to the Wishlist, the button icon changes to a solid heart | Click the Wishlist button to add and remove a product |  |
| Admin Features | The options to edit and delete products are only displayed for admin users | View the page while signed out and again while signed in as an admin |  |
| Edit Product | Clicking the `Edit` button on a product navigates to the edit product page | Click the `Edit` button for a product |  |
| Delete Modal | Clicking the `Delete` button for a product triggers the delete modal | Click the `Delete` button for a product |  |
| Delete Modal 'Cancel' | Clicking the `NO` button in the delete modal cancels the deletion | Click the `NO` button in the delete modal |  |
| Delete Modal 'Confirm' | Clicking the `YES` button in the delete modal deletes the product | Click the `YES` button in the delete modal |  |
| `Product Detail Page` |
| Max Width | Reaches maximum width at 1600px | View page using Chrome DevTools and expand width beyond 1600px |  |
| Min Width | All elements can be reduced to a screen width of 320px without distortion | View page using Chrome DevTools and reduce width to 320px |  |
| Hover Effects | Hovering over buttons and navigation links triggers their hover state | Hover over buttons and navigation links |  |
| Back To Top Button | Clicking the back to top button takes the user back to the top of the page | Scroll to the bottom of the page and click the button |  |
| Range Link Navigation | Clicking the product range link navigates to the products page and displays all products in that range | Click the product range link |  |
| Keep Shopping | Clicking the `KEEP SHOPPING` button navigates to the products page | Click the `KEEP SHOPPING` button |  |
| Wishlist Button Displayed | The Wishlist button is only displayed for users that have created an account | View the page while signed out and again while signed in |  |
| Wishlist Toast | A toast message is displayed when a product is added or removed from the Wishlist | Click the Wishlist button to add and remove a product |  |
| Wishlist Button Display Change | When adding a product to the Wishlist, the button icon changes to a solid heart | Click the Wishlist button to add and remove a product |  |
| Quantity Decrement Button 'Disable' | The quantity decrement button disables when the input value reaches 1 | Reduce quantity input value to 1 |  |
| Quantity Increment Button 'Disable' | The quantity increment button disables when the input value reaches 99 | Increase quantity input value to 99 |  |
| Quantity Input 'Required' | The quantity input does not allow users to submit without a value | Remove the quantity input value and attempt to submit the form |  |
| Quantity Input 'Min/Max Value' | The quantity input does not allow users to submit with a value outside the range of 1-99 | Attempt to submit the form with a value less than 1 or greater than 99 |  |
| Add To Bag Button | Adding a valid quantity to the bag triggers a toast message to confirm the action and display the bag | Add a valid quantity of the product to the bag |  |
| Add Review Button Displayed | The `ADD REVIEW` button is only displayed for users that have created an account | View the page while signed out and again while signed in |  |
| Add Review Navigation | Clicking the `ADD REVIEW` button navigates the user to the add review page for the product | Click the `ADD REVIEW` button |  |
| Product Range Carousel | Clicking the carousel arrow buttons scrolls through the other range of products from the same range | Click the arrow button in the other products carousel |  |
| Add Other Product | Clicking the `ADD` button for a product displayed in the other products from this range section adds a quantity of 1 for that product | Click the `ADD` button for another product in the range |  |
| View Other Product | Clicking the `VIEW` button for a product displayed in the other products from this range section navigates to that product's detail page | Click the `VIEW` button for another product in the range |  |
| `Bag Page` |
| Max Width | Reaches maximum width at 1600px | View page using Chrome DevTools and expand width beyond 1600px |  |
| Min Width | All elements can be reduced to a screen width of 320px without distortion | View page using Chrome DevTools and reduce width to 320px |  |
| Hover Effects | Hovering over buttons and navigation links triggers their hover state | Hover over buttons and navigation links |  |
| Back To Top Button | Clicking the back to top button takes the user back to the top of the page | Scroll to the bottom of the page and click the button |  |
| Product Links | Clicking the product title or image navigates to the product detail page | Click each product title and image |  |
| Quantity Decrement Button 'Disable' | The quantity decrement button disables when the input value reaches 1 | Reduce quantity input value to 1 |  |
| Quantity Increment Button 'Disable' | The quantity increment button disables when the input value reaches 99 | Increase quantity input value to 99 |  |
| Quantity Input 'Required' | The quantity input does not allow users to submit without a value | Remove the quantity input value and attempt to submit the form |  |
| Quantity Input 'Min/Max Value' | The quantity input does not allow users to submit with a value outside the range of 1-99 | Attempt to submit the form with a value less than 1 or greater than 99 |  |
| Update Button | Clicking the `UPDATE` button updates the bag total to reflect the input quantity | Add/remove a quantity and click the `UPDATE` button |  |
| Update Toast | Updating the bag displays a confirmation toast message and the updated total | Add/remove a quantity and click the `UPDATE` button |  |
| Remove Product | Clicking the `REMOVE` button removes the product from the bag | Click the `REMOVE` button for a product in the bag |  |
| Checkout Button | Clicking the `CHECKOUT` button navigates to the checkout page | Click the `CHECKOUT` button |  |
| `Wishlist Page` |
| Max Width | Reaches maximum width at 1600px | View page using Chrome DevTools and expand width beyond 1600px |  |
| Min Width | All elements can be reduced to a screen width of 320px without distortion | View page using Chrome DevTools and reduce width to 320px |  |
| Hover Effects | Hovering over buttons and navigation links triggers their hover state | Hover over buttons and navigation links |  |
| Back To Top Button | Clicking the back to top button takes the user back to the top of the page | Scroll to the bottom of the page and click the button |  |
| Add Product | Clicking the `ADD` button for a product in the Wishlist adds a quantity of 1 to the bag | Click the `ADD` button for a product in the Wishlist |  |
| View Product | Clicking the `VIEW` button for a product in the Wishlist navigates to the product detail page | Click the `VIEW` button for a product in the Wishlist |  |
| Remove Product | Clicking the `REMOVE` button removes the product from the Wishlist | Click the `REMOVE` button for a product in the Wishlist |  |
| `Checkout Page` |
| Max Width | Reaches maximum width at 1600px | View page using Chrome DevTools and expand width beyond 1600px |  |
| Min Width | All elements can be reduced to a screen width of 320px without distortion | View page using Chrome DevTools and reduce width to 320px |  |
| Hover Effects | Hovering over buttons and navigation links triggers their hover state | Hover over buttons and navigation links |  |
| Back To Top Button | Clicking the back to top button takes the user back to the top of the page | Scroll to the bottom of the page and click the button |  |
| Back To Bag Button | Clicking the `BACK TO BAG` button navigates back to the bag page | Click the `BACK TO BAG` button |  |
| Checkout Toast | An error toast message displays when trying to checkout with an empty bag | Checkout with an empty bag |  |
| Quantity Decrement Button 'Disable' | The quantity decrement button disables when the input value reaches 1 | Reduce quantity input value to 1 |  |
| Quantity Increment Button 'Disable' | The quantity increment button disables when the input value reaches 99 | Increase quantity input value to 99 |  |
| Quantity Input 'Required' | The quantity input does not allow users to submit without a value | Remove the quantity input value and attempt to submit the form |  |
| Quantity Input 'Min/Max Value' | The quantity input does not allow users to submit with a value outside the range of 1-99 | Attempt to submit the form with a value less than 1 or greater than 99 |  |
| Update Button | Clicking the `UPDATE` button updates the bag total to reflect the input quantity | Add/remove a quantity and click the `UPDATE` button |  |
| Update Toast | Updating the bag displays a confirmation toast message and the updated total | Add/remove a quantity and click the `UPDATE` button |  |
| Remove Product | Clicking the `REMOVE` button removes the product from the bag | Click the `REMOVE` button for a product in the bag |  |
| Total Update | Removing a product updates the bag total | Click the `REMOVE` button for a product in the bag |  |
| Product Links | Clicking the product title or image navigates to the product detail page | Click each product title and image |  |
| Bag Summary | All required information is displayed in the order summary | View the summary order section |  |
| Payment Method | All required payment methods are displayed | View the payment method section |  |
| Delivery Option | All delivery options are displayed | View the delivery method section |  |
| Invalid Card | An error toast message displays when using invalid card details | Attempt to checkout using invalid card details |  |
| Confirm Order Button | Clicking the `CONFIRM ORDER` button confirms the order and navigates to the order summary page | Click the `CONFIRM ORDER` button |  |
| Order Confirmation Toast | An error toast message displays when there is an issue confirming the order | Submit the order with missing details |  |
| `Review Page` |
| Max Width | Reaches maximum width at 1600px | View page using Chrome DevTools and expand width beyond 1600px |  |
| Min Width | All elements can be reduced to a screen width of 320px without distortion | View page using Chrome DevTools and reduce width to 320px |  |
| Hover Effects | Hovering over buttons and navigation links triggers their hover state | Hover over buttons and navigation links |  |
| Back To Top Button | Clicking the back to top button takes the user back to the top of the page | Scroll to the bottom of the page and click the button |  |
| Add Review Button | Clicking the `ADD REVIEW` button navigates to the add review page | Click the `ADD REVIEW` button |  |
| Edit Review Button | Clicking the `EDIT` button navigates to the edit review page | Click the `EDIT` button |  |
| Delete Review Button | Clicking the `DELETE` button triggers the delete modal | Click the `DELETE` button |  |
| Delete Modal 'Cancel' | Clicking the `NO` button in the delete modal cancels the deletion | Click the `NO` button in the delete modal |  |
| Delete Modal 'Confirm' | Clicking the `YES` button in the delete modal deletes the review | Click the `YES` button in the delete modal |  |
| Review Details | The review displays the correct username, date, rating, and review content | View all reviews |  |
| Review Toast | A toast message is displayed when a review is successfully added, updated, or deleted | Add, update, and delete a review |  |
| `Add/Edit Review Page` |
| Max Width | Reaches maximum width at 1600px | View page using Chrome DevTools and expand width beyond 1600px |  |
| Min Width | All elements can be reduced to a screen width of 320px without distortion | View page using Chrome DevTools and reduce width to 320px |  |
| Hover Effects | Hovering over buttons and navigation links triggers their hover state | Hover over buttons and navigation links |  |
| Back To Top Button | Clicking the back to top button takes the user back to the top of the page | Scroll to the bottom of the page and click the button |  |
| Form Validation | Required fields are displayed in the form | View the add/edit review form |  |
| Star Rating | Selecting a star rating triggers the selection | Click each star rating |  |
| Invalid Form | An error message is displayed when submitting with missing details | Submit the form with missing details |  |
| Cancel Button | Clicking the `CANCEL` button navigates to the review page | Click the `CANCEL` button |  |
| Review Toast | A toast message is displayed when a review is successfully added or updated | Add and update a review |  |

---

### **Bugs & Fixes**

**Carousel Button Bug**

![Carousel Button Bug](media/docs/bug-carousel-button.jpg)

I encountered this bug when I first viewed the site on my iPhone. It appears to be due to differences in how Safari and Chrome render certain properties. Specifically, the `ADD` button within the product carousel was displaying text vertically, which distorted the layout. I resolved this issue by changing the button’s display type to `flex` and explicitly setting both its height and width.

**Logo Link Bug**

![Logo Link Bug](media/docs/bug-logo-link.gif)

Due to the navbar's design, the logo link became unclickable on medium screens. This problem occurred because the icons container for medium screen sizes was layered on top of the logo. Although the logo remained visible, users couldn't click it, which removed the link to the home page. To fix this, I added a `z-index` to the logo to ensure it was layered above the navigation icons.

**Update Bag Bug**

![Update Bag Bug](media/docs/bug-update-bag.gif)

Since the quantity input field is an editable input, users could potentially remove the number and attempt to submit the form. This was not a problem on the product details page because the `ADD TO BAG` button serves as the form's submission. By marking the input field with the `required` attribute, the form is unable to be submitted without a valid quantity.

However, on the Shopping Bag page, quantity updates are handled via JavaScript. This allowed users to delete the number input and attempt to update the quantity, which caused a server error when the backend received a null value instead of an integer.

To fix this, I updated the `adjust_bag` view to check if the quantity input is valid. If not, the page reloads and displays a toast message to notify the user of the error.

---