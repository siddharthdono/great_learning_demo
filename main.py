from flask import Flask, request, Response
from joblib import load
import pdb

my_lr_model = load('model/my_linear_regression_model.joblib')

# How to use my model
# my_lr_model.predict([[1]])


# Initialising
app = Flask(__name__)

# Creating the very first route
@app.route("/", methods = ['POST', 'GET'])
def hello_world():
    return "<h1>Hello, World!</h1>"

# Creating the very first route
@app.route("/help", methods = ['GET'])
def help():
    return "<p>Hey, help is here !!!</p>"


# Creating the very first route
@app.route("/testing", methods = ['POST','GET'])
def test():
    # pdb.set_trace()
    # Reading user data
    data = request.json

    # Getting the mydata from userdata
    x = data.get('mydata')
    x = float(x)

    # Getting the predictions
    output = my_lr_model.predict([[float(x)]])

    # My output will be an array
    output = str(output[0])

    # Just return the orignal data back to the user
    return Response(output)

if __name__ == '__main__':
    app.run(debug=True)



