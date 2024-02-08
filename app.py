from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.secret_key = "asdsdsdfsdfdsfsdfsdfsdfasfsdfsdfs"

userpass = "mysql+pymysql://root:@"
basedir = "127.0.0.1"
dbname = "/test"

app.config["SQLALCHEMY_DATABASE_URI"] = userpass + basedir + dbname
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    img = db.Column(db.String(800), nullable=False)
    map = db.Column(db.String(800), nullable=False)
    latitude = db.Column(db.Integer, nullable=False)
    longitude = db.Column(db.Integer, nullable=False)

    def __init__(self, name, address, img, map, latitude, longitude):
        self.name = name
        self.address = address
        self.img = img
        self.map = map
        self.latitude = latitude
        self.longitude = longitude



@app.route("/")
def index():
    data_hotel = db.session.query(Hotel)
    return render_template("index.html" , data=data_hotel)

@app.route("/input", methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        img = request.form['img']
        map = request.form['map']
        latitude = request.form['latitude']
        longitude = request.form['longitude']

        add_data = Hotel(name, address, img, map, latitude, longitude)
        
        db.session.add(add_data)
        db.session.commit()

        flash("Input Data Success")

        return redirect(url_for('index'))
    
    return render_template("input.html")

@app.route('/edit/<int:id>')
def edit_data(id):
    data_hotel = Hotel.query.get(id)
    return render_template('edit.html', data=data_hotel)


@app.route('/proses_edit', methods=['POST', 'GET'])
def proses_edit():
    data_hotel = Hotel.query.get(request.form.get('id'))

    data_hotel.name = request.form['name']
    data_hotel.address = request.form['address']
    data_hotel.img = request.form['img']
    data_hotel.map = request.form['map']
    data_hotel.latitude = request.form['latitude']
    data_hotel.longitude = request.form['longitude']
    db.session.commit()

    flash('Edit Data Success')
    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete(id):
    data_employe = Hotel.query.get(id)
    db.session.delete(data_employe)
    db.session.commit()

    flash('Delete Data Success')

    return redirect(url_for('index'))

# # # # # # # # 
import pandas as pd
@app.route("/home" , methods=['GET', 'POST'])
def home():
    # file_path = inputFile
    # df = pd.read_csv(file_path, header=None)
    # print(df) 

    return render_template("index.php")




if __name__ == "__main__":
    app.run(debug=True)
