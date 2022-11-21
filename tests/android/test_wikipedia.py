from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from allure import step


def test_search():
    with step('Verify Settings tab displaying'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/menu_overflow_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/explore_overflow_settings')).click()
        browser.element((AppiumBy.CLASS_NAME, "android.widget.ImageButton")).click()

    with step('Verify content "BrowserStack" found'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('BrowserStack')
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))

    with step('Verify content "Friends" found'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).clear()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Friends')
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))