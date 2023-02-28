from flask import Flask
app = Flask(__name__)

@app.route('/math')
def math():
    operations = ['add', 'subtract', 'multiply', 'divide', 'modulus']
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

if __name__ == '__main__':
    app.run(debug=True)