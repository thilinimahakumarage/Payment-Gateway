from flask import Flask, render_template_string, request

app = Flask(__name__)

html_page = """
<h2>Payment Gateway</h2>

<form method="POST" action="/pay">
    <label>Payment Method:</label>
    <select name="method">
        <option value="Card">Card</option>
        <option value="PayPal">PayPal</option>
        <option value="Bank Transfer">Bank Transfer</option>
    </select>

    <br><br>

    <label>Amount:</label>
    <input type="number" name="amount" required>

    <br><br>

    <button type="submit">Pay Now</button>
</form>

{% if result %}
<h3>{{ result }}</h3>
{% endif %}
"""

@app.route("/")
def home():
    return render_template_string(html_page)

@app.route("/pay", methods=["POST"])
def pay():
    method = request.form["method"]
    amount = request.form["amount"]

    result = f"Payment successful! Amount: £{amount}, Method: {method}"

    return render_template_string(html_page, result=result)

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)