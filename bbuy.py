from splinter import Browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import conf

def bestbuy_automation(url):
    #set up browser
    #add options to browser to avoid headless detection
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('window-size=1366,768')
    chrome_options.add_argument('user-agent=' + conf.user_agent)
    browser = Browser('chrome', executable_path=conf.executable_path, options=chrome_options, headless=True)
    browser.visit(url)
    status = check_product(browser)
    return status

def check_product(browser):
    in_stock = browser.find_by_css("button.c-button.c-button-primary.c-button-lg.c-button-block.c-button-icon.c-button-icon-leading.add-to-cart-button")
    out_stock = browser.find_by_css("button.c-button.c-button-disabled.c-button-lg.c-button-block.add-to-cart-button")
    if len(in_stock) == 1 and len(out_stock) == 0:
        print("Product is in stock!")
        return 0
    else:
        print("Product is out of stock!")
        return 1

'''
def login(browser):
    login_menu = browser.find_by_css('button.c-button-unstyled.plButton.account-button.d-flex.justify-content-center.align-items-center').first
    login_menu.click()
    login_button = browser.find_by_css('a.c-button.c-button-secondary.c-button-sm.sign-in-btn').first
    login_button.click()
    email_input = browser.find_by_css('input#fld-e.tb-input').first
    email_input.fill('jianjunxu123@gmail.com')
    pass_input = browser.find_by_css('input#fld-p1.tb-input').first
    pass_input.fill('jianxu12800')
    submit_button = browser.find_by_css('button.c-button.c-button-secondary.c-button-lg.c-button-block.c-button-icon.c-button-icon-leading.cia-form__controls__submit ').first
    submit_button.click()

def search(browser, keywords):
    search_input = browser.find_by_css('input#gh-search-input.search-input').first
    search_input.fill(keywords)
    search_button = browser.find_by_css('button.header-search-button').first
    search_button.click()
    item = browser.find_by_css('button.c-button.c-button-primary.c-button-sm.c-button-block.c-button-icon.c-button-icon-leading.add-to-cart-button').first
    item.click()

def checkout(browser):
    cart = browser.find_by_css('div.cart-icon').first
    cart.click()
    checkout_button = browser.find_by_css('button.btn.btn-lg.btn-block.btn-primary').first
    checkout_button.click()
    #switch_shipping_button = browser.find_by_css('button.c-button-link.card-call-to-action-button').first
    #switch_shipping_button.click()
    fname = browser.find_by_id('firstName').first
    fname.fill('fname')
    lname = browser.find_by_id('lastName').first
    lname.fill('lname')
    address = browser.find_by_id('street').first
    address.fill('1234 hello street')
    city = browser.find_by_id('city').first
    city.fill('Portland')
    state = browser.find_by_id('state').first
    state.select('OR')
    zipcode = browser.find_by_id('zipcode').first
    zipcode.fill('90000')
    same_address_checkbox = browser.find_by_id('save-for-billing-address-Map {}').first
    same_address_checkbox.check()
    apply_button = browser.find_by_css('button.c-button.c-button-secondary.c-button-md.new-address-form__button').first
    apply_button.click()
    payment_button = browser.find_by_css('button.btn.btn-lg.btn-block.btn-secondary').first
    payment_button.click()
'''