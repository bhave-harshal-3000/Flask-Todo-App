from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db=SQLAlchemy(app)


class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(80),nullable=False)
    description=db.Column(db.String(220),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.now())

    def __repr__(self):
        return f"{self.sno} - {self.title}"

with app.app_context():
    db.create_all()

@app.route("/",methods=["GET","POST"])
def rendertemplate():
    if request.method== "POST":
        title=request.form['title']
        description=request.form['description']
        todo=Todo(title=title,description=description)
        db.session.add(todo)
        db.session.commit()
    alltodo=Todo.query.all()
    print( alltodo )
    return render_template("index.html",alltodo=alltodo)



@app.route('/delete/<int:sno>')
def deletetodo(sno):
    todo = db.session.execute(db.select(Todo).filter_by(sno=sno)).scalar_one()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/update/<int:sno>",methods=["GET","POST"])
def update(sno):
    if request.method== "POST":
        todo = db.session.execute(db.select(Todo).filter_by(sno=sno)).scalar_one()
        title=request.form['title']
        description=request.form['description']
        todo.title=title
        todo.description=description
        todo.verified = True
        db.session.commit()
        return redirect("/")
    todo = db.session.execute(db.select(Todo).filter_by(sno=sno)).scalar_one()
    return render_template("update.html",todo=todo)

if __name__== '__main__':
    app.run(debug=True,port=8000)