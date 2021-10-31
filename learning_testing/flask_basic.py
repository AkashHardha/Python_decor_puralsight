from flask import Flask, request,  render_template
'''from flask import Flask
app = Flask(__name__)

@app.route('/home') 
def hello_world():
   return "Hello World"

if __name__ == '__main__':
   app.run()'''

# this is script with variable //give ulr as /hello/<anyname> ///http://127.0.0.1:5000/hello/akash
'''from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run(debug = True)'''

#this is a example of flask and login.html work togather
'''from flask import Flask
app = Flask(__name__)

@app.route('/login', methods = ['POST' , 'GET'])
def hello_name():
    if request.method == 'POST':
        user = request.form['nm']
        print("akash")
    return user

if __name__ == '__main__':
   app.run(debug = True)'''

from flask import *  
app = Flask(__name__)  
@app.route('/')  
def message():  
      return render_template('hello.html', something_random = 'akash')  
if __name__ == '__main__':  
   app.run(debug = True)