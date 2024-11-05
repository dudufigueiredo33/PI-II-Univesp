from flask import Flask, render_template, request, redirect, url_for, flash 

import sqlite3 

 

app = Flask(__name__) 

app.secret_key = 'supersecretkey' 

 

# Função para conectar ao banco de dados SQLite 

def get_db_connection(): 

    conn = sqlite3.connect('database.db') 

    conn.row_factory = sqlite3.Row 

    return conn 

 

# Criação da tabela se não existir 

def create_table(): 

    conn = get_db_connection() 

    conn.execute(''' 

        CREATE TABLE IF NOT EXISTS alunos ( 

            id INTEGER PRIMARY KEY AUTOINCREMENT, 

            nome TEXT NOT NULL, 

            nota REAL, 

            ausencias INTEGER 

        ) 

    ''') 

    conn.commit() 

    conn.close() 

 

# Rota principal para visualizar os dados 

@app.route('/') 

def index(): 

    conn = get_db_connection() 

    alunos = conn.execute('SELECT * FROM alunos').fetchall() 

    conn.close() 

    return render_template('index.html', alunos=alunos) 

 

# Rota para adicionar um novo aluno 

@app.route('/add', methods=('GET', 'POST')) 

def add(): 

    if request.method == 'POST': 

        name = request.form['name'] 

        grade = request.form['grade'] 

        absences = request.form['absences'] 

        if not name: 

            flash('O nome é obrigatório!') 

        else: 

            conn = get_db_connection() 

            conn.execute( 

                'INSERT INTO alunos (nome, nota, ausencias) VALUES (?, ?, ?)', 

                (name, grade, absences) 

            ) 

            conn.commit() 

            conn.close() 

            flash('Estudante adicionado com sucesso!') 

            return redirect(url_for('index')) 

    return render_template('add.html') 

 

# Rota para editar as informações do aluno 

@app.route('/edit/<int:id>', methods=('GET', 'POST')) 

def edit(id): 

    conn = get_db_connection() 

    student = conn.execute('SELECT * FROM alunos WHERE id = ?', (id,)).fetchone() 

 

    if request.method == 'POST': 

        name = request.form['name'] 

        grade = request.form['grade'] 

        absences = request.form['absences'] 

 

        if not name: 

            flash('O nome é obrigatório!') 

        else: 

            conn.execute( 

                'UPDATE alunos SET nome = ?, nota = ?, ausencias = ? WHERE id = ?', 

                (name, grade, absences, id) 

            ) 

            conn.commit() 

            conn.close() 

            flash('Informações atualizadas com sucesso!') 

            return redirect(url_for('index')) 

 

    conn.close() 

    return render_template('edit.html', student=student) 

 

# Rota para excluir um estudante 

@app.route('/delete/<int:id>', methods=('POST',)) 

def delete(id): 

    conn = get_db_connection() 

    conn.execute('DELETE FROM alunos WHERE id = ?', (id,)) 

    conn.commit() 

    conn.close() 

    flash( 

    conn.commit() 

    conn.close() 

    flash 

'Estudante excluído com sucesso!') 

    return redirect(url_for('index')) 

 

if __name__ == '__main__': 

    create_table()  # Cria a tabela se ela ainda não existir 

    app.run(debug=True) 

 
