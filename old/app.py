from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import urllib
import pyodbc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'creating_new_doc_23'

params = urllib.parse.quote_plus("Driver={ODBC Driver 17 for SQL Server};"
                                 "Server=tcp:lida-dat-cms-test.database.windows.net;"
                                 "Database=lida_dat_cms_test;"
                                 "Uid=medich;"
                                 "Pwd=LIDA@LeedsPrism22;"
                                 "Encrypt=yes;"
                                 "TrustServerCertificate=no;"
                                 "Connection Timeout=30;")

app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params

db = SQLAlchemy(app)

class FormModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

class Form(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = Form()
    if form.validate_on_submit():
        entry = FormModel(name=form.name.data, email=form.email.data)
        db.session.add(entry)
        db.session.commit()
        return 'Thank You'
    return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)