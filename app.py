import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask, request, render_template, flash
from flask_mysqldb import MySQL

# Inicialización de Flask
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # necesario para flash messages

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'database-formulario.ce85czpa3slf.us-east-1.rds.amazonaws.com'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'hkdjjhe67764'
app.config['MYSQL_DB'] = 'contactanos_db'

mysql = MySQL(app)

# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Guardar datos en la base de datos
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO contactos(name, email, message) VALUES(%s, %s, %s)",
            (name, email, message)
        )
        mysql.connection.commit()
        cur.close()

        flash('Contacto guardado exitosamente!')

    return render_template('contact.html')

# Ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)
