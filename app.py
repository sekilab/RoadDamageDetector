from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
data_list = []

@app.route("/")
def index():
    return render_template_string("""
    <h2>Login</h2>
    <form action="/login" method="post">
        <input name="username" placeholder="username"><br>
        <input type="submit" value="Login">
    </form>
    """)

@app.route("/login", methods=["POST"])
def login():
    return redirect("/form")

@app.route("/form")
def form():
    return render_template_string("""
    <h2>Tambah Data</h2>
    <form action="/submit" method="post">
        <input name="data" placeholder="data"><br>
        <input type="submit" value="Submit">
    </form>
    """)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form.get("data")
    data_list.append(data)
    return redirect("/result")

@app.route("/result")
def result():
    return render_template_string("""
    <h2>Data Tersimpan:</h2>
    <ul>
        {% for item in data %}
        <li>{{ item }}</li>
        {% endfor %}
    </ul>
    <a href="/">Logout</a>
    """, data=data_list)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
