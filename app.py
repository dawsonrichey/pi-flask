from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')