from flask import Flask, render_template_string
from datetime import datetime
import sqlite3

app = Flask (__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title> Weather Dashboard </title>
    <meta name="viewport" content="witdh=device-width, initial-scale=1">
    
    <style>
    body {
        font-family: Arial; 
        padding: 20px; 
        background: #F0F4F8;
        color: 2B2D42;
    }
    
    h1 {
        color: #1F7A8C;
    }
    
    table {
        width: 90%; 
        border-collapse: collapse; 
        margin-top: 20px;
    }
    
    th, td {
        padding: 10px;
        border: 1px solid #ccc;
    }
    
    th {
        background-color: #A8DADC;
        color: #2B2D42;
    }
    
    td {
        background-color: #E0FBFC;
    }
    
    tr:nth-child (even) td {
        background-color: #F0F4F8;
    }
    
    </style>
</head>

<body>
    <h1> 🌤️ Weather Dashboard </h1>
    <table>
        <tr>
            <th>Time</th>
            <th>Condition</th>
            <th>Temperature in Celcius</th>
            <th>Wind in KM/H</th>
            <th>Wind Direction</th>
        </tr>
        {% for row in data %}
        <tr>
            <td>{{ row[1] }}</td>
            <td>{{ row[2] }}</td>
            <td>{{ row[3] }}</td>
            <td>{{ row[4] }}</td>
            <td>{{ row[5] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""


@app.route ("/")
def index():
    conn = sqlite3.connect ("/app/data/weather.db")
    cursor = conn.cursor()
    cursor.execute ("SELECT * FROM weather ORDER BY id DESC LIMIT 10")
    data = cursor.fetchall()
    conn.close()
    
    # Formating the UNIX timestamps (row[1]) to HH:MM:SS
    formatted_data = []
    for row in data:
        ts = datetime.fromtimestamp (row[1]).strftime ('%H:%M:%S')
        formatted_row = (row [0], ts, row[2], row[3], row[4], row[5])
        formatted_data.append (formatted_row)
    
    return render_template_string (HTML_TEMPLATE, data = formatted_data)

if __name__ == "__main__":
    app.run (host = "0.0.0.0", port=5000, debug=True)