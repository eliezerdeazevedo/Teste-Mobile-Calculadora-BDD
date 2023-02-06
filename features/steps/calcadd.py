from behave import given, when, then
from features.Pages.classe_calculadora import Calculadora

@given('que estou no aplicativo da calculadora')
def calc(context):
    calculator_steps = Calculadora(context)
    calculator_steps.go_to_calculator()


@when('realizar a operação de adição 10 + 20')
def op_add(context):
    calculator_steps = Calculadora(context)
    calculator_steps.perform_addition()


@then('resultado esperado deve ser 30')
def result_add(context):
    calculator_steps = Calculadora(context)
    calculator_steps.check_result()