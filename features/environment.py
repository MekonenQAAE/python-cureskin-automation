from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from time import sleep


def browser_init(context, scenario):
    # Allure command
    # behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/checkout_flow.feature
    # And run the following
    # allure serve test_results
    '''setup for Chrome'''
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    # Chrome DevTools Protocol (CDP) for iPhone 12 Pro dimensions
    set_device_metrics_override = dict({
        "width": 390,
        "height": 844,
        "deviceScaleFactor": 100,
        "mobile": True
    })
    context.driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', set_device_metrics_override)

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
    # firefox_options = webdriver.FirefoxOptions()
    # firefox_options.add_argument('--headless')
    # firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    # context.driver = webdriver.Firefox(executable_path='./geckodriver.exe', options=firefox_options)

    # #### BROWSERSTACK For Window and Firefox ####
    # desired_cap = {
    #     'browser': 'Firefox',
    #     'os_version': '10',
    #     'os': 'Windows',
    #     'sessionName': scenario.name
    # }
    # bs_user = 'rickymekonen_S7wo5Q'
    # bs_key = 'DJGttBWXpdRWN6qso4Vs'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    # context.driver.execute_script(
    #     'browserstack_executor:{"action":"setSessionName", "arguments":{"name": " ' + scenario.name + ' " }}')

    # #### BROWSERSTACK For iOS and safari ####
    # desired_cap = {
    #     'bstack:options': {
    #         "os": "OS X",
    #         "osVersion": "Ventura",
    #         "browserVersion": "16.0",
    #         "local": "false",
    #         "seleniumVersion": "3.14.0",
    #     },
    #     "browserName": "Safari",
    # }
    #
    # bs_user = 'rickymekonen_S7wo5Q'
    # bs_key = 'DJGttBWXpdRWN6qso4Vs'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    # context.driver.execute_script(
    #     'browserstack_executor:{"action":"setSessionName", "arguments":{"name": " ' + scenario.name + ' " }}')

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 12)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        context.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {'
                                      '"status":"failed", "reason": "Step failed"}}')

    #


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
