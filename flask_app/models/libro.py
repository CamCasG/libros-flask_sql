from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import autor

class Libro:
    def __init__(self,data):
        self.id = data['id']
        self.titulo= data['titulo']
        self.num_pag = data['num_pag']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #Lista vacia donde irán los autores que dieron fav a determinado libro. Se llamará en el class de specific_book
        self.autores_fav = []

    #métodos de creación
    @classmethod
    def save_book(cls,data):
        query = "INSERT INTO libros (titulo, num_pag) VALUES (%(titulo)s,%(num_pag)s)"
        resultado = connectToMySQL('esquema_libros').query_db(query,data)
        return resultado

    #métodos de consulta
    @classmethod
    def get_all_books(cls):
        #seleccionar todo de mi tabla libros
        query = "SELECT * FROM libros;"
        resultado =  connectToMySQL('esquema_libros').query_db(query)
        # crear una lista vacía
        libros =[]
        for x in resultado:
            #agregar elementos encontrado dentro de mi lista
            libros.append(cls(x))
        return libros

    @classmethod
    def specific_book(cls,data):
        query = "SELECT * FROM libros LEFT JOIN libros_favoritos ON libros.id = libros_favoritos.libro_id LEFT JOIN autores ON autores.id = libros_favoritos.autor_id WHERE libros.id = %(id)s;"
        resultado = connectToMySQL('esquema_libros').query_db(query, data)
        print(resultado)

        libro = cls(resultado[0])

        for row in resultado:

            libro_data = {

                "id" : row["autores.id"],
                "autor" : row["autor"],
                "created_at" : row["autores.created_at"],
                "updated_at" : row["autores.updated_at"]

            }
            libro.autores_fav.append(autor.Autor(libro_data))
        return libro

    @classmethod
    def l_no_favoritos(cls,data):
        query = "SELECT * FROM libros WHERE libros.id NOT IN ( SELECT libro_id FROM libros_favoritos WHERE autor_id = %(id)s );"
        results = connectToMySQL('esquema_libros').query_db(query,data)
        libros = []
        for row in results:
            libros.append(cls(row))
        print(libros)
        return libros
