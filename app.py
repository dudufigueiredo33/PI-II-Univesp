from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Função para conectar ao banco de dados SQLite
def get_db_connection():
    conn = sqlite3.connect(
    conn = sqlite3.connect

    conn = sqlite

    conn
'database.db')
    conn.row_factory = sqlite3.Row
    
    conn.row_factory = sqlite3.Row
    ret

    conn.row_factory = sql

    conn.row_factor

    conn.ro

  
return conn

# Criação da tabela
def create_table():
    conn = get_db_connection()
    conn.execute(
    conn = get_db_connection()
    conn.execute

    conn = get_db_connection()
    conn.exe

    conn = get_db_connection()
    c

    conn = get_db_connection()
  

    conn = get_db_connection()

    conn = get_db_connecti

    conn = get_db_conn

    conn = g

    conn 

    c

 
'''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            grade REAL,
            absences INTEGER
        )
    ''')
    conn.commit()
    conn.close()


    conn.commit()
    conn.clos

    conn.commit()
    con

    conn.commit()
   

    conn.commit()

    conn.comm

    conn

   
# Rota principal para visualizar os dados
@app.route('/')
def index():
    conn = get_db_connection()
    students = conn.execute(
    conn
'SELECT * FROM students').fetchall()
    conn.close()
    
    conn.close()
    

    conn.close

    con
return render_template('index.html', students=students)

# Rota para adicionar um novo estudante
@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        name = request.form[
        name = request

   
'name']
        grade = request.form[
        grade = request

     

   
'grade']
        absences = request.form[
        absences
'absences']

        

       
if not name:
            flash(
  
'O nome é obrigatório!')
        
      

   
else:
            conn = get_db_connection()
            conn.execute(
            conn = get_db_connection()
            conn.execute

            conn = get_db_connection()
      

            conn = get_db_connection()
   

            conn = get_db_connection()

            conn = get_db_connection

            conn =

           
'INSERT INTO students (name, grade, absences) VALUES (?, ?, ?)',
                         (name, grade, absences))
            conn.commit()
            conn.close()
            flash(
                         (name, grade, absences))
            conn.commit()
            conn.close()
            flash

                         (name, grade, absences)
            conn.commit()
            conn.close()

                         (name, grade, absences)
            conn.commit()
            conn.close

                         (name, grade, absences)
            conn.commit()
   

                         (name, grade, absences)
            conn.commit()

                         (name, grade, absences)
           

                         (name, grade, abse)

                         (name, grade, ab)

                         (name, grade,)

                         (name)

            

         

      

   
'Estudante adicionado com sucesso!'
            
            retur

            re

           

        

    
return redirect(url_for('index'))

    

return render_template('add.html')

# Rota para editar as informações do estudante
@app.route('/edit/<int:id>', methods=('GET', 'POST'))

de
def edit(id):
    conn = get_db_connection()
    student = conn.execute(
    conn = get_db_connection()
    student = conn.execute(

    conn = get_db_connection()
    student = conn

    conn = get_db_connection()
 

    conn = get_db_conne

    conn = ge

 
'SELECT * FROM students WHERE id = ?', (id,)).fetchone()

    

   


if request.method == 'POST':
        name = request.form[
        name =
'name']
        grade = request.form[
        grade = r

        grade =
'grade']
        absences = request.form[
        absences
'absences']

        

       
if not name:
            flash(
  
'O nome é obrigatório!')
        
      

   
else:
            conn.execute(
            co

           
'UPDATE students SET name = ?, grade = ?, absences = ? WHERE id = ?',
                         (name, grade, absences, 
                         (name, grade, absences,

                         (name,

             

          

       

    
id))
            conn.commit()
            conn.close()
            flash(
            conn.commit()
            conn.close()
            flash(

            conn.commit()
            conn.close()
            flas

            conn.commit()
            conn.close()
            f

            conn.commit()
            conn.close()
          

            conn.commit()
            conn.close()
    

            conn.commit()
            conn.close()
 

            conn.commit()
            conn.close(

            conn.commit()
            conn.clo

            conn.commit()
            conn

            conn.commit()
       

            conn.commit()
    

            conn.commit()
 

            conn.commit(

            conn.comm

            conn.

            co

           

        

    
'Informações atualizadas com sucesso!')
            
            retur

            re

           

        

    
return redirect(url_for('index'))

    conn.close()
    

    conn.close()
    retu


    conn.close()
    r


    conn.close()
  


    conn.close()


    conn.clo


    conn
return render_template('edit.html', student=student)

# Rota para excluir um estudante
@app.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    conn = get_db_connection()
    conn.execute(
    conn = get_db_connection()
    conn.execute(

    conn = get_db_connection()
    conn.execu

    conn = get_db_connection()
    conn

    conn = get_db_con

    conn = get_db_

    conn = get_

    conn = g

    conn
'DELETE FROM students WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash(
    conn.commit()
    conn.close()

    conn.commit()
   

   
'Estudante excluído com sucesso!')
    
 
return redirect(url_for('index'))

if __name__ == '__main__':
    create_table()  
   

 
# Cria a tabela se ela ainda não existir
    app.run(debug=
    app.run(de

    app.r

   
True)

`