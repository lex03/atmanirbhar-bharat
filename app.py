from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__, template_folder='template')

#model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/industry.html')
def hello_world1():
    return render_template("industry.html")

@app.route('/agri.html')
def hello_world2():
    return render_template("agri.html")

@app.route('/edu.html')
def hello_world3():
    return render_template("edu.html")

@app.route('/marketing.html')
def hello_world4():
    return render_template("marketing.html")

@app.route('/index.html')
def hello_world5():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    return 
#    int_features=[int(x) for x in request.form.values()]
#     final=[np.array(int_features)]
#     print(int_features)
#     print(final)
#     prediction=model.predict_proba(final)
#     output='{0:.{1}f}'.format(prediction[0][1], 2)
#     if output>str(0.5):
#         return render_template('agri.html',pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output),bhai="kuch karna hain iska ab?")
#     else:
#         return render_template('agri.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output),bhai="Your Forest is Safe for now")


if __name__ == '__main__':
    app.run(debug=True)
