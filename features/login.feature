@chrome @firefox
Feature: Login Functionality

  Scenario: Successful login
    Given Navego ate a pagina de login
    When Preencho o usuario "teste@teste.com" e a senha "teste"
    Then Verifico a mensagem "Dados incorretos"
