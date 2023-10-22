from flask import Flask, render_template, request, redirect, url_for
import random
import openpyxl

app = Flask(__name__)

# Function to update the Excel database
def update_excel(user_input):
    excel_file = 'Me Time Moments Activities Database.xlsx'
    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook.active
    data = [row[0].value for row in sheet.iter_rows(min_row=2)] 

    new_row = [user_input['activitylevel'], user_input['userInput']]
    sheet.append(new_row)

    workbook.save(excel_file)
    workbook.close()

# Define a route to display the survey
@app.route('/')
def form():
    return render_template('userInput.html', options=update_excel())

# Define a route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    user_input = {
        'name': request.form['name'],
        'userInput': request.form['userInput']
    }

    update_excel(user_input)

    return redirect(url_for('process_form'))

# Define a route to handle form submission
@app.route('/process_form', methods=['POST'])
def process_form():
    user_selection = request.form['user_selection']

    # Filter data based on the user's selection
    filtered_options = [option for option in update_excel() if user_selection in option]

    if not filtered_options:
        random_option = random.choice(update_excel)
    else:
        random_option = random.sample(filtered_options, min(len(filtered_options), 3))

    return render_template('userInput.html', options= update_excel, filtered_options=filtered_options, random_option=random_option)

# Define a route to handle random selection
@app.route('/pick_random', methods=['GET'])
def pick_random_option():
    data = update_excel()
    random_option = random.choice(data)
    return render_template('userInput.html', random_option=random_option)

# Define a route to ask the multiple-choice question
@app.route('/goal', methods=['GET'])
def goal():
    return render_template('goal.html')


# Generate the date
@app.route('/Your_Date')
def Your_Date():
    return "Here's your Date"

if __name__ == '__main__':
    app.run(debug=True)
