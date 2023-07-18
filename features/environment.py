from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from time import sleep


def browser_init(context):
    '''setup for Chrome'''
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)


    '''setup for firefox'''
    # firefox_options = webdriver.FirefoxOptions()
    # firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    # context.driver = webdriver.Firefox(executable_path='./geckodriver.exe', options=firefox_options)


    '''HEADLESS MODE FOR CHROME'''
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(chrome_options=options, service=service)


    '''HEADLESS MODE FOR FIREFOX FOR WINDOWS'''
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')
    firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    context.driver = webdriver.Firefox(executable_path='./geckodriver.exe', options=firefox_options)


    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 12)

    context.app = Application(context.driver)



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
