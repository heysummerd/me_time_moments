from flask import Flask, render_template, request, redirect, url_for
import random
import openpyxl

app = Flask(__name__)

# Function to load data from the Excel database
def load_data():
    excel_file = 'Me Time Moments Activities Database.xlsx'
    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook.active
    data = [row[0].value for row in sheet.iter_rows(min_row=2)]
    workbook.close()
    return data

# Define a route to display the questionnaire
@app.route('/')
def form():
    return render_template('quiz.html')

# Define a route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    user_selection = request.form['goal']

    data = load_data()

    # Filter data based on the user's selection
    filtered_options = [option for option in data if user_selection in option]

    if not filtered_options:
        random_option = random.choice(data)
    else:
        random_option = random.sample(filtered_options, min(len(filtered_options), 3))

    return render_template('quiz.html', options=data, filtered_options=filtered_options, random_option=random_option)

# Define a route to ask the multiple-choice question
@app.route('/goal', methods=['GET'])
def goal():
    return render_template('goal.html')

# Define a route to handle the final submission
@app.route('/date', methods=['POST'])
def final_submission():
    # You can access the user's intention for the date here using request.form['goal']
    intention = request.form['goal']

    # You can perform any necessary processing or redirection here
    # For now, let's just display a message with the selected intention
    return f"Your intention for the date is: {intention}"

# Generate the date
@app.route('/Your_Date')
def Your_Date():
    return "Here's your Date"

if __name__ == '__main__':
    app.run(debug=True)
