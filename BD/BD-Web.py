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


@app.route('/deputados')
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

@app.route('/g1')
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

@app.route('/g2')
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

if __name__ == '__main__':
    app.run(debug = True)