const express = require("express");

const app = express();

const PORT = 3000;

app.get("/", (req, res) => {
    res.send(`
    <html>

    <head>
        <title>Node.js Employee Directory</title>

        <style>

            body{
                font-family:Arial;
                background:#f4f4f4;
                margin:40px;
            }

            .card{
                background:white;
                padding:20px;
                width:600px;
                border-radius:10px;
                box-shadow:0 0 10px rgba(0,0,0,.2);
            }

        </style>

    </head>

    <body>

    <div class="card">

        <h1>🚀 Node.js Employee Directory</h1>

        <ul>

            <li>Sara — Data Scientist</li>
            <li>Ali — DevOps Engineer</li>
            <li>Ayesha — Software Engineer</li>

        </ul>

        <h3 style="color:green;">
        ✅ Node.js Deployment Successful
        </h3>

    </div>

    </body>

    </html>
    `);
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
