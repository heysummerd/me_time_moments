from flask import Flask, render_template, request, redirect, url_for
import openpyxl

app = Flask(__name__)

# Function to update the Excel database
def update_excel(user_input):
    excel_file = 'Me Time Moments Activities Database.xlsx'
    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook.active

    new_row = [user_input['activitylevel'], user_input['userInput']]
    sheet.append(new_row)

    workbook.save(excel_file)
    workbook.close()

# Define a route to display the survey
@app.route('/')
def form():
    return render_template('userInput.html')

# Define a route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    user_input = {
        'name': request.form['name'],
        'userInput': request.form['userInput']
    }

    update_excel(user_input)

    return redirect(url_for('Your_Date'))

# Generate the date
@app.route('/Your_Date')
def thank_you():
    return "Here's your Date"

if __name__ == '__main__':
    app.run(debug=True)