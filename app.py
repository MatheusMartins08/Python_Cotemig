import os

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

pasta_aula = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    pasta_aula, "alunos.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# --- MODEL (tabela no banco) ---
class Aluno(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    tel = db.Column(db.String(20), nullable=False)  # Alterado para String para aceitar DDD e formatação

    def __repr__(self):
        return f"<Aluno {self.id} {self.nome} {self.tel}>"


with app.app_context():
    db.create_all()


# --- READ — listar ---
@app.route("/")
def index():
    # 2 Ordenado por ID decrescente
    alunos = Aluno.query.order_by(Aluno.id.desc()).all()
    # 3 Quantidade total de alunos enviada para o template
    total_alunos = len(alunos)
    return render_template("lista.html", alunos=alunos, total_alunos=total_alunos)


# --- CREATE — cadastrar ---
@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        tel = request.form.get("tel", "").strip() # 1 Captura o telefone
        
        if not nome or not email or not tel:
            return render_template(
                "formulario.html",
                titulo="Cadastrar aluno",
                erro="Preencha nome, e-mail e telefone.",
                nome=nome,
                email=email,
                tel=tel,
            )
        # 1 Adicionado o campo tel na criação
        aluno = Aluno(nome=nome, email=email, tel=tel)
        db.session.add(aluno)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("formulario.html", titulo="Cadastrar aluno")


# --- UPDATE — editar ---
@app.route("/editar/<int:aluno_id>", methods=["GET", "POST"])
def editar(aluno_id):
    aluno = db.session.get(Aluno, aluno_id)
    if not aluno:
        return redirect(url_for("index"))

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        tel = request.form.get("tel", "").strip() # 1 Captura o telefone
        
        if not nome or not email or not tel:
            return render_template(
                "formulario.html",
                titulo="Editar aluno",
                erro="Preencha nome, e-mail e telefone.",
                nome=nome,
                email=email,
                tel=tel,
                aluno_id=aluno.id,
            )
        # 1 Atualiza o campo tel
        aluno.nome = nome
        aluno.email = email
        aluno.tel = tel
        db.session.commit()
        return redirect(url_for("index"))

    return render_template(
        "formulario.html",
        titulo="Editar aluno",
        nome=aluno.nome,
        email=aluno.email,
        tel=aluno.tel, # 1 Passa o telefone atual para o formulário
        aluno_id=aluno.id,
    )


# --- DELETE — excluir ---
@app.route("/excluir/<int:aluno_id>", methods=["POST"])
def excluir(aluno_id):
    aluno = db.session.get(Aluno, aluno_id)
    if aluno:
        db.session.delete(aluno)
        db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
