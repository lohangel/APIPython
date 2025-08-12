# 📚 API da Biblioteca

Uma **API simples para gerenciar usuários** em uma biblioteca online, construída com **FastAPI** e **Supabase**.

Permite:
- Cadastro
- Login
- Gerenciamento de perfis de usuários (listar, obter detalhes e atualizar)

> ⛳ Desenvolvido como parte de uma aula prática em Super Módulo, com foco em **autenticação** e **CRUD**.

---

## 🛠️ Funcionalidades

- 📝 **Cadastro:** Crie uma conta com email, senha, nome e função (ex.: membro, administrador).
- 🔐 **Login:** Autentique-se e receba um token JWT.
- 👥 **CRUD de Usuários:**
  - Listar todos os perfis
  - Obter detalhes de um usuário por ID
  - Atualizar nome ou função
- 📄 Documentação automática com Swagger disponível em: `http://localhost:8000/docs`

---

## 🚀 Tecnologias Utilizadas

- **FastAPI** – Framework moderno e rápido para construção de APIs
- **Supabase** – Banco de dados PostgreSQL + autenticação
- **Pydantic** – Validação de dados
- **Python 3.11+**

---

## 🗂️ Estrutura do Projeto

```bash
/biblioteca-api
├── /aplicativo
│   ├── main.py                  # Ponto de entrada da API
│   ├── /api/v1
│   │   ├── auth.py              # Rotas de cadastro e login
│   │   ├── users.py             # Rotas para gerenciar usuários
│   ├── /núcleo
│   │   ├── config.py            # Configurações do Supabase
│   │   ├── database.py          # Conexão com o Supabase
│   ├── /modelos
│   │   ├── user.py              # Modelos de dados
├── .env                         # Chaves do Supabase (não versionar!)
├── requisitos.txt               # Dependências
├── README.md                    # Este arquivo
├── /imagens
│   └── Structure.png            # Imagem da estrutura de pastas
```
---

✅ Pré-requisitos

Python 3.11+
Conta no Supabase
Git instalado

---
## ⚙️ Configuração

1. Clone o repositório:
git clone https://github.com/seu-usuario/library-api.git
cd biblioteca-api

2. Crie um ambiente virtual:
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

3. Instale as dependências:
pip install -r requisitos.txt

4. Configure o Supabase:
Crie um projeto no Supabase
Copie a URL do projeto e a API Key ("anon") em Configurações > API
Habilite autenticação por e-mail:
Painel > Autenticação > Provedores > E-mail

5. Crie a tabela profiles no SQL Editor:
```
*SQL:
CREATE TABLE profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id),
  full_name VARCHAR(255),
  role VARCHAR(50) DEFAULT 'member',
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
---
```bash
*ini
SUPABASE_URL=https://xyz.supabase.co
SUPABASE_KEY=sua-chave-anônima
```

---

▶️ Como Rodar

Inicie a API localmente:
uvicorn app.main:app --reload
Acesse: http://localhost:8000/docs

---

🔁 Teste as Rotas

🔸 Cadastro
- POST /api/v1/auth/signup

Exemplo de payload:
{

  "email": "teste@email.com",
  
  "password": "senha123",
  
  "full_name": "Teste",
  
  "role": "member"
  
}

🔸 Login

POST /api/v1/auth/login
- Receba o token JWT
- Use o token no Swagger (ícone de cadeado) para testar as rotas protegidas

---

## 🧪 Notas sobre o Desenvolvimento
Durante o processo, enfrentamos e resolvemos:

❌ Configuração incorreta do Supabase (URL/chave)

❌ Problemas com tokens JWT

❌ Erros ao mapear dados para os modelos Pydantic

Tudo foi solucionado com testes, revisão da documentação e uso do Swagger.

A API está estável e pronta para uso! ✅

---

## 📈 Próximos Passos

- 🔄 Rotas para redefinição de senha

- 🔐 Implementar permissões (ex.: só admins listam usuários)

- 📚 Gerenciamento de livros

---

<p align="center"><strong>🚀 Projeto em desenvolvimento contínuo, aplicado pelo Super Módulo pela Infinity School! Sinta-se em casa.</strong></p> 

|       Arquivo         | Imagem Estática                        |
| --------------------- | -------------------------------------- |
|       Diploma         |  |
