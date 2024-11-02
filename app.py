from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

#criar o banco de dados

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    nota INTEGER NOT NULL,
    materia TEXT NOT NULL
    faltas INTEGER NOT NULL
)
''')

connection.commit()
connection.close()

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Rota para a página principal
@app.route('/')
def index():
    conn = get_db_connection()
    alunos = conn.execute('SELECT * FROM alunos').fetchall()
    conn.close()
    return render_template('index.html', alunos=alunos)

# Rota para adicionar novas notas e faltas
@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        nome = request.form['nome']
        nota = request.form['nota']
        faltas = request.form['faltas']

        conn = get_db_connection()
        conn.execute('INSERT INTO alunos (nome, nota, faltas) VALUES (?, ?, ?)',
                     (nome, nota, faltas))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('add.html')

# Função principal para rodar o aplicativo
if __name__ == '__main__':
    app.run(debug=True)


#rota de edição
@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit(id):
    conn = get_db_connection()
    aluno = conn.execute('SELECT * FROM alunos WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        nome = request.form['nome']
        nota = request.form['nota']
        faltas = request.form['faltas']

        conn.execute('UPDATE alunos SET nome = ?, nota = ?, faltas = ? WHERE id = ?',
                     (nome, nota, faltas, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('edit.html', aluno=aluno)

#rota de deletar
@app.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM alunos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
