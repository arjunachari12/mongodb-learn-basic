from pymongo import MongoClient
from flask import Flask, request, render_template

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["testdb1"]
collection = db["people"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = int(request.form['age'])

    # Insert into MongoDB
    data = {'name': name, 'age': age}
    collection.insert_one(data)

    return 'Data inserted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
