-- Criação do Banco de Dados Deputados com CHARSET utf8
CREATE DATABASE Deputados DEFAULT CHARSET=utf8;

-- Usar o Banco de Dados Deputados
USE Deputados;

CREATE TABLE Partido (
    idPartido INT PRIMARY KEY,
    sigla VARCHAR(10),
    nome VARCHAR(100)
);

-- Criação da tabela Legislatura
CREATE TABLE Legislatura (
    idLegislatura INT PRIMARY KEY,
    dataInicio DATE,
    dataFim DATE,
    anoEleicao INT
);

-- Criação da tabela Deputados
CREATE TABLE Deputados (
    idDeputado INT PRIMARY KEY,
    nome VARCHAR(255),
    idLegislaturaInicial INT,
    idLegislaturaFinal INT,
    sexo CHAR(1),
    idPartido INT,
    foto VARCHAR(255),
    email VARCHAR(255),
    idFrente INT,
    FOREIGN KEY (idPartido) REFERENCES Partido(idPartido)
);

-- Criação da tabela Despesas
CREATE TABLE Despesas (
    idDespesa INT PRIMARY KEY,
    nomeParlamentar VARCHAR(255),
    idDeputado INT,
    Descricao VARCHAR(255),
    Fornecedor VARCHAR(255),
    dataEmissao DATE,
    valor DECIMAL(10, 2),
    FOREIGN KEY (idDeputado) REFERENCES Deputados(idDeputado)
);

-- Criação da tabela Frente Parlamentar
CREATE TABLE FrenteParlamentar (
    idFrente INT PRIMARY KEY,
    titulo VARCHAR(255),
    dataCriacao DATE,
    idLegislatura INT,
    telefone VARCHAR(20),
    idDeputadoCoordenador INT,
    idPartidoCoordenador INT,
    idLegislaturaCoordenador INT,
    FOREIGN KEY (idDeputadoCoordenador) REFERENCES Deputados(idDeputado),
    FOREIGN KEY (idPartidoCoordenador) REFERENCES Partido(idPartido),
    FOREIGN KEY (idLegislaturaCoordenador) REFERENCES Legislatura(idLegislatura)
);
