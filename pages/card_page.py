class CardPage:
    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get("http://localhost:3000/add-card")

    def add_card(self, number, expiry, cvv):
        self.browser.find_element_by_id("card_number").send_keys(number)
        self.browser.find_element_by_id("expiry").send_keys(expiry)
        self.browser.find_element_by_id("cvv").send_keys(cvv)
        self.browser.find_element_by_id("submit").click()

    def get_success_message(self):
        return self.browser.find_element_by_id("message").text