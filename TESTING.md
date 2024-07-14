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
| index.html | ![HTML Validation Result]() |
| products.html | ![HTML Validation Result]() |
| product_detail.html | ![HTML Validation Result]() |
| bag.html | ![HTML Validation Result]() |
| checkout.html | ![HTML Validation Result]() |
| checkout_success.html | ![HTML Validation Result]() |
| profile.html | ![HTML Validation Result]() |
| add_review.html | ![HTML Validation Result]() |
| edit_review.html | ![HTML Validation Result]() |
| add_product.html | ![HTML Validation Result]() |
| edit_product.html | ![HTML Validation Result]() |

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
