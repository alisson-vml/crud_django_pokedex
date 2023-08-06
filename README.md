<h1 align="center">CRUD DJANGO</h1>

<p align = "center">
  <img src=".github/preview.png" alt="Demonstração do projeto" width="100%"/>
</p>

## 💻 Projeto

Esse é um projeto simples de um CRUD de uma Pokédex.
OBS: Tem muita coisa que poderia ser melhor, porém para um CRUD inicial ele serve seu proposito.

## ✔️ Tecnologias utilizadas

- ``DJANGO``
- ``SQLITE``
- ``HTML``
- ``CSS``

# :hammer: Funcionalidades do projeto

- `Create`: Adicionar novos Pokémons no seu banco de dados informando o nome e o link da imagem
- `Editar`: Atualizar informações de um Pokémon específico
- `Delete`: Remover o Pokémon do seu banco de dados
- `Titulo`: Ao clicar no titulo você será redirecionado para a página de Pokémons, para obter o links das imagens


## 🔌 Como rodar o projeto | Local
### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com),[Python](https://www.python.org/downloads/).
Além disto é bom ter um editor para trabalhar com o código como o [VSCode](https://code.visualstudio.com/)

### 🎲 Rodando o Back End (servidor)

```bash
# Clone este repositório
$ git clone https://github.com/alisson-vml/crud_django_pokedex.git

# Cria um ambiente virtual para as dependências
$ python -m venv env

# ativa seu ambiente
$ .\env\Scripts\activate

# Instale as dependências
$ pip install -r requirements.txt

# Execute a aplicação
$ python manage.py runserver

# O servidor inciará na porta:8000 - acesse <http://localhost:8000/core>
```


