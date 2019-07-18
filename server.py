from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "bobbyhill"

@app.route("/")
def index():

    return render_template("sutra.html")
    
if __name__ == "__main__":
    app.run(debug=True)
