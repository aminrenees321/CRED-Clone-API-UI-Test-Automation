class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get("http://localhost:3000/login")

    def enter_email(self, email):
        self.browser.find_element_by_id("email").send_keys(email)

    def enter_password(self, password):
        self.browser.find_element_by_id("password").send_keys(password)

    def submit(self):
        self.browser.find_element_by_id("submit").click()

    def get_welcome_message(self):
        return self.browser.find_element_by_id("welcome").text