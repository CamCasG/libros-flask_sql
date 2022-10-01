from flask_app.models.autor import Autor
from flask_app.models.libro import Libro
from flask_app import app
from flask import redirect, render_template, request

@app.route('/')
def inicio():
    return redirect('/autores')

@app.route('/autores')
def autores():
    return render_template("crear_autor.html", todos_autores=Autor.get_all())

@app.route('/autores/crear', methods=['POST'])
def crear_autor():

    data = { 

        "autor": request.form['autor']
    }
    print(request.form)
    Autor.save(data)
    return redirect('/autores')

@app.route('/autores/<int:id>')
def mostrar_autores(id):

    data = { 
        "id":id
    }

    return render_template('mostrar_autor.html', autor=Autor.autor_especifico(data), libros_no_favoritos=Libro.l_no_favoritos(data))


@app.route('/autores/fav', methods=['POST'])
def libro_favorito():

    data = {

        "autor_id": request.form['autor_id'],
        "libro_id": request.form['libro_id']

    }
    print(request.form)
    Autor.agregar_favorito(data)
    return redirect(f"/autores/{request.form['autor_id']}")