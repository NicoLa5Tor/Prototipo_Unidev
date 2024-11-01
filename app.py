from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/editar')
def edit():
    return render_template('editar_proyecto.html')
@app.route('/profile')
def profile():
    return render_template('profile.html')
@app.route('/busqueda_postulacion')
def busqueda_postulacion():
    return render_template('busqueda.html')
@app.route('/postulacion')
def postulacion():
    return render_template('postulacion.html')
@app.route('/ver_postulantes')
def postulaciones():
    return render_template('ver_postulantes.html')
@app.route('/gestion_proyectos')
def gestion_proyectos():
    return render_template('proyectos_empresa.html')

@app.route('/evaluacion_ranking')
def evaluacion_ranking():
    return render_template('evaluacion_ranking.html')

@app.route('/gestion_pagos')
def gestion_pagos():
    return render_template('gestion_pagos.html')
@app.route('/ranking_mejores_estudiantes')
def rank_stu():
    return render_template('ranking_mejores_estudiantes.html')
@app.route('/soporte_pqrs')
def soporte_pqrs():
    return render_template('soporte_pqrs.html')

@app.route('/reportes_estadisticas')
def reportes_estadisticas():
    return render_template('reportes_estadisticas.html')

@app.route('/auditoria')
def auditoria():
    return render_template('auditoria.html')

@app.route('/logout')
def logout():
    return "Has cerrado sesión exitosamente."

if __name__ == '__main__':
    app.run(debug=True)
