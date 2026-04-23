# Flowers4U - Catálogo de Floricultura 🌻

Projeto fullstack desenvolvido como parte de um processo seletivo para a vaga de Desenvolvedor Django. O sistema é uma plataforma de gerenciamento e catálogo de floricultura, contando com uma interface web responsiva e uma API RESTful completa.

## 🚀 Tecnologias Utilizadas
* **Back-end:** Python, Django
* **API:** Django REST Framework (DRF)
* **Front-end:** HTML5, CSS3, Bootstrap 5
* **Banco de Dados:** SQLite (padrão)

## 🎯 Funcionalidades e Requisitos Atendidos
- [x] **Autenticação:** Sistema de login com proteção de rotas (`@login_required` e Middlewares).
- [x] **Área Restrita:** 3 páginas exclusivas para usuários autenticados (Vitrine, Detalhes e Perfil).
- [x] **Banco de Dados:** Mais de 3 modelos relacionais implementados (Category, Flower, Cart, CartItem).
- [x] **CRUD Interface Web:** Operações completas de Criação, Leitura, Atualização e Exclusão integradas ao front-end via `ModelForms`.
- [x] **Validação:** Formulários com validação nativa de tipos de dados.
- [x] **API RESTful:** Rotas exclusivas retornando JSON via `ModelSerializers`.
- [x] **Status Codes:** Respostas HTTP precisas (200 OK, 201 Created, 204 No Content, 404 Not Found).
- [x] **Feedback Visual:** Sistema de mensagens dinâmicas (Toasts) via `django.contrib.messages`.
- [x] **Interface Responsiva:** Uso de herança de templates (`base.html`) e Bootstrap 5 para adaptação mobile.
- [x] **Programação Defensiva:** Tratamento de erros e `try/except` para evitar quebra da aplicação.

## ⚙️ Como Rodar o Projeto Localmente

1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU-USUARIO/floricultura.git](https://github.com/SEU-USUARIO/floricultura.git)

2. Crie e ative o ambiente virtual:

Bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
3. Instale as dependências:

Bash
pip install -r requirements.txt
4. Execute as migrações do banco de dados:

Bash
python manage.py migrate
5. Crie um superusuário para acessar o sistema:

Bash
python manage.py createsuperuser

6. Inicie o servidor:

Bash
python manage.py runserver

O sistema estará disponível em http://127.0.0.1:8000/. Acesse com os dados do usuário recém-criado.


*Lembre-se de trocar `SEU-USUARIO` no item 1 pelo seu nome de usuário real do GitHub.*