from flask import Flask, render_template, request, redirect
from models_db import db, Usuario, Tecnologia
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        discord = request.form['discord']
        github = request.form['github']
        linkedin = request.form['linkedin']
        tecnologias_nomes = request.form.getlist('tecnologia')
        tecnologias_niveis = request.form.getlist('nivel')

        usuario = Usuario(
            nome=nome,
            email=email,
            telefone=telefone,
            discord=discord,
            github=github,
            linkedin=linkedin
        )
        db.session.add(usuario)
        db.session.commit()

        for nome, nivel in zip(tecnologias_nomes, tecnologias_niveis):
            tech = Tecnologia(nome=nome, nivel=nivel, usuario_id=usuario.id)
            db.session.add(tech)
        db.session.commit()

        return redirect('/')

    return render_template('index.html')
@app.route('/integrantes')
def integrantes():
    usuarios = Usuario.query.all()
    return render_template('integrantes.html', usuarios=usuarios)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port)
