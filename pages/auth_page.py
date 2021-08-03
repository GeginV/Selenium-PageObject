from pages.base import WebPage
from elements import *

class AuthPage(WebPage):

    def __init__(self,driver,timeout=5):
        super().__init__(driver,timeout)
        url = 'http://petfriends1.herokuapp.com/login'

        driver.get(url)

    email = WebElement(id='email')
    password = WebElement(id='pass')
    btn = WebElement(xpath='/html/body/div/div/form/div[3]/button')

