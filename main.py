from flask import *

app = Flask(__name__)


@app.route('/times')
@app.route('/times/<int:number>')
def times_table(number=None):
    return render_template('times.html', number=number)


@app.route('/')
def home():
    student_ages = {"Naeemah": 25, "Godwin": 26, "Thapelo": 47, "Jason": 23}
    return render_template('students.html', student_ages=student_ages)


if __name__ == '__main__':
    app.run(debug=True)

# student_ages = {"Naeemah": 25, "Godwin": 26, "Thapelo": 47, "Jason": 23}
# print(student_ages.keys())