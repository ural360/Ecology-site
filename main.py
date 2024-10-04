#Импорт
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    #Переменные для энергозатратности приборов
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

#Первая страница
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/1')
def lights():
    return render_template(
                            'lights.html', 
                           )
@app.route('/2')
def lights2():
    return render_template(
                            'lights2.html', 
                            )
@app.route('/3')
def lights3():
    return render_template(
                            'lights3.html', 
                           )
@app.route('/4')
def text():
    return render_template(
                            'text.html', 
                           )
@app.route('/5')
def text1():
    return render_template(
                            'text2.html', 
                           )










app.run(debug=True)