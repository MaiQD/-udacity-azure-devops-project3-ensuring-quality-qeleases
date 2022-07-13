# #!/usr/bin/env python
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

def current_time():
    # ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # return (ts + '\t')
    return ''

# Start the browser and login with standard_user
def login (driver, user, password):
    logging.info (current_time() + 'Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    logging.info (current_time() + 'Navigating to the demo page to login.')
    
    # login
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_id("login-button").click()
    product_label = driver.find_element_by_css_selector("div.header_secondary_container > span.title").text
    assert "PRODUCTS" in product_label
    logging.info(current_time() + 'Login successfully as {:s} .'.format(user))

def add_cart(driver, n):
    logging.info(current_time() + 'Start adding {:d} items to cart.'.format(n))
    for i in range(n):
        driver.find_element_by_css_selector("a#item_"+str(i)+"_img_link").click()
        logging.info(current_time() + 'Navigated to product detail page.')

        driver.find_element_by_css_selector("button.btn.btn_primary.btn_small.btn_inventory").click()
        product_name = driver.find_element_by_css_selector("div.inventory_details_name.large_size").text
        logging.info(current_time() + 'Added {:s} to cart.'.format(product_name))

        driver.find_element_by_css_selector("button#back-to-products").click()
        logging.info(current_time() + 'Navigated back to products page.')
    logging.info(current_time() + 'Add {:d} items to cart successfully.'.format(n))
def remove_cart(driver, n):
    logging.info(current_time() + 'Start removing {:d} items from cart.'.format(n))
    for i in range(n):
        driver.find_element_by_css_selector("a.shopping_cart_link").click()
        logging.info(current_time() + 'Navigated to cart page.')

        driver.find_element_by_css_selector("a#item_"+str(i)+"_title_link").click()
        logging.info(current_time() + 'Navigated to product detail page.')

        driver.find_element_by_css_selector("button.btn.btn_secondary.btn_small.btn_inventory").click()
        product_name = driver.find_element_by_css_selector("div.inventory_details_name.large_size").text
        logging.info(current_time() + 'Remove {:s} from cart.'.format(product_name))

        driver.find_element_by_css_selector("button#back-to-products").click()
        logging.info(current_time() + 'Navigated back to products page.')
    logging.info(current_time() + 'Remove {:d} items from cart successfully.'.format(n))


logging.info (current_time() + 'Starting the browser...')
# --uncomment when running in Azure DevOps.
options = ChromeOptions()
options.add_argument("--headless") 
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()

n = 6
login(driver, 'standard_user', 'secret_sauce')
add_cart(driver, n)
remove_cart(driver, n)

