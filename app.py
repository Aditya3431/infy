from flask import Flask
from config import Config
from routes import proj
from db import mysql
app=proj
app.config.from_object(Config)
mysql.init_app(app)
if __name__=='__main__':
    proj.run(debug=True)