#importing all modules
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
#model = joblib.load(open('students_marks_model.pkl', 'rb'))
model = pickle.load(open('students_marks_model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict",methods=['POST'])
def predict():
    if request.method == 'POST':
        study_hours = int(request.form['study_hours']) 
        prediction = model.predict([[study_hours]])[0][0].round(2)
        if study_hours<0 or study_hours>24:
            return render_template('index.html', prediction_text='Enter a valid number of hours(1-24)!!')
        else:
            return render_template('index.html', prediction_text='If you study {} hours per day, You will score approximately {}% marks!'.format( int(study_hours),prediction))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)                        