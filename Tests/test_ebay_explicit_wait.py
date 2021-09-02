import pytest


@pytest.mark.smoketest
def test_ebay_title1(browser):
    browser.get("https://www.ebay.com/")
    assert browser.title == "Electronics, Cars, Fashion, Collectibles & More | eBay"
    browser.find_element_by_id("gh-ac").send_keys("Lexus")
    element = WebDriverWait(browser, 5).until(lambda x: x.find_element_by_xpath("//a[@aria-label='lexus sc430']"))
    element.click()
    assert browser.title == "lexus sc430 | eBay"
