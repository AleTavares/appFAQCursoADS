CREATE USER faq_app WITH PASSWORD 'sua_senha_segura';
CREATE DATABASE faq_db OWNER faq_app;
GRANT ALL PRIVILEGES ON DATABASE faq_db TO faq_app;

\c faq_db;

CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    tipo_usuario ENUM('respondente', 'questionador') NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS temas (
    id_tema SERIAL PRIMARY KEY,
    nome_tema VARCHAR(255) UNIQUE NOT NULL,
    descricao TEXT
);

CREATE TABLE IF NOT EXISTS perguntas (
    id_pergunta SERIAL PRIMARY KEY,
    id_usuario_questionador INTEGER NOT NULL REFERENCES usuarios(id_usuario),
    id_tema INTEGER NOT NULL REFERENCES temas(id_tema),
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    data_pergunta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('pendente', 'respondida') DEFAULT 'pendente'
);

CREATE TABLE IF NOT EXISTS respostas (
    id_resposta SERIAL PRIMARY KEY,
    id_pergunta INTEGER NOT NULL UNIQUE REFERENCES perguntas(id_pergunta),
    id_usuario_respondente INTEGER NOT NULL REFERENCES usuarios(id_usuario),
    texto_resposta TEXT NOT NULL,
    data_resposta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inserir alguns temas iniciais (opcional)
INSERT INTO temas (nome_tema) VALUES ('Geral');
INSERT INTO temas (nome_tema) VALUES ('Matrícula');
INSERT INTO temas (nome_tema) VALUES ('Disciplinas');
INSERT INTO temas (nome_tema) VALUES ('Trabalho de Conclusão de Curso (TCC)');
INSERT INTO temas (nome_tema) VALUES ('Estágios');