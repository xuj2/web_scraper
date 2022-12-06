from splinter import Browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import conf

def nike_automation(url, size):
    #set up browser
    browser = Browser('chrome', executable_path=conf.executable_path, headless=True)
    browser.visit(url)
    status = check_product(browser, size)
    return status

def check_product(browser, size):
    m_size_str = ("M %s / W" % str(size))
    w_size_str = ("/ M %s" % str(size))
    sizes = browser.find_by_css("button.size-grid-dropdown.size-grid-button")
    for option in sizes:
        if m_size_str in option.text or w_size_str in option.text:
            option.click()
            in_stock = browser.find_by_css("li.size.va-sm-m.d-sm-ib.va-sm-t.ta-sm-c.selected")
            if len(in_stock) > 0:
                print("Size %s is available!" % size)
                return 0
            else:
                print("Size %s is not available!" % size)
                return 1
    print("Product is not available!")
    return 1

'''
def login(browser):
    login_button = browser.find_by_css('button.nav-btn.p0-sm.d-sm-b.body-4.u-bold.ml2-sm.mr2-sm').first
    login_button.click()

def search(browser, keyword):
    search_field = browser.find_by_id('VisualSearchInput').first
    search_field.fill("jordan1")
    search_button = browser.find_by_css('div.pre-search-contain').first.find_by_tag('div').first.find_by_tag('button')[1]
    search_button.click()
    browser.visit("https://www.nike.com/cart")
'''