from flask import Flask, render_template, request, redirect, url_for

app = Flask('__name__')

# Sample data
students = [
    {"usn": 1, "name": "Keerthana", "age": 20,"state":"Bengaluru","phno":9731633434},
    {"usn": 2, "name": "Yashaswini", "age": 22,"state":"Mysore","phno":9731633434},
    {"usn": 3, "name": "Siri", "age": 21,"state":"Coorg","phno":9731633434}
]

# Route to show all students
@app.route('/')
def index():
    return render_template('index.html', students=students)

# Route to add a new student
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        new_student = {
            "usn": max(student["usn"] for student in students) + 1 if students else 1,
            "name": request.form['name'],
            "age": int(request.form['age']),
            "state": request.form['state'],
            "phno": int(request.form['phno'])
        }
        students.append(new_student)
        return redirect(url_for('index'))
    return render_template('add_student.html')

# Route to edit a student
@app.route('/edit/<int:student_usn>', methods=['GET', 'POST'])
def edit_student(student_usn):
    student = next((s for s in students if s["usn"] == student_usn), None)
    if not student:
        return "Student not found", 404

    if request.method == 'POST':
        student['name'] = request.form['name']
        student['age'] = int(request.form['age'])
        student['state'] = request.form['state']
        student['phno'] = int(request.form['phno'])
        return redirect(url_for('index'))

    return render_template('edit_student.html', student=student)

# Route to delete a student
@app.route('/delete/<int:student_usn>')
def delete_student(student_usn):
    global students
    students = [s for s in students if s["usn"] != student_usn]
    return redirect(url_for('index'))


# Run the application
if __name__ == "__main__":
    app.run(debug=True)
