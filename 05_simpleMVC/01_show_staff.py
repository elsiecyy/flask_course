from flask import Flask, render_template
import model

app = Flask(__name__, static_url_path='/static', static_folder='./static')

@app.route('/show_staff')
def hello_google():
    staff_data = model.getStaff()
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                                              column=column)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
