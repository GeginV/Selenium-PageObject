from pages.auth_page import AuthPage

def test_invalid_user(web_browser):
    page = AuthPage(web_browser)

    page.email.send_keys('email@email.com')
    page.password.send_keys('123')
    page.btn.click()

    assert web_browser.get(url) == ''

