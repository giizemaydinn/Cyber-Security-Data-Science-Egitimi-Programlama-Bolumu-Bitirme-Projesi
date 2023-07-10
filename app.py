from flask import Flask, jsonify, request, render_template, redirect
from flask_cors import CORS
from models import Todo

from initialize import createApp, createDB

app = createApp()
CORS(app)
createDB()

@app.route("/")
def todos():
    try:
        allTodos = Todo.get_all_todos()
        return render_template('index.html', todos=allTodos)
    
    except Exception as e:
        print("ERROR: ", e)
        return render_template('index.html', todos=allTodos)

@app.route("/addTodo", methods=["POST"])
def addTodo():
    try:
        description = request.form.get("description")
        done = request.form.get("done")

        if description == None:
            return "Description is required"
        
        if done == None:
            done = False
        Todo.add_todo(description, done)

        return redirect('/')
    except Exception as e:
        return "ERROR"


@app.route("/<int:id>", methods=["POST"])
def delete_todo(id):
    try:
        todo = Todo.get_todo_by_id(id)

        if todo is None:
            return "Todo not found"

        if request.method == "POST":
            Todo.delete_todo(id)

            return redirect('/')

    except Exception as e:
        return "ERROR"

@app.route("/update/<int:id>", methods=["POST"])
def update_todo(id):
    try:
        todo = Todo.get_todo_by_id(id)

        if todo is None:
            return "Todo not found"

        elif request.method == "POST":
            description = request.form.get("description")
            done = request.form.get("done")
            print(done)
            if description == None:
                description = todo.description

            if done == None:
                done = todo.done
            Todo.update_todo(id, description, done)

            return redirect('/')

    except Exception as e:
        return "ERROR"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
