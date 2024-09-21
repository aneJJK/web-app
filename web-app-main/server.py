from random import randint
from flask import Flask, session, redirect, url_for, request, render_template
from main_db_controll import db
def index():
   return render_template('main.html')



def result():
   data = tuple(request.form.values())
   db.add_data(data)
   info = db.get_data()
   print(info)
   return render_template('answer.html', obj=info)



# Створюємо об'єкт веб-програми:
app = Flask(__name__)  
app.add_url_rule('/', 'index', index)   # створює правило для URL '/'
app.add_url_rule('/result', 'result', result, methods=['POST']) # створює правило для URL '/test'
app.config['SECRET_KEY'] = 'secret_key'

if __name__ == '__main__':
   # Запускаємо веб-сервер:
   app.run(debug=True)
