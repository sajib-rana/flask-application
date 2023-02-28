from flask import Flask
app = Flask(__name__)

@app.route('/math')
def math():
    operations = ['add', 'subtract', 'multiply', 'divide', 'modulus']
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    results = []
    for op in operations:
        if op == 'add':
            result = a + b
        elif op == 'subtract':
            result = a - b
        elif op == 'multiply':
            result = a * b
        elif op == 'divide':
            result = a / b
        elif op == 'modulus':
            result = a % b
        else:
            result = None
        results.append((op, result))
    return str(results)
    
if __name__ == '__main__':
    app.run(debug=True)