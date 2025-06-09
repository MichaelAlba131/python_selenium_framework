from behave import given, when, then
from features.interactions.LoginInteractions import LoginInteractions
from pages.login_page import LoginPage



@given("Navego ate a pagina de login")
def step_navigate_to_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_interactions = LoginInteractions(context.login_page)
    context.login_page.open()

@when('Preencho o usuario "{username}" e a senha "{password}"')
def step_enter_credentials(context, username, password):
    context.login_interactions = LoginInteractions(context.login_page)
    context.login_interactions.login(username, password)

@then('Verifico a mensagem "{mensagem}"')
def step_impl(context, mensagem):
    context.login_interactions = LoginInteractions(context.login_page)
    assert context.login_interactions.valido_a_mensagem_na_tela(mensagem)