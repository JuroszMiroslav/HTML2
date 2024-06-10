from flask import Flask, request

app = Flask(__name__)

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
