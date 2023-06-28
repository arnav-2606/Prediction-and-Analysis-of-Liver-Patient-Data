from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open(r'model.pkl', 'rb'))
scaler = pickle.load(open(r'scaler.pkl', 'rb'))


@app.route('/')
def homescreen():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    age = request.form["age"]
    gender = request.form["gender"]
    tbil = request.form["tbil"]
    dbil = request.form["dbil"]
    alp = request.form["alp"]
    alt = request.form["alt"]
    ast = request.form["ast"]
    tp = request.form["tp"]
    alb = request.form["alb"]
    agr = request.form["agr"]
    
    if gender == 'male':
        gender=1
    else:
        gender=0
    
    scaled_data = scaler.transform([[age,dbil,alp,ast,alb,agr,gender]])
    prediction = model.predict(scaled_data)
    if prediction[0]==1:
        result = "You are a potential Liver Patient"
    else:
        result = "You are not a Liver Patient"
    return render_template("index.html", result = result)

if __name__ == '__main__':
    app.run(debug=True)