import functions
import PySimpleGUI as sg 

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo" , key="todos")

add_button = sg.Button("Add")

window=sg.Window('My To-Do App',
                 layout=[[label], [input_box, add_button]],
                 font=('Helvetica',20))

while True:
    event, values = window.read()
    
    if event == "Add":
        new_todo = values['todos'] + '\n'
        todos = functions.read_todos()
        todos.append(new_todo)
        functions.write_todos(todos)
    elif event == sg.WIN_CLOSED:
        break
    
window.close()