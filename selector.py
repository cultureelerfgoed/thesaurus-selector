import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to read data from CSV file
def read_csv(filename):
    with open(filename, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        thesauri_data = {}
        for row in reader:
            thesaurus = row[0]
            category = row[1]
            if thesaurus not in thesauri_data:
                thesauri_data[thesaurus] = set()
            thesauri_data[thesaurus].add(category)
        return thesauri_data

# Read data from the CSV file
csv_filename = 'C:\\Users\\Ruben\\Documents\\05. RCE\\Termennetwerk\\thesauri_selector\\thesauri_data.csv'
thesauri_data = read_csv(csv_filename)

# Print the data for debugging
print("Thesauri Data:")
print(thesauri_data)

# Get unique categories
categories = set(category for categories in thesauri_data.values() for category in categories)

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_categories = request.form.getlist('categories')

    # Filter thesauri based on selected categories
    filtered_thesauri = [
        thesaurus for thesaurus, categories in thesauri_data.items()
        if set(selected_categories).issubset(categories)
    ]

    # Print debugging information
    print("Selected Categories:", selected_categories)
    print("Filtered Thesauri:", filtered_thesauri)

    return render_template('index.html', categories=categories, selected_categories=selected_categories, filtered_thesauri=filtered_thesauri)

if __name__ == '__main__':
    app.run(debug=True)





# 'C:\\Users\\Ruben\\Documents\\05. RCE\\Termennetwerk\\thesauri_selector\\thesauri_data.csv'