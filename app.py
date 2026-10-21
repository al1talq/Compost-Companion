from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the root route (homepage)
@app.route('/')
def home():
    # Flask looks inside the "templates" folder for this file automatically
    return render_template('index.html')

if __name__ == '__main__':
    # Run the app in debug mode so it restarts when you save changes
    app.run(debug=True)
