from appium.webdriver.common.appiumby import AppiumBy
from behave import given, when, then
from time import sleep


class Calculadora:
    def __init__(self, context):
        self.context = context

    def go_to_calculator(self):
        self.context.camp_result = self.context.driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/formula")
        self.context.camp_result.click()

    def perform_addition(self):
        self.context.button1 = self.context.driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/digit_1")
        self.context.button1.click()
        self.context.button0 = self.context.driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/digit_0")
        self.context.button0.click()
        self.context.add_op = self.context.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="plus")
        self.context.add_op.click()
        self.context.button2 = self.context.driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/digit_2")
        self.context.button2.click()
        self.context.button0.click()
        self.context.button_equals = self.context.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="equals")
        self.context.button_equals.click()

    def check_result(self):
        self.context.camp_result = self.context.driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/formula")
        assert int(self.context.camp_result.text) == 30
        sleep(3)
        self.context.driver.quit()