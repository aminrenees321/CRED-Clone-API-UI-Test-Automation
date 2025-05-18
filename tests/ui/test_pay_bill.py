def test_pay_bill_success(browser):
    payment_page = PaymentPage(browser)
    payment_page.open()
    payment_page.enter_payment_details("1000", "123")
    payment_page.submit()
    assert payment_page.get_status_message() == "Payment successful"