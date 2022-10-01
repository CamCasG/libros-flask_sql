from flask_app.models.libro import Libro
from flask_app.models.autor import Autor
from flask_app import app
from flask import redirect, render_template, request

@app.route('/libros')
def mostrar_libros():
    return render_template("crear_libro.html", todos_libros=Libro.get_all_books())

@app.route('/libros/crear', methods=['POST'])
def agregar_libro():

    data = { 

        "titulo": request.form['titulo'],
        "num_pag": request.form['num_pag']
    }
    
    print(request.form)
    Libro.save_book(data)
    return redirect('/libros')

@app.route('/libros/<int:id>')
def mostrar_libros_favoritos(id):

    data = { 
        "id":id
    }

    return render_template('mostrar_libro.html', libro=Libro.specific_book(data), autores_no_favoritos=Autor.no_favoritos(data))


#ruta para poder agregar a favoritos.
@app.route('/libros/fav', methods=['POST'])
def autor_favorito():

    data = {

        "autor_id": request.form['autor_id'],
        "libro_id": request.form['libro_id']

    }
    print(request.form)
    #para poder llamar algo de otra clase, hay que importarla en las primeras líneas.
    Autor.agregar_favorito(data)
    return redirect(f"/libros/{request.form['libro_id']}")