from flask import Flask, request, redirect, render_template
import sqlite3
import string
import random
import os

# Set the template folder explicitly
template_dir = os.path.abspath('./templates')
app = Flask(__name__, template_folder=template_dir)

# Database setup
def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS urls
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  long_url TEXT NOT NULL,
                  short_code TEXT NOT NULL UNIQUE)''')
    conn.commit()
    conn.close()

init_db()

# Generate a random short code
def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        long_url = request.form['url']
        short_code = generate_short_code()
        
        conn = sqlite3.connect('urls.db')
        c = conn.cursor()
        c.execute("INSERT INTO urls (long_url, short_code) VALUES (?, ?)",
                  (long_url, short_code))
        conn.commit()
        conn.close()
        
        short_url = request.host_url + short_code
        return render_template('result.html', short_url=short_url)
    return render_template('home.html')

# Redirection
@app.route('/<short_code>')
def redirect_to_url(short_code):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    result = c.execute("SELECT long_url FROM urls WHERE short_code = ?", (short_code,)).fetchone()
    conn.close()
    
    if result:
        long_url = result[0]
        return redirect(long_url)
    else:
        return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)