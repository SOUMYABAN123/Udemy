from flask import Flask, render_template, request


## intializing the flask app, 
## means it will create an instance of Flask class which will be your WSGI application
app = Flask(__name__)

@app.route("/")        ##decorator= as soon as the app instance go to route with the / symbol it will go the defination function
def welcome():
    return "Welcome to the Flask course. This should be an amazing course"

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/forms", methods=['GET', 'POST'])
def form_post():
    if request.method == 'POST':
        pass
    return render_template('form.html')



if __name__ =="__main__":
    app.run(debug = True)




