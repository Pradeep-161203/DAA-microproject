from flask import Flask, request
app = Flask(__name__)
def compute_gcd(a, b):
    if b == 0:
        return a
    return compute_gcd(b, a % b)
def compute_lcm(m, n):
    gcd = compute_gcd(m, n)
    return (m * n) // gcd
@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        try:
            m = int(request.form['m'])
            n = int(request.form['n'])
            if m <= 0 or n <= 0:
                result = "Please enter positive integers only."
            else:
                gcd = compute_gcd(m, n)
                lcm = compute_lcm(m, n)
                result = f"GCD of {m} and {n} is: {gcd}<br>LCM of {m} and {n} is: {lcm}"
        except ValueError:
            result = "Invalid input. Please enter numbers." 
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>LCM Calculator</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                padding: 20px;
                background: #f0f4f8;
            }}
            .container {{
                max-width: 400px;
                margin: auto;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px #ccc;
            }}
            h2 {{
                text-align: center;
                color: #333;
            }}
            input, button {{
                width: 100%;
                padding: 10px;
                margin: 10px 0;
            }}
            #result {{
                margin-top: 20px;
                font-weight: bold;
                color: #006400;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>LCM Calculator</h2>
            <form method="post">
                <label>Enter first positive integer (m):</label>
                <input type="number" name="m" min="1" required>
                <label>Enter second positive integer (n):</label>
                <input type="number" name="n" min="1" required>
                <button type="submit">Compute LCM</button>
            </form>
            <div id="result">{result}</div>
        </div>
    </body>
    </html>
    """
if __name__ == '__main__':
    app.run(debug=True)
