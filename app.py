from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Hardcoded full name
    full_name = "Manoj Solapure"

    # Corrected: Server time in IST (Asia/Kolkata)
    try:
        ist = pytz.timezone('Asia/Kolkata')
        server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    except Exception as e:
        server_time = f"Error fetching time: {e}"

    # HTML template (Removed 'top' command output)
    html_content = f"""
    <html>
    <head><title>htop</title></head>
    <body>
        <h1>Name: {full_name}</h1>
        <h2>User: {full_name}</h2> <!-- Replaced username with "Manoj Solapure" -->
        <h3>Server Time (IST): {server_time}</h3>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
