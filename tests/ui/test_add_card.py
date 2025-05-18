def test_add_valid_card(browser):
    card_page = CardPage(browser)
    card_page.open()
    card_page.add_card("4111111111111111", "12/26", "123")
    assert card_page.get_success_message() == "Card added successfully"