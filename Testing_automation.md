Here is a complete, structured Markdown documentation for your Playwright and Pytest automation suite. You can copy and paste this directly into a `.md` file (for example, `README.md` or `test_documentation.md`) in your VS Code workspace.

---

# E-Commerce Automation Testing Documentation

## Overview

This document outlines the automated testing suite for the e-commerce web application. The test suite is built using **Python**, **Pytest**, and **Playwright** to ensure UI functionality, business logic, and user security are working as expected.

## Technology Stack

* **Language:** Python
* **Testing Framework:** Pytest
* **Automation Tool:** Playwright
* **Target Environment:** Localhost (`[http://127.0.0.1:5500/ecommerce.html](http://127.0.0.1:5500/ecommerce.html)`)

---

## Setup & Execution Prerequisites

Before running the test suite, ensure your environment is correctly configured.

**1. Install Dependencies**

```bash
pip install pytest pytest-playwright

```

**2. Install Playwright Browsers**

```bash
playwright install

```

**3. Run the Tests**
To execute the tests and see the output in the terminal, run:

```bash
pytest test_file_name.py -v

```

*(Optional) To view the browser execution visually, use the headed flag:*

```bash
pytest test_file_name.py --headed

```

---

## Test Suite Summary

The test suite covers authentication, UI security, sorting algorithms, cart logic, tax calculations, and checkout validation.

| Test Case | Module | Objective | Priority |
| --- | --- | --- | --- |
| **TC-01** | Authentication | Verify successful login with valid credentials. | High |
| **TC-02** | Security | Ensure password field input is masked. | High |
| **TC-03** | Product List | Validate "Low to High" price sorting functionality. | Medium |
| **TC-04** | Cart | Prevent negative quantities from generating negative totals. | High |
| **TC-05** | Cart | Verify cart badge counter updates upon item removal. | Medium |
| **TC-06** | Checkout | Validate tax calculation (10% of subtotal). | High |
| **TC-07** | Checkout | Prevent checkout process with an empty cart. | High |

---

## Detailed Test Cases

### TC-01: Valid Login Authentication

**Objective:** Verify that a user can successfully log into the application using valid credentials.

* **Steps:**
1. Navigate to the e-commerce application.
2. Enter `standard_user` in the `#username` field.
3. Enter the valid password in the `#password` field.
4. Click the login submit button.


* **Expected Result:** The user successfully logs in, and the `#user-display` element becomes visible on the dashboard.
* **Assertion:** `page.is_visible("#user-display")` is `True`.

### TC-02: Password Field Security (Masking)

**Objective:** Verify that the password input field masks the user's keystrokes.

* **Steps:**
1. Navigate to the login page.
2. Inspect the `#password` HTML element attributes.


* **Expected Result:** The input field must have the type attribute set to `"password"` to ensure characters are hidden from the screen.
* **Assertion:** `input_type == "password"`.

### TC-03: Product Sorting (Price: Low to High)

**Objective:** Validate that the product sorting feature correctly arranges items in ascending order based on price.

* **Steps:**
1. Log into the application.
2. Select `low-high` from the `#sort-select` dropdown.
3. Extract all product prices displayed on the page.
4. Strip the `$` symbol and convert the extracted strings to float values.


* **Expected Result:** Every price in the list should be less than or equal to the subsequent price.
* **Assertion:** Validates the boolean result of a loop checking ascending numerical order.

### TC-04: Negative Quantity Validation in Cart

**Objective:** Ensure the application handles invalid/negative product quantities properly and prevents negative total amounts.

* **Steps:**
1. Log into the application and add a product to the cart.
2. Navigate to the cart page.
3. Input `-2` into the `#qty-1` field and trigger a `change` event.
4. Retrieve the updated total amount.


* **Expected Result:** The system should reject negative quantities or default to zero. The total amount must never drop below `$0.00`.
* **Assertion:** `total_val >= 0`.

### TC-05: Cart Badge Counter Synchronization

**Objective:** Verify that removing an item from the cart correctly updates the UI badge counter.

* **Steps:**
1. Log into the application.
2. Add two distinct products to the cart.
3. Navigate to the cart page.
4. Click the remove button for the first item (`#remove-btn-1`).
5. Check the value of the `#cart-count` badge.


* **Expected Result:** The cart badge count should dynamically decrease by 1, displaying exactly `1`.
* **Assertion:** `bage_count == "1"` *(Note: inner_text returns a string, ensure types match in the code).*

### TC-06: Tax Calculation Accuracy

**Objective:** Verify that the backend/frontend calculates the tax rate accurately based on the subtotal.

* **Steps:**
1. Log into the application and add an item to the cart.
2. Navigate to the cart page.
3. Extract the `#subtotal-amount` and the `#tax-amount`.
4. Calculate the expected tax programmatically (Subtotal * 10%).


* **Expected Result:** The displayed tax amount must perfectly match the calculated expected tax (rounded to 2 decimal places).
* **Assertion:** `taxval == expectedtax`.

### TC-07: Empty Cart Checkout Prevention

**Objective:** Ensure that a user cannot proceed to the order success page if their cart is empty.

* **Steps:**
1. Log into the application.
2. Navigate directly to the cart page *without* adding any products.
3. Fill in the shipping details (Name, ZIP code).
4. Click the checkout button.


* **Expected Result:** The application should block the transaction, display an error (`#checkout-error`), and prevent navigation to the `#order-success-page`.
* **Assertion:** `not is_success_page` evaluates to `True`.