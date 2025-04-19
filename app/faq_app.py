import streamlit as st
import psycopg2
from psycopg2.extras import RealDictCursor

# Função para conectar ao banco de dados
def connect_to_db():
    return psycopg2.connect(
        host="faq_db_container",
        database="faq_db",
        user="faq_app",
        password="app_curso_faat"
    )

# Função para executar consultas no banco de dados
def execute_query(query, params=None, fetch=False):
    conn = connect_to_db()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cursor.execute(query, params)
        if fetch:
            result = cursor.fetchall()
        else:
            conn.commit()
            result = None
    except Exception as e:
        st.error(f"Erro ao executar a consulta: {e}")
        result = None
    finally:
        cursor.close()
        conn.close()
    return result

# Função para exibir o menu
def menu():
    st.sidebar.title("Menu")
    options = ["Usuários", "Temas", "Perguntas", "Respostas"]
    return st.sidebar.radio("Navegação", options)

# Tela de gerenciamento de usuários
def usuarios():
    st.title("Gerenciamento de Usuários")
    st.subheader("Adicionar Novo Usuário")
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    tipo_usuario = st.selectbox("Tipo de Usuário", ["respondente", "questionador"])
    if st.button("Adicionar Usuário"):
        query = """
        INSERT INTO usuarios (nome, email, tipo_usuario)
        VALUES (%s, %s, %s)
        """
        execute_query(query, (nome, email, tipo_usuario))
        st.success("Usuário adicionado com sucesso!")

    st.subheader("Lista de Usuários")
    usuarios = execute_query("SELECT * FROM usuarios", fetch=True)
    if usuarios:
        for usuario in usuarios:
            st.write(f"ID: {usuario['id_usuario']}, Nome: {usuario['nome']}, Email: {usuario['email']}, Tipo: {usuario['tipo_usuario']}")

# Tela de gerenciamento de temas
def temas():
    st.title("Gerenciamento de Temas")
    st.subheader("Adicionar Novo Tema")
    nome_tema = st.text_input("Nome do Tema")
    descricao = st.text_area("Descrição")
    if st.button("Adicionar Tema"):
        query = """
        INSERT INTO temas (nome_tema, descricao)
        VALUES (%s, %s)
        """
        execute_query(query, (nome_tema, descricao))
        st.success("Tema adicionado com sucesso!")

    st.subheader("Lista de Temas")
    temas = execute_query("SELECT * FROM temas", fetch=True)
    if temas:
        for tema in temas:
            st.write(f"ID: {tema['id_tema']}, Nome: {tema['nome_tema']}, Descrição: {tema['descricao']}")

# Tela de gerenciamento de perguntas
def perguntas():
    st.title("Gerenciamento de Perguntas")
    st.subheader("Adicionar Nova Pergunta")
    id_usuario = st.number_input("ID do Usuário Questionador", min_value=1, step=1)
    id_tema = st.number_input("ID do Tema", min_value=1, step=1)
    titulo = st.text_input("Título")
    descricao = st.text_area("Descrição")
    if st.button("Adicionar Pergunta"):
        query = """
        INSERT INTO perguntas (id_usuario_questionador, id_tema, titulo, descricao)
        VALUES (%s, %s, %s, %s)
        """
        execute_query(query, (id_usuario, id_tema, titulo, descricao))
        st.success("Pergunta adicionada com sucesso!")

    st.subheader("Lista de Perguntas")
    perguntas = execute_query("SELECT * FROM perguntas", fetch=True)
    if perguntas:
        for pergunta in perguntas:
            st.write(f"ID: {pergunta['id_pergunta']}, Título: {pergunta['titulo']}, Status: {pergunta['status']}")

# Tela de gerenciamento de respostas
def respostas():
    st.title("Gerenciamento de Respostas")
    st.subheader("Adicionar Nova Resposta")
    id_pergunta = st.number_input("ID da Pergunta", min_value=1, step=1)
    id_usuario = st.number_input("ID do Usuário Respondente", min_value=1, step=1)
    texto_resposta = st.text_area("Texto da Resposta")
    if st.button("Adicionar Resposta"):
        query = """
        INSERT INTO respostas (id_pergunta, id_usuario_respondente, texto_resposta)
        VALUES (%s, %s, %s)
        """
        execute_query(query, (id_pergunta, id_usuario, texto_resposta))
        st.success("Resposta adicionada com sucesso!")

    st.subheader("Lista de Respostas")
    respostas = execute_query("SELECT * FROM respostas", fetch=True)
    if respostas:
        for resposta in respostas:
            st.write(f"ID: {resposta['id_resposta']}, Resposta: {resposta['texto_resposta']}")

# Aplicação principal
def main():
    st.title("Sistema de FAQ")
    option = menu()
    if option == "Usuários":
        usuarios()
    elif option == "Temas":
        temas()
    elif option == "Perguntas":
        perguntas()
    elif option == "Respostas":
        respostas()

if __name__ == "__main__":
    main()