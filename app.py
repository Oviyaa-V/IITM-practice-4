from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/register" , methods=['GET','POST']) 
#default HTTP method is GET in route function. for POST method we need to explicitly mention.
def registeration():
    if request.method == 'POST': # the submit button initiates the POST method
        n = request.form['name']
        gen = request.form['gender']
        a = request.form.get('age')
        qual = request.form.get('qualification')
        st = request.form['stream']
        addrs = request.form.get('address')

        return render_template("view.html", name = n, gender = gen, age = a, qualification = qual, stream = st, address = addrs)
    return render_template("register.html")

@app.route('/success')
def display():
    return " <center> <h1> SUBMISSION SUCCESSFUL! </h1> </center>> "

app.run(debug=True)