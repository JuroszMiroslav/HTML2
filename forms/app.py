from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="cs">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Formulář GET a POST</title>
    </head>
    <body>
        <h1>Formulář s metodou GET</h1>
        <form action="/search" method="get">
            <label for="query">Hledat:</label>
            <input type="text" id="query" name="query">
            <button type="submit">Odeslat</button>
        </form>
        <h1>Formulář s metodou POST</h1>
        <form action="/submit" method="post">
            <label for="username">Uživatelské jméno:</label>
            <input type="text" id="username" name="username">
            <label for="password">Heslo:</label>
            <input type="password" id="password" name="password">
            <button type="submit">Odeslat</button>
        </form>
    </body>
    </html>
    ''')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    return f'<h1>Odeslaná data GET</h1><pre>{query}</pre>'

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')
    return f'<h1>Odeslaná data POST</h1><pre>Uživatelské jméno: {username}\nHeslo: {password}</pre>'

if __name__ == '__main__':
    app.run(debug=True)
