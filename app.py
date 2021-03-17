from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")




if __name__== '__name__':
    db.create_all()
    app.run()
