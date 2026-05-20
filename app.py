from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/books")
def books():
    return render_template("books.html")

@app.route("/fiction")
def fiction():
    return render_template("fiction.html")

@app.route("/finance")
def finance():
    return render_template("finance.html")

@app.route("/selfgrowth")
def selfgrowth():
    return render_template("selfgrowth.html")

@app.route("/technology")
def technology():
    return render_template("technology.html")

@app.route("/buy")
def buy():
    return render_template("buy.html")

@app.route("/rent")
def rent():
    return render_template("rent.html")

@app.route("/bemember")
def bemember():
    return render_template("self.html")

# READING PAGES

@app.route("/read_pride")
def read_pride():
    return render_template("read_pride.html")

@app.route("/read_frank")
def read_frank():
    return render_template("read_frank.html")

@app.route("/read_tale")
def read_tale():
    return render_template("read_tale.html")

    # FINANCE READING PAGES

@app.route("/read_babylon")
def read_babylon():
    return render_template("read_babylon.html")

@app.route("/read_think")
def read_think():
    return render_template("read_think.html")

@app.route("/read_artm")
def read_artm():
    return render_template("read_artm.html")

# SELF HELP READING PAGES

@app.route("/read_speaking")
def read_speaking():
    return render_template("read_speaking.html")

@app.route("/read_analyze")
def read_analyze():
    return render_template("read_analyze.html")


# SEARCH BOOK DATA

books = {

    "How to Analyze People on Sight": "read_analyze",

    "The Art of Money Getting": "read_artm",

    "The Richest Man in Babylon": "read_babylon",

    "Frankenstein": "read_frank",

    "Pride and Prejudice": "read_pride",

    "The Art of Public Speaking": "read_speaking",

    "A Tale of Two Cities": "read_tale",

    "Think and Grow Rich": "read_think"

}

@app.route("/search")
def search():

    query = request.args.get("q")

    if query in books:

        return redirect("/" + books[query])

    return render_template("noresult.html", query=query)

if __name__ == "__main__":
    app.run(debug=True)

