# Manual Testing Documentation - E-Commerce Web Application (BuggyShop)

## 1. Document Control & Scope

| Attribute | Details |
| :--- | :--- |
| **Project Name** | BuggyShop QA Demo Store |
| **Application Type** | Web Application (HTML5 / Vanilla JavaScript / CSS3) |
| **Test Environment** | Local Host (`http://127.0.0.1:5500/ecommerce.html` or `file:///.../ecommerce.html`) |
| **Browsers Tested** | Google Chrome (v120+), Mozilla Firefox, Microsoft Edge |
| **Document Version** | 1.0.0 |
| **Testing Type** | Functional, Security, Boundary, UI/UX, Business Logic Testing |
| **Target Audience** | QA Engineers, Automation Engineers, Software Developers |

---

## 2. Test Strategy & Execution Approach

### 2.1 Testing Objective
The objective of this manual testing process is to systematically execute functional and security workflows on the BuggyShop web application, evaluate feature compliance against business specifications, and document all defect observations (functional bugs, security risks, calculation errors, and state desyncs).

### 2.2 Prerequisites & Setup
1. **Server Setup**: Launch a local web server (e.g., Live Server on port 5500 or `python -m http.server 5500`).
2. **Access URL**: Open the application URL in a supported web browser.
3. **Test Credentials**:
   * **Valid Username**: `standard_user`
   * **Valid Password**: `secret_pass`

---

## 3. Manual Test Execution Suite

### Module 1: Authentication & User Security

#### **TC-MAN-01: Valid Customer Login Authentication**
* **Test Priority**: High | **Severity**: Major
* **Precondition**: Application is loaded on the login page.
* **Test Steps**:
  1. Navigate to the login page (`#login-page`).
  2. Enter `standard_user` into the **Username** field (`#username`).
  3. Enter `secret_pass` into the **Password** field (`#password`).
  4. Click the **Sign In** button (`#login-submit-btn`).
* **Expected Result**: 
  * User is successfully authenticated.
  * Login page closes and Product Catalog page (`#products-page`) is displayed.
  * Header shows user greeting (`#user-display`), cart button (`#nav-cart-btn`), and logout button (`#logout-btn`).
* **Actual Result**: User logged in successfully; dashboard navigation worked as expected.
* **Status**: **PASS**

---

#### **TC-MAN-02: Password Field Keystroke Masking Validation**
* **Test Priority**: High | **Severity**: Critical (Security)
* **Precondition**: Application is on the login page.
* **Test Steps**:
  1. Inspect the **Password** input field (`#password`).
  2. Enter sensitive characters into the **Password** field.
  3. Right-click and select **Inspect Element** to examine the `<input>` DOM attributes.
* **Expected Result**: 
  * Password characters should be masked with bullets/asterisks on screen.
  * The HTML input tag attribute must be `type="password"`.
* **Actual Result**: 
  * Password characters are displayed in plain cleartext.
  * Input tag attribute is `type="text"`.
* **Status**: **FAIL**
* **Defect Reference**: **[BUG-01]**

---

### Module 2: Product Catalog & Sorting

#### **TC-MAN-03: Product Sorting by Price (Low to High)**
* **Test Priority**: Medium | **Severity**: Major (Functional)
* **Precondition**: User is logged in and viewing the Product Catalog (`#products-page`).
* **Test Steps**:
  1. Observe initial product grid items and their displayed prices:
     * Wireless Bluetooth Headphones ($49.99)
     * Mechanical Gaming Keyboard ($89.99)
     * Ergonomic Optical Mouse ($29.99)
     * Ultra-Wide Gaming Monitor ($299.99)
  2. Click on the **Sort Dropdown** (`#sort-select`).
  3. Select the **"Price: Low to High"** option (`low-high`).
  4. Verify the numerical order of prices displayed on screen.
* **Expected Result**: Products should be sorted in ascending numerical order:
  1. Ergonomic Optical Mouse ($29.99)
  2. Wireless Bluetooth Headphones ($49.99)
  3. Mechanical Gaming Keyboard ($89.99)
  4. Ultra-Wide Gaming Monitor ($299.99)
* **Actual Result**:
  * Products were sorted lexicographically (alphabetical string comparison):
    1. Ergonomic Optical Mouse ($29.99)
    2. Ultra-Wide Gaming Monitor ($299.99) — *(299.99 placed before 49.99)*
    3. Wireless Bluetooth Headphones ($49.99)
    4. Mechanical Gaming Keyboard ($89.99)
* **Status**: **FAIL**
* **Defect Reference**: **[BUG-02]**

---

### Module 3: Cart Management & Calculations

#### **TC-MAN-04: Negative & Zero Quantity Handling in Cart**
* **Test Priority**: High | **Severity**: Major (Boundary / Validation)
* **Precondition**: User has added 1 item ("Wireless Bluetooth Headphones" - $49.99) to the cart and navigated to the Cart page.
* **Test Steps**:
  1. Locate the item quantity input field (`#qty-1`).
  2. Clear the input field and type `-2`.
  3. Trigger the `change` event by clicking outside or pressing Enter.
  4. Observe the **Subtotal**, **Tax**, and **Total** values.
* **Expected Result**: 
  * Cart input should reject negative numbers and zero (`min="1"` boundary).
  * System should default to `1` or prevent negative total calculations. Total should remain $\ge \$0.00$.
* **Actual Result**: 
  * Input accepted `-2`.
  * Subtotal updated to `-$99.98`, tax to `$0.00`, and total amount displayed `-$99.98`.
* **Status**: **FAIL**
* **Defect Reference**: **[BUG-03]**

---

#### **TC-MAN-05: Cart Header Badge Counter Synchronization on Item Removal**
* **Test Priority**: Medium | **Severity**: Moderate (UI Desync)
* **Precondition**: User has added 2 items to the cart. Cart badge header displays `2`.
* **Test Steps**:
  1. Navigate to the Cart page (`#cart-page`).
  2. Verify cart table displays 2 rows and cart badge shows `2`.
  3. Click the **Remove** button (`#remove-btn-1`) for the first item.
  4. Observe table rows and cart header badge (`#cart-count`).
* **Expected Result**: 
  * The item row is removed from the table.
  * Cart header badge updates dynamically from `2` to `1`.
* **Actual Result**: 
  * Item row was deleted from the table.
  * Cart header badge stayed fixed at `2` (UI state out of sync).
* **Status**: **FAIL**
* **Defect Reference**: **[BUG-04]**

---

#### **TC-MAN-06: Tax Calculation Accuracy Verification**
* **Test Priority**: High | **Severity**: Major (Calculation Logic)
* **Precondition**: User has added 1 item ("Wireless Bluetooth Headphones" - $49.99) to the cart.
* **Test Steps**:
  1. Navigate to the Cart page (`#cart-page`).
  2. Inspect the **Subtotal** ($49.99).
  3. Calculate the expected 10% tax: $\$49.99 \times 0.10 = \$4.999 \approx \$5.00$.
  4. Inspect the displayed **Tax (10%)** value (`#tax-amount`).
* **Expected Result**: 
  * Displayed tax should be `$5.00`.
  * Total should be $\$49.99 + \$5.00 = \$54.99$.
* **Actual Result**: 
  * Displayed tax was `$4.95` (Arbitrary $0.05 subtraction in logic).
  * Displayed total was `$54.94`.
* **Status**: **FAIL**
* **Defect Reference**: **[BUG-05]**

---

### Module 4: Checkout & Order Processing

#### **TC-MAN-07: Empty Cart Checkout Prevention**
* **Test Priority**: High | **Severity**: Critical (Business Logic)
* **Precondition**: User is logged in with an **empty** cart (0 items).
* **Test Steps**:
  1. Click the **Cart** button (`#nav-cart-btn`) without adding any items.
  2. Enter `Jane Doe` in the **Full Name** field (`#shipping-name`).
  3. Enter `12345` in the **ZIP Code** field (`#shipping-zip`).
  4. Click the **Complete Purchase** button (`#checkout-btn`).
* **Expected Result**: 
  * System blocks checkout execution.
  * An error message (`#checkout-error`) appears stating "Cart cannot be empty".
  * User remains on the cart page; order reference is not generated.
* **Actual Result**: 
  * System bypasses cart validation and processes the order.
  * Navigated to Order Confirmation page (`#order-success-page`) with a generated Order Reference ID (`ORD-XXXXXX`).
* **Status**: **FAIL**
* **Defect Reference**: **[BUG-06]**

---

## 4. Defect Log & Bug Traceability Matrix (RTM)

| Bug ID | Module | Defect Title | Severity | Root Cause | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BUG-01** | Authentication | Password input exposes cleartext (`type="text"`) | Critical | Missing `type="password"` attribute in HTML line 66. | **Open** |
| **BUG-02** | Catalog | Price sorting performs string/alphabetical comparison | Major | `localeCompare()` used instead of numeric subtraction `a.price - b.price` in line 218. | **Open** |
| **BUG-03** | Cart Page | Quantity input permits negative numbers and negative totals | Major | Missing input `min="1"` restriction and validation check in line 270. | **Open** |
| **BUG-04** | Cart Page | Header cart count badge does not decrement on item removal | Moderate | `updateCartBadge()` was omitted in `removeFromCart()` line 278. | **Open** |
| **BUG-05** | Cart Page | 10% tax calculation has a -$0.05 calculation skew | Major | Hardcoded `- 0.05` subtraction in `calculateTotals()` line 289. | **Open** |
| **BUG-06** | Checkout | Empty cart checkout bypass creates valid order IDs | Critical | Missing guard clause `if (cart.length === 0)` in `handleCheckout()` line 300. | **Open** |

---

## 5. Exploratory & Edge Case Testing Findings

| Scenario | Input / Action | Observed Behavior | Risk Level |
| :--- | :--- | :--- | :--- |
| **Invalid ZIP Input** | Entered letters `ABCDE` into Postal Code | Accepted without regex validation | Low |
| **Multiple Removals** | Added 4 items, removed all 4 manually | Table emptied, but cart badge showed `4` | Medium |
| **Logout & Re-login** | Logged out and logged back in | Cart state cleared, but UI page defaults to login | Low |

---

## 6. Manual Execution Summary

```
Total Test Cases Executed : 7
Passed                    : 1  (14.3%)
Failed                    : 6  (85.7%)
Total Defected Logged     : 6
```

### Recommendation & Conclusion
The core authentication workflow is operational; however, **Release Sign-Off is REJECTED** due to critical security defects (cleartext password input) and high-severity business logic errors (empty cart purchases, negative monetary values, and tax calculation discrepancies). Developers should resolve defects **BUG-01 through BUG-06** prior to re-testing.
