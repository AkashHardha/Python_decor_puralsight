from flask import Flask, request,  render_template

from database_json  import Database
# from database_mvc import * // // this is used for traditional database (database_mvc_traditional)

app = Flask(__name__) 

#db = Database()  // this is used for traditional database (database_mvc_traditional)

path = "jason_database/database.json"
db = Database(path)

@app.route('/', methods = ['POST','GET'])  
def message():  

    if request.method == 'POST':
        acc_number = request.form['account_number']
        acc_number_upper = acc_number.upper()
        acc_balance = db.balance(acc_number_upper)
        
        return render_template('index_mvc.html', acc_bal = acc_balance )
    
    return ("it is a get method")

if __name__ == '__main__':  
   app.run(debug = True)