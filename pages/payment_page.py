class PaymentPage:
    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get("http://localhost:3000/pay")

    def enter_payment_details(self, amount, cvv):
        self.browser.find_element_by_id("amount").send_keys(amount)
        self.browser.find_element_by_id("cvv").send_keys(cvv)

    def submit(self):
        self.browser.find_element_by_id("submit").click()

    def get_status_message(self):
        return self.browser.find_element_by_id("status").text