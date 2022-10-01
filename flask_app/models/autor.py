from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import libro

class Autor:
    def __init__(self,data):
        self.id = data['id']
        self.autor= data['autor']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        ##Lista vacia donde irán los libros fav del autor. Se llamará en la class de autor_especifico
        self.libros_favoritos = []

    @classmethod
    #Este método es para guardar algo en nuestra base de datos, en este caso, un autor.
    def save(cls,data):
        query = "INSERT INTO autores (autor) VALUES (%(autor)s);"
        resultado = connectToMySQL('esquema_libros').query_db(query,data)
        return resultado

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM autores;"
        resultado =  connectToMySQL('esquema_libros').query_db(query)
        autores = []
        for x in resultado:
            autores.append(cls(x))
        return autores

    @classmethod
    def autor_especifico(cls,data):
        query = "SELECT * FROM autores LEFT JOIN libros_favoritos ON autores.id = libros_favoritos.autor_id LEFT JOIN libros ON libros.id = libros_favoritos.libro_id WHERE autores.id = %(id)s;"
        resultados = connectToMySQL('esquema_libros').query_db(query,data)
        print(resultados)

        autor = cls(resultados[0])

        for row in resultados:

            autor_data = {

                "id": row['libros.id'],
                "titulo": row['titulo'],
                "num_pag": row['num_pag'],
                "created_at": row['libros.created_at'],
                "updated_at": row['libros.updated_at']
            }
            autor.libros_favoritos.append(libro.Libro(autor_data))
        return autor

    @classmethod
    def agregar_favorito(cls,data):
        #agregar a favoritos
        query = "INSERT INTO libros_favoritos (autor_id, libro_id) VALUES (%(autor_id)s,%(libro_id)s);"
        resultado = connectToMySQL('esquema_libros').query_db(query,data)
        print(resultado)
        return resultado

    @classmethod
    def l_no_favoritos(cls,data):
        query = "SELECT * FROM autores;"

    @classmethod
    def no_favoritos(cls,data):
        query = "SELECT * FROM autores WHERE autores.id NOT IN ( SELECT autor_id FROM libros_favoritos WHERE libro_id = %(id)s );"
        autores = []
        results = connectToMySQL('esquema_libros').query_db(query,data)
        for row in results:
            autores.append(cls(row))
        return autores
