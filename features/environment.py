from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from features.application import Application

bs_user = "olegmorozov1"
bs_pw = "YNfQosLfxu4X6zkzYkpY"


def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
    # context.driver = webdriver.Safari()
    # context.driver = webdriver.Firefox(executable_path='drivers/geckodriver.exe')


    ### BrowserStack ###
    # desired_cap = {
    #     'browser': 'Safari',
    #     'browser_version': '13.0',
    #     'os': 'OS X',
    #     'os_version': 'Catalina',
    #     'name': 'Verify that Sign-In with existing account works'
    # }
    #
    # url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)


    # context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver, 25)
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
