from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Book database (in memory)
books = []

# Route to display the home page
@app.route("/")
def home():
    return render_template("home.html", books=books)

# Route to add a new book
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = request.form.get("book")
        books.append(book)
        return redirect(url_for("home"))
    return render_template("add.html")

# Route to edit a book
@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    if request.method == "POST":
        book = request.form.get("book")
        books[index] = book
        return redirect(url_for("home"))
    return render_template("edit.html", index=index, book=books[index])

# Route to delete a book
@app.route("/delete/<int:index>")
def delete(index):
    books.pop(index)
    return redirect(url_for("home"))

if __name__ == "_main_":
    app.run(debug=True)