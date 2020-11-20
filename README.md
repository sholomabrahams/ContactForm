# Internship Project
#### Project to demonstrate some of the tasks performed during my summer 2020 internship at Harbor Labs.
#### Architecture:
* Front-end: Vue.js, Vuetify
* Back-end: Flask
* Databse: SQLite

### To start:
From the `/InternshipCourse` folder, run:
```
pip install -r requirements.txt
set FLASK_APP=app.py
set FLASK_ENV=development   # omit this line for a production server
python -m flask run
```



#### To open front-end dev-server:
```
cd static
npm run serve
```
(You cannot connect to the Flask backend from the front-end dev-server without first enabling CORS)

#### To rebuild front-end:
```
npm run build
```
