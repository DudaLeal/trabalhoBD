from flask import Flask, render_template, request
import pymysql.cursors

# Creando a conexão com o Bando de Dados -> importante já ter ele salvo.
host = 'localhost'
user = 'root'
password = '040899'
#Definindo o Banco de Dados a ser Usado
database = 'deputados'
# Estabelecendoa conexão
connection = pymysql.connect(host=host, user=user, password=password, database=database,cursorclass=pymysql.cursors.DictCursor)
# Fechando Conexão


app = Flask(__name__)


@app.route('/')
def deputados():
    with connection.cursor() as cursor:
        query_args = []
        if request.args.get("search"):
            sql = """
                    SELECT d.*, l.dataInicio AS dataInicioLegislatura, l.dataFim AS dataFimLegislatura, p.nome AS nomePartido
                    FROM `deputados` d
                    INNER JOIN `Legislatura` l ON d.idLegislaturaInicial = l.idLegislatura
                    INNER JOIN `Partido` p ON d.idPartido = p.idPartido
                    WHERE LOWER(d.nome) LIKE LOWER(%s)
                    ORDER BY d.nome ASC
                """
            search = "%{}%".format(request.args["search"])
            query_args = [search]
        else:
            sql = """
                    SELECT d.*, l.dataInicio AS dataInicioLegislatura, l.dataFim AS dataFimLegislatura, p.nome AS nomePartido
                    FROM `deputados` d
                    INNER JOIN `Legislatura` l ON d.idLegislaturaInicial = l.idLegislatura
                    INNER JOIN `Partido` p ON d.idPartido = p.idPartido
                    ORDER BY `nome` ASC
                """
        cursor.execute(sql, query_args)
        deputados = cursor.fetchall()

    return render_template("deputados.html", deputados=deputados, search=request.args.get("search"))

@app.route('/coordenadores')
def genero():
    with connection.cursor() as cursor:
        sql = """
                SELECT d.sexo, COUNT(*) AS total
                FROM `FrenteParlamentar` f
                INNER JOIN `Deputados` d ON f.idDeputadoCoordenador = d.idDeputado
                GROUP BY d.sexo
            """
        cursor.execute(sql)
        deputados = cursor.fetchall()

    return render_template("genero.html", deputados=deputados)

@app.route('/partidos')
def partidos():
    with connection.cursor() as cursor:
        sql = """
            SELECT p.nome AS nomePartido, COUNT(d.idDeputado) AS total
            FROM Partido p
            INNER JOIN Deputados d ON p.idPartido = d.idPartido
            GROUP BY p.nome
        """
        cursor.execute(sql)
        partidos = cursor.fetchall()

    return render_template("partido.html", partidos=partidos)

@app.route('/despesas')
def despesas_por_deputado():
    with connection.cursor() as cursor:
        sql = """
            SELECT
                D.nome AS Nome_Deputado,
                P.nome AS Nome_Partido,
                COALESCE(SUM(DP.valor), 0) AS Soma_Despesas
            FROM Deputados D
            LEFT JOIN Despesas DP ON D.idDeputado = DP.idDeputado
            LEFT JOIN Partido P ON D.idPartido = P.idPartido
            GROUP BY D.nome, P.nome
            ORDER BY Soma_Despesas DESC;
        """
        cursor.execute(sql)
        despesas = cursor.fetchall()

    return render_template('despesas.html', despesas=despesas)

@app.route('/despesasMediaPartido')
def media_despesas_por_partido():
    with connection.cursor() as cursor:
        sql = """
            SELECT Partido.sigla AS Sigla_Partido,
                (SELECT AVG(Despesas.valor)
                FROM Despesas
                INNER JOIN Deputados ON Despesas.idDeputado = Deputados.idDeputado
                WHERE Deputados.idPartido = Partido.idPartido) AS Media_Despesas_Por_Partido
            FROM Partido;
        """
        cursor.execute(sql)
        partidos = cursor.fetchall()

    return render_template('despesaMediaPartido.html', partidos=partidos)

@app.route('/despesaPartido')
def despesa_por_partido():
    with connection.cursor() as cursor:
        sql = """
            SELECT Partido.sigla AS Sigla_Partido,
                COALESCE(SUM(Despesas.valor), 0) AS Total_Despesas
            FROM Partido
            LEFT JOIN Deputados ON Partido.idPartido = Deputados.idPartido
            LEFT JOIN Despesas ON Deputados.idDeputado = Despesas.idDeputado
            GROUP BY Partido.sigla;
        """
        cursor.execute(sql)
        partidos = cursor.fetchall()

    return render_template('despesaPartido.html', partidos=partidos)



if __name__ == '__main__':
    app.run(debug = True)