from appium.webdriver.common.appiumby import AppiumBy
from behave import given, when, then
from time import sleep



@given('que estou no aplicativo da calculadora')
def calc(context):
    context.camp_result = context.driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/formula")
    context.camp_result.click()


@when('realizar a operação de adição 10 + 20')
def op_add(context):
    context.button1 = context.driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/digit_1")
    context.button1.click()
    context.button0 = context.driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/digit_0")
    context.button0.click()
    context.add_op = context.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="plus")
    context.add_op.click()
    context.button2 = context.driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/digit_2")
    context.button2.click()
    context.button0.click()
    context.button_equals = context.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="equals")
    context.button_equals.click()


@then('resultado esperado deve ser 30')
def result_add(context):
    context.camp_result = context.driver.find_element(by=AppiumBy.ID, value="com.android.calculator2:id/formula")
    assert int(context.camp_result.text) == 30
    sleep(3)
    context.driver.quit()
