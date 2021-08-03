from conftest import web_browser
from selenium.webdriver import ActionChains

#option 1
menu = web_browser.find_element_by_css_selector('.nav')
hidden_submenu = web_browser.find_element_by_css_selector('.nav #submenu1')

ActionChains(web_browser).move_to_element(menu).click(hidden_submenu)

#option 2
menu = web_browser.find_element_by_css_selector('.nav')
hidden_submenu = web_browser.find_element_by_css_selector('.nav #submenu1')

actions = ActionChains(web_browser)
actions.move_to_element(menu)
actions.click(hidden_submenu)
actions.perform()

def click(self, hold_seconds=0, x_offset=1, y_offset=1):
    element = self.wait_to_be_clickable()

    if element:
        action = ActionChains(self._web_driver)
        action.move_to_element_with_offset(element,x_offset,y_offset).\
            pause((hold_seconds).click(on_element=element).perform())
    else:
        msg = 'Element with locator {0} not found'
        raise AttributeError(msg,format(self._locator))
    if self.wait_after_click:
        self._page.wait_page_loaded()