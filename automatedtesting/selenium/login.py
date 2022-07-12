# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def currentTime():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (ts + '\t')

# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    print (currentTime() + 'Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    print (currentTime() + 'Navigating to the demo page to login success.')
    
    # login
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_id("login-button").click()
    product_label = driver.find_element_by_css_selector("div[class='product_label']").text
    assert "Products" in product_label
    print(currentTime() + 'Login successfully as {:s} .'.format(user))


login('standard_user', 'secret_sauce')

