from flask import Flask

app = Flask(__name__)

employees = [
    {"name": "Sara", "role": "Data Scientist"},
    {"name": "Ali", "role": "DevOps Engineer"},
    {"name": "Ayesha", "role": "Software Engineer"}
]

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Employee Directory</title>
        <style>
            body{
                font-family:Arial;
                background:#f4f4f4;
                margin:40px;
            }
            .card{
                background:white;
                padding:20px;
                border-radius:10px;
                width:600px;
                box-shadow:0 0 10px rgba(0,0,0,.2);
            }
            a{
                margin-right:20px;
                text-decoration:none;
                color:#0077cc;
                font-weight:bold;
            }
            li{
                padding:8px;
            }
        </style>
    </head>

    <body>

    <div class="card">

        <h1>🚀 Employee Directory</h1>

        <a href="/">Home</a>
        <a href="/employees">Employees</a>
        <a href="/about">About</a>
        <a href="/contact">Contact</a>

        <hr>

        <h3>Welcome!</h3>

        <p>This application is deployed using:</p>

        <ul>
            <li>Python</li>
            <li>Gunicorn</li>
            <li>Nginx</li>
        </ul>

    </div>

    </body>

    </html>
    """

@app.route("/employees")
def employee_list():

    html = """
    <html>
    <head>
        <title>Employees</title>
    </head>

    <body>

    <h1>Employee List</h1>

    <ul>
    """

    for emp in employees:
        html += f"<li><b>{emp['name']}</b> - {emp['role']}</li>"

    html += """

    </ul>

    <a href="/">Home</a>

    </body>
    </html>

    """

    return html


@app.route("/about")
def about():
    return """
    <h1>About</h1>

    <p>
    This Employee Directory was developed for DevOps deployment practice.
    </p>

    <a href="/">Home</a>
    """


@app.route("/contact")
def contact():
    return """
    <h1>Contact</h1>

    <p>Email: sarafaysal2012@gmail.com</p>

    <a href="/">Home</a>
    """


if __name__ == "__main__":
    app.run(debug=True)
