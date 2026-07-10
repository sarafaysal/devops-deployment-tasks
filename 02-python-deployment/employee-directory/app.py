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
                font-family: Arial;
                margin:40px;
                background:#f4f4f4;
            }
            .card{
                background:white;
                padding:20px;
                border-radius:10px;
                width:500px;
                box-shadow:0 0 10px rgba(0,0,0,.2);
            }
            h1{
                color:#2c3e50;
            }
            li{
                padding:8px;
            }
        </style>
    </head>
    <body>

        <div class="card">

            <h1>🚀 Employee Directory</h1>

            <ul>

                <li>👩 Sara — Data Scientist</li>
                <li>👨 Ali — DevOps Engineer</li>
                <li>👩 Ayesha — Software Engineer</li>

            </ul>

            <h3 style="color:green;">
            ✅ Python Application Running Successfully
            </h3>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
