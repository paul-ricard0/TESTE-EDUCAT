CREATE DATABASE db_teste_api_gpt;


CREATE TABLE question (
    id_question INT IDENTITY(1,1) PRIMARY KEY,
    date_time_question DATETIME,
    text_question VARCHAR(100)
);


-- O meu usuário estava sem permissões para fazer referências 
CREATE TABLE answer (
    id_answer INT IDENTITY(1,1) PRIMARY KEY,
    id_question INT,
    date_time_answer DATETIME,
    text_answer VARCHAR(100),
    FOREIGN KEY (id_question) REFERENCES question(id_question)
);

