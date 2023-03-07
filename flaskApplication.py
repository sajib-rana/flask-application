from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def calculator():
    return render_template("calculator.html")

@app.route("/", methods=["POST"])
def calculate():
    num1 = request.form.get("num1")
    num2 = request.form.get("num2")
    operator = request.form.get("operator")
    result = None
    
    if operator == "+":
        result = int(num1) + int(num2)
    elif operator == "-":
        result = int(num1) - int(num2)
    elif operator == "*":
        result = int(num1) * int(num2)
    elif operator == "/":
        result = int(num1) / int(num2)
        
    return render_template("calculator.html", result=result)
    
if __name__ == '__main__':
    app.run(debug=True)