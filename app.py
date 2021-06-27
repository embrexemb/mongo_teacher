from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
from os import environ
#from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo

load_dotenv()

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')

#app.config['MONGO_URI'] = environ.get('mongodb+srv://Scott:nN5GELRQucw.qJb@cluster0.w73ay.mongodb.net/mars_app?retryWrites=true&w=majority')
#mongo = PyMongo(app, uri="mongodb+srv://Scott:nN5GELRQucw.qJb@cluster0.w73ay.mongodb.net/notepad?retryWrites=true&w=majority")
#app.config['MONGO_URI'] = 'mongodb://localhost:27017/notepad'
app.config['MONGO_URI'] = environ.get(MONGO_URI)

# database setup
#db = SQLAlchemy(app)
mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/notes/mongo')
def note_mongo():
    notes = mongo.db.notepad.find()
    data = []

    for note in notes:
        data.append({
            '_id': str(note['_id']),
            'content': note['content']
        })

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)