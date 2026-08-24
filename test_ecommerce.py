# NOW I AM GOING TO IMPORT THE PYTEST , TO INTERGRATE WITH THE PLAYWRIGHT AND PYTEST AS THE FUNCTION TO DEVELOP THE PROGRAM 

import pytest

# TEST 1 : I AM GOING VALID THE LOGIN PAGE , BY GIVING THE USERNAME AND PASSWORD , AS PER CERATED ID TO PASS THE EXECTUTION , AND TO PASS THE TEST CASE [1]

def test_case_1(page):
    page.goto("http://127.0.0.1:5500/ecommerce.html") # HERE I AM SAYING THAT YOU TO GO THAT PAGE
    page.fill("#username","standard_user") # IN THIS PLACE , I GAVED THE ID AND THE PLACE HOLDER AND ITS VALUE 
    page.fill("#password","secret_pass") # SAME
    page.click("#login-submit-btn") # HERE IN THIS PLACE , I AM GOING TO CLICK THE SUBMIT BUTTON , SO I GAVED THE ID OF THE SUBMIT BUTTON
    assert page.is_visible("#user-display") , f"HERE YOU CANT ABLE TO ENTER THE WEBSITE ITSELF , CHECK IT NOW" # I NEED TO ASSIT YOU TO SEE THAT ANY HTML ELEMENT IS THERE IN THIS PAGE AS A ID 


# TEST 2 : I AM GOING CHECK WHEATHER PASSWORD HAS THE TYPE OF PASSWORD , TO BE MASKED :

def test_case_2(page):
    page.goto("http://127.0.0.1:5500/ecommerce.html")   # HERE I AM SAYING THAT YOU TO GO THAT PAGE
    input_type = page.get_attribute("#password","type") # HERE I USED A FUNCTION TO TAKE THE INPUT TYPE FROM THE PASSWORD , 
    assert input_type == "password" , f"Password , Is Need To Be masked , To Give The Valid Input Type For The Filled {input_type}" # AND HERE I USED THE ASSERT TO MAAKE THE TEST CASE PASS OR FAIL 
    
# TEST 3 : HERE I AM GOING CHECK THE OPTION FILED THAT IF I CHOOSE LOOW TO HIGH THEN IT SHOULD BE IN THE ORDER OF ASSENDING TO MAKE SURE OF THAT I TESTING THIS PART 

def test_case_3(page):
    page.goto("http://127.0.0.1:5500/ecommerce.html") # HERE I AM SAYING THAT YOU TO GO THAT PAGE
    page.fill("#username","standard_user") # IN THIS PLACE , I GAVED THE ID AND THE PLACE HOLDER AND ITS VALUE 
    page.fill("#password","secret_pass") # SAME
    page.click("#login-submit-btn") # HERE IN THIS PLACE , I AM GOING TO CLICK THE SUBMIT BUTTON , SO I GAVED THE ID OF THE SUBMIT BUTTON
    
    page.select_option("#sort-select","low-high") # HERE IN THIS PLACE I SELECTED THE OPTION OF LOW TO HIGH 
    
    price_element = page.locator(".product-price").all_inner_texts() # HERE I AMM USING THE LOCATOR TO FIND THE ELEMENT OF THE PRICE AND TO EXTRATE THEM FROM THE HTML , SO I AM USING THE INNER_TEXTS 
    
    numbers_price = [float(p.replace('$',''))  for p in price_element] # HERE I AM USING THE REPLACE FUNCTION TO EXTRATE THE $ SYMBOLO FROM THE PRICE TAGE 
    
    is_sorted = all(numbers_price[p] <= numbers_price[p+1] for p in range(len(numbers_price)-1)) # NOW I AM CHECKING THAT IS  ORDERED IN THE ASSCENDING OREDED WAY 
    
    assert is_sorted , f"It Is Not Sorted In The Asscending Order" # THIS CONDITION STATEMENT AND THE FLASE ENTER TO BE APPERE IF NOT TRUE
    
    # TEST CASE 4 : CHECKING THE AMOUNT VALUE IS IN THE POSTIVE OR NEGATIVE 
    
def test_case_4(page):
    page.goto("http://127.0.0.1:5500/ecommerce.html") # HERE I AM SAYING THAT YOU TO GO THAT PAGE
    page.fill("#username","standard_user") # IN THIS PLACE , I GAVED THE ID AND THE PLACE HOLDER AND ITS VALUE 
    page.fill("#password","secret_pass") # SAME
    page.click("#login-submit-btn") # HERE IN THIS PLACE , I AM GOING TO CLICK THE SUBMIT BUTTON , SO I GAVED THE ID OF THE SUBMIT BUTTON  
    
    page.click("#add-to-cart-1") # NOW I AM CLICKING THE FIRST PRODUCT TO BE ADD
    page.click("#nav-cart-btn") # AND I AM GOING TO VIST THE CART PAGE 
    
    page.fill("#qty-1","-2") # NOW I WANT TO FILL THE CONTENT OF -2 IN THE QUANTIY BOX
    page.dispatch_event("#qty-1","change") # NOW I AM TELLING THAT TO THE WEBSITE YOU NEED TO CHANGE THE QUANTITY FIELD 
    
    total_text = page.inner_text("#total-amount") # NOW I AM TAKING THE TEXT OF THE TOTAL AMOUNT
    total_val = float(total_text) # CHANGING THE TEXT INTO INTEGER 
    
    assert total_val >= 0 , f"YOU CANT GIVE THE TOTAL VALUE IN THENEGATIVE , MUST BE IN THE POSTIVE INTEGER {total_val}" #CONDITION GIVEN IF IT IS FAILED
    
    # TEST CASE 5 : HEREE I AM GOING TO VIST THE CART SECTION AND ITS ITEAM DISPLAY WORKS CORRECTLY OR NOT  
    
def test_case_5(page):
    page.goto("http://127.0.0.1:5500/ecommerce.html") # HERE I AM SAYING THAT YOU TO GO THAT PAGE
    page.fill("#username","standard_user") # IN THIS PLACE , I GAVED THE ID AND THE PLACE HOLDER AND ITS VALUE 
    page.fill("#password","secret_pass") # SAME
    page.click("#login-submit-btn") # HERE IN THIS PLACE , I AM GOING TO CLICK THE SUBMIT BUTTON , SO I GAVED THE ID OF THE SUBMIT BUTTON
    
    page.click("#add-to-cart-1") # HERE I ADD THE PRODUCT IN THE CART
    page.click("#add-to-cart-2") # HERE I ADD THE PRODUCT IN THE CART
    page.click("#nav-cart-btn") # I NAVIGATE TO THE CART PAGE 
    
    page.click("#remove-btn-1") # I USED THE REMOVE BTN ID TO REMOVE THE PRODUCT IN THE CART
    
    bage_count = page.inner_text("#cart-count") # I USED TO IDETIFY THE ELEMENT OF THE VALUE IN THE CART-COUNT
    
    assert bage_count == 1 , "THERE IS THE PROBLEM IN THE RENDERING SITE , BECAUSE WHEN EVER YOU REMOVE THE ELEMENT IT MUST REDUCE THE VALUE -1 , IT IS THE CONCEPT" # CONDITION STATEMENT 
    


def test_case_6(page):
    page.goto("http://127.0.0.1:5500/ecommerce.html") # HERE I AM SAYING THAT YOU TO GO THAT PAGE
    page.fill("#username","standard_user") # IN THIS PLACE , I GAVED THE ID AND THE PLACE HOLDER AND ITS VALUE 
    page.fill("#password","secret_pass") # SAME
    page.click("#login-submit-btn") # HERE IN THIS PLACE , I AM GOING TO CLICK THE SUBMIT BUTTON , SO I GAVED THE ID OF THE SUBMIT BUTTON
    
    page.click("#add-to-cart-1") # I AM GOING TO ADD THE PRODUCT IN THE CART 
    page.click("#nav-cart-btn") # AND GOING TO THE CART PAGE , TO NAVIGATE THAT
    
    subtotal = float(page.inner_text("#subtotal-amount")) # TAKING THE SUBTOTAL AMOUNT VALUE FORM THE WEBSITE , AND SAID IT SHOULD BE INTEGER
    taxval = float(page.inner_text("#tax-amount")) # SAME FOR THE TAXVALUE
    expectedtax = round(subtotal * 0.10 , 2) # AND WRITING THAT THE EXPECTED VALUE MUST * BY 0.10 , TO IT IS SUB  AMMOUNT VALUE
    
    assert taxval == expectedtax , f"'Calculation Bug: Expected tax ${expectedtax}, but app calculated ${taxval}!'" # CONDITIONAL SATEMENT
    
def test_case_7(page):
    page.goto("http://127.0.0.1:5500/ecommerce.html") # HERE I AM SAYING THAT YOU TO GO THAT PAGE
    page.fill("#username","standard_user") # IN THIS PLACE , I GAVED THE ID AND THE PLACE HOLDER AND ITS VALUE 
    page.fill("#password","secret_pass") # SAME
    page.click("#login-submit-btn") # HERE IN THIS PLACE , I AM GOING TO CLICK THE SUBMIT BUTTON , SO I GAVED THE ID OF THE SUBMIT BUTTON
    
    page.click("#nav-cart-btn") # AND GOING TO THE CART PAGE , TO NAVIGATE THAT
    
    page.fill("#shipping-name","Jane Doe") # HERE I AM FILLING THE NAME OF THE USER GOING TO BUY
    page.fill("#shipping-zip","1234") # AND HIS SHIPPING ID
    
    page.click("#checkout-btn") # NOW I AM CLICKING THE COMPLETE BUTTON MOVE FUTHER PROCESS
    
    is_error = page.is_visible("#checkout-error") # IF ANY ERROR IS VISIBLE IT WILL OCCURE
    is_success_page = page.is_visible("#order-success-page") # IF IT GOES TO THE ODER SUCESS PAGE IT WILL IDENTIFY
    
    assert not is_success_page , f"Without Adding The Product In The Cart , You Cant Able To Move on To The Oder-Success-Page , This Basic Bussinees Concept" # CONDITION STATEMENT