from flask import Blueprint, render_template, request
from website.model_cotroller import  ModelController

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('base.html')

@views.route('/output', methods=['POST'])
def output():
    model = ModelController.get_element()[0]
    work_type_float = 0
    work_type = request.form['worktype']
    if work_type == 'children':
        work_type_float = 4
    elif work_type == 'private':
        work_type_float = 2
    elif work_type == 'never-worked':
        work_type_float == 1
    elif work_type == 'self-employed':
        work_type_float == 3
    elif work_type == 'government':
        work_type_float == 0

    gender = request.form['gender']
    if gender == 'male':
        gender = 1
    elif gender == 'female':
        gender = 0
    elif gender == 'others':
        gender == 2

    heart_disease = request.form['heart-disease']
    if heart_disease == 'yes':
        heart_disease = 1
    elif heart_disease == 'no':
        heart_disease = 0

    hypertension = request.form['hypertension']
    if hypertension == 'yes':
        hypertension = 1
    elif hypertension == 'no':
        hypertension = 0

    ever_married = request.form['marriage']
    if ever_married == 'yes':
        ever_married = 1
    elif ever_married == 'no':
        ever_married = 0

    residence_type = request.form['residency']
    if residence_type == 'urban':
        residence_type = 1
    elif residence_type == 'rural':
        residence_type = 0

    smoking_status = request.form['smoking']
    if smoking_status == 'never smoked':
        smoking_status = 1
    elif smoking_status == 'formerly smoked':
        smoking_status = 0
    elif smoking_status == 'smokes':
        smoking_status = 2

    age = request.form['age']
    glucose = request.form['glucose']
    bmi = request.form['bmi']

    data = [gender, age, hypertension, heart_disease, ever_married, work_type_float, residence_type, glucose, bmi, smoking_status]
    data_scaled = model.scale(data)
    
    disease = ''
    
    y_pred = model.get_model().predict(data_scaled)  
    if y_pred[0] == 1:
        disease = 'Kemungkinan terkena penyakit stroke' 
    else:
        disease = 'Tidak terkena penyakit stroke'

    return render_template('output.html', prediction=disease) 
