from flask import Flask, render_template, request, redirect
import csv
import pandas as pd

app = Flask(__name__)

# ==============================
# GET STUDENT
# ==============================
def get_student(regno):
    with open('student_data.csv', newline='') as f:
        for row in csv.DictReader(f):
            if row['regno'] == regno:
                return row
    return None


# ==============================
# GET ROOM
# ==============================
def get_room(room_no):
    with open('room_details.csv', newline='') as f:
        for row in csv.DictReader(f):
            if row['room'] == room_no:
                return row
    return None


# ==============================
# MAIN SCAN PAGE
# ==============================
@app.route('/', methods=['GET','POST'])
def index():
    student = None
    room = None
    error = ""

    if request.method == 'POST':
        regno = request.form['regno'].strip()
        student = get_student(regno)

        if student:
            room = get_room(student['room'])
        else:
            error = "INVALID REGISTRATION NUMBER"

    return render_template('index.html', student=student, room=room, error=error)


# ==============================
# ADMIN PAGE (EDIT CSV)
# ==============================
@app.route('/admin', methods=['GET','POST'])
def admin():

    student_df = pd.read_csv("student_data.csv")
    room_df = pd.read_csv("room_details.csv")

    if request.method == 'POST':

        file_type = request.form.get("type")
        action = request.form.get("action")

        # ================= STUDENT =================
        if file_type == "student":

            if action == "add":
                new_row = {
                    "regno": request.form['regno'],
                    "name": request.form['name'],
                    "department": request.form['department'],
                    "semester": request.form['semester'],
                    "seat": request.form['seat'],
                    "room": request.form['room']
                }

                student_df = pd.concat(
                    [student_df, pd.DataFrame([new_row])],
                    ignore_index=True
                )
                student_df.to_csv("student_data.csv", index=False)

            elif action == "delete":
                index = int(request.form['index'])
                student_df = student_df.drop(index)
                student_df.to_csv("student_data.csv", index=False)

        # ================= ROOM =================
        elif file_type == "room":

            if action == "add":
                new_row = {
                    "room": request.form['room'],
                    "building": request.form['building'],
                    "floor": request.form['floor']
                }

                room_df = pd.concat(
                    [room_df, pd.DataFrame([new_row])],
                    ignore_index=True
                )
                room_df.to_csv("room_details.csv", index=False)

            elif action == "delete":
                index = int(request.form['index'])
                room_df = room_df.drop(index)
                room_df.to_csv("room_details.csv", index=False)

        return redirect('/admin')

    return render_template(
        "admin.html",
        students=student_df.to_dict(orient="records"),
        rooms=room_df.to_dict(orient="records")
    )


# ==============================
# RUN APP (MUST BE LAST)
# ==============================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)