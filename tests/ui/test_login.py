from pages.login_page import LoginPage

def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.enter_email("user@example.com")
    login_page.enter_password("password123")
    login_page.submit()
    assert login_page.get_welcome_message() == "Welcome, User"