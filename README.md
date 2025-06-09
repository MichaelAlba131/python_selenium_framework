<!DOCTYPE html>
<html lang="pt-BR">

<body>

<h1>🚀 Framework de Automação BDD com Selenium & Behave (Python)</h1>

<div class="center">
  <img class="badge" src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python version" />
  <img class="badge" src="https://img.shields.io/badge/Selenium-4.x-green.svg" alt="Selenium version" />
  <img class="badge" src="https://img.shields.io/badge/Behave-BDD-orange.svg" alt="Behave version" />
  <img class="badge" src="https://img.shields.io/badge/Browsers-Chrome%20%7C%20Firefox-yellow.svg" alt="Browsers Supported" />
</div>

<hr/>

<h2>🎯 Sobre o Projeto</h2>
<p>Este projeto é um <strong>framework de automação de testes</strong> desenvolvido em <strong>Python</strong> que utiliza:</p>
<ul>
  <li>Selenium WebDriver para automação de browser</li>
  <li>Behave para desenvolvimento orientado a comportamento (BDD)</li>
  <li>WebDriver Manager para gerenciar automaticamente os drivers dos navegadores</li>
  <li>Paralelismo para execução simultânea em múltiplos browsers (Chrome e Firefox)</li>
  <li>Padrão Page Object Model (POM) para melhor organização e manutenção dos testes</li>
</ul>
<hr/>

<h2>🏗️ Estrutura do Projeto</h2>
<pre><code>.
├── features/
│   ├── environment.py          # Hooks (setup e teardown dos testes)
│   ├── interactions/
│   │   └── login_interactions.py # Ações encapsuladas (ex: login)
│   ├── steps/
│   │   └── login_steps.py      # Steps BDD para o login
│   └── login.feature           # Feature file (cenários BDD)
├── pages/
│   └── login_page.py           # Page Object Model (elementos da página)
├── runners/
│   └── parallel_runner.py      # Script para execução paralela dos testes
├── utils/
│   └── utils.py                # Utilitários (espera dinâmica, etc)
├── requirements.txt            # Dependências do projeto
└── README.md                   # Esta documentação
</code></pre>

<hr/>

<h2>🚀 Como Executar os Testes</h2>

<h3>1. Pré-requisitos</h3>
<ul>
  <li>Python 3.8 ou superior instalado</li>
  <li>Google Chrome e/ou Mozilla Firefox instalados</li>
  <li>Internet para baixar drivers com WebDriver Manager</li>
</ul>

<h3>2. Instalar dependências</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>3. Rodar os testes localmente</h3>
<p>Por padrão roda no Chrome:</p>
<pre><code>behave features/</code></pre>
<p>Para rodar em Firefox, configure variável de ambiente:</p>
<pre><code>BROWSER=firefox behave features/</code></pre>
<p>Para rodar em modo headless (sem abrir janela):</p>
<pre><code>HEADLESS=true behave features/</code></pre>

<h3>4. Execução Paralela</h3>
<pre><code>python runners/parallel_runner.py</code></pre>
<p>Executa os testes em Chrome e Firefox simultaneamente usando multiprocessing.</p>

<hr/>

<h2>⚙️ Configurações Importantes</h2>
<table>
  <thead>
    <tr>
      <th>Variável Ambiente</th>
      <th>Descrição</th>
      <th>Valores possíveis</th>
      <th>Padrão</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>BROWSER</code></td>
      <td>Navegador para executar os testes</td>
      <td><code>chrome</code>, <code>firefox</code></td>
      <td><code>chrome</code></td>
    </tr>
    <tr>
      <td><code>HEADLESS</code></td>
      <td>Executar em modo headless</td>
      <td><code>true</code>, <code>false</code></td>
      <td><code>false</code></td>
    </tr>
  </tbody>
</table>

<hr/>

<h2>📚 Detalhes Técnicos</h2>

<h3>Page Object Model (POM)</h3>
<p>Organiza elementos e interações com a página web em classes, facilitando manutenção e legibilidade.</p>
<pre><code>class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def username_input(self):
        return self.driver.find_element(By.XPATH, "//input[@name='email']")
</code></pre>

<h3>Utils.py</h3>
<p>Contém funções úteis como <code>wait_for_element</code> e <code>wait_for_text</code> para esperas dinâmicas e robustas.</p>

<h3>Paralelismo</h3>
<p>Executa os testes para múltiplos browsers em paralelo usando o módulo <code>multiprocessing</code> do Python.</p>

<hr/>

<h2>🧪 Exemplos de Cenários (BDD)</h2>
<pre><code>@chrome @firefox
Feature: Login Functionality

  Scenario: Successful login
    Given Navego ate a pagina de login
    When Preencho o usuario "teste@teste.com" e a senha "teste"
    Then Verifico a mensagem "Dados incorretos"
</code></pre>

<hr/>

<h2>📌 Boas Práticas &amp; Recomendações</h2>
<ul>
  <li>Utilize sempre variáveis de ambiente para configuração do browser e modo headless</li>
  <li>Use POM para manter o código limpo e reutilizável</li>
  <li>Separe steps por funcionalidade para facilitar escalabilidade do framework</li>
</ul>

<hr/>

<h2>🎉 Integração com Allure para Relatórios</h2>
<p>O framework pode gerar relatórios detalhados e visualmente amigáveis utilizando o <strong>Allure Framework</strong>. Veja como configurar:</p>

<h3>1. Instalar dependências</h3>
<pre><code>pip install allure-behave allure-python-commons</code></pre>

<h3>2. Instalar Allure Commandline</h3>
<p>Baixe e instale o <a href="https://github.com/allure-framework/allure2/releases" target="_blank" rel="noopener noreferrer">Allure Commandline</a> para gerar e visualizar os relatórios.</p>
<ul>
  <li><strong>macOS:</strong> <code>brew install allure</code></li>
  <li><strong>Windows:</strong> <code>scoop install allure</code></li>
  <li><strong>Manual:</strong> Baixe do site oficial e configure o executável no <code>PATH</code></li>
</ul>

<h3>4. Executar os testes com Allure</h3>
<p>Para rodar os testes gerando os resultados para o Allure, use o comando abaixo, substituindo variáveis conforme necessário:</p>
<pre><code>BROWSER=chrome HEADLESS=true behave -f allure_behave.formatter:AllureFormatter -o allure-results features/</code></pre>

<h3>5. Gerar e abrir o relatório Allure</h3>
<p>Após a execução dos testes, gere o relatório HTML com:</p>
<pre><code>allure generate allure-results --clean -o allure-report</code></pre>
<p>E abra o relatório no navegador:</p>
<pre><code>allure open allure-report</code></pre>

<h3>Resumo dos comandos</h3>
<pre><code>
# Executar testes com Allure (exemplo Chrome + headless)
BROWSER=chrome HEADLESS=true behave -f allure_behave.formatter:AllureFormatter -o allure-results features/

# Gerar relatório Allure
allure generate allure-results --clean -o allure-report

# Abrir relatório Allure
allure open allure-report
</code></pre>
<hr/>

<h2>🤝 Contribuição</h2>
<p>Contribuições são bem-vindas! Abra uma issue ou faça um pull request para melhorias, correções e novas features.</p>

<hr/>

<h2>🪪 Licença</h2>
<p>
Distribuído sob a licença MIT. Veja o arquivo <code>LICENSE</code> para mais informações.
</p>
</body>
</html>