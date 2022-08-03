from flask import Flask, render_template

app = Flask(__name__)

headings = ("Name","Role","Salary")

table_data = (
    ("Santhosh","ML Associate","15"),
    ("Nandha","HR","16"),
    ("Niky","Manager","17"),
    ("Vishnu","Lawyer","18"),
    ("Jana","Engineer","19")
)

@app.route('/')
def content():
    return render_template('table.html',headings=headings,table_data=table_data)


if __name__ == "__main__":
    app.run(debug=True)
