from os import name
import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'


@app.route('/', methods=['GET', 'POST'])
def index():
    city1 = 'bangalore'
    city2 = 'Mumbai'
    city3 = 'Tokyo'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    a = requests.get(url.format(city1)).json()
    b = requests.get(url.format(city2)).json()
    c = requests.get(url.format(city3)).json()


    weather = { 'city1':{
        'city' :city1 ,
        'temperature' : a['main']['temp'],
        'description' : a['weather'][0]['description'],
        'icon' : a['weather'][0]['icon']
    }, 'city2':{
        'city' : city2,
        'temperature' : b['main']['temp'],
        'description' : b['weather'][0]['description'],
        'icon' : b['weather'][0]['icon']
    }, 'city3':{
        'city' : city3,
        'temperature' : c['main']['temp'],
        'description' : c['weather'][0]['description'],
        'icon' : c['weather'][0]['icon']
    }
    }

    print(weather)
    
    """ 
   if request.method == 'POST':
        requestcity = request.form["city"]
        print("yes city")
    if not requestcity:
        return render_template('failure.html')
    
    print(requestcity)
    
    m = requests.get(url.format(requestcity)).json()
    requestcity= {'city' : requestcity,
        'temperature' : m['main']['temp'],
        'description' : m['weather'][0]['description'],
        'icon' : m['weather'][0]['icon']}
        """
 
    return render_template('weather.html', city1 = weather['city1'], city2 = weather['city2'],city3 = weather['city3'])


    
