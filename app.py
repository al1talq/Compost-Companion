from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define the root route (homepage)
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/results', methods=['GET'])
def results():
    return redirect(url_for("home"))


@app.route('/analyze', methods=['POST'])
def analyze():
    inputted_groceries = request.form.get("grocinputbox", "").strip()
    browns_groceries = request.form.get('browninputbox', "").strip()

    if len(inputted_groceries) > 8000 or len(browns_groceries) > 8000:
        
        return render_template("index.html", 
                               error='Please shorten to 8,000 characters or less')

    #------ADD OPENAI CODE------







    
    


if __name__ == '__main__':
    # Run the app in debug mode so it restarts when you save changes
    app.run(debug=True)
