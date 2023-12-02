# Deputados

Página web com informações sobre os deputados e alguns gráficos para analise referente aos deputados e seus partidos.

## Requisitos
- Python 3.x
- Bibliotecas: Flask, PyMYSQL
- Banco de dados local ou acesso a um banco de dados externo

## Instalação
1. Clone este repositório ou faça o download do código.
2. Instale as dependências
3. Rode a query do arquivo deputadosdb.sql 

## Configuração do Banco de Dados
1. Configure as credenciais do banco de dados no arquivo `DB-Web.py`.
2. Certifique-se de que o banco de dados esteja criado e acessível.

## Execução
1. Execute o arquivo `DB-Web.py` para iniciar a aplicação.
2. Acesse a aplicação no navegador utilizando o seguinte link: [http://127.0.0.1:5000/](http://127.0.0.1:5000/) (ou outro endereço indicado durante a execução).

## Funcionalidades
- **Página inicial**: Exibi tabela com informações sobre todos os deputados eleitos em 2022.
- **/coordenadores**: Mostra gráfico e tabela comparando quantidade de coordenadores de frente parlamentar do gênero feminino e masculino.
- **/partidos**: Mostra grafico e tabela com quantidade de deputados por partido.
- **/despesas**: Mostra o total de despesas que cada deputado teve desde de janeiro até outubro 2023.
- **/despesaMediaPartido**: Mostra os partidos que tiveram as despesas acima da média no periodo de janeiro até outubro 2023.
- **/despesaPartido**: Mostra o total de despesas que cada partido teve no período de janeiro até outubro 2023.
