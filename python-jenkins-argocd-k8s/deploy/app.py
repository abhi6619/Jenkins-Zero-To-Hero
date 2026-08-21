from flask import Flask, request, jsonify

app = Flask(__name__)


# HOME PAGE
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Vintage Car Booking</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f2eee8;
                margin: 0;
                padding: 40px;
            }

            .container {
                max-width: 600px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
            }

            h1 {
                color: #5b3924;
                text-align: center;
            }

            label {
                display: block;
                margin-top: 15px;
                font-weight: bold;
            }

            input,
            select {
                width: 100%;
                padding: 12px;
                margin-top: 5px;
                box-sizing: border-box;
                border: 1px solid #ccc;
                border-radius: 5px;
            }

            button {
                width: 100%;
                margin-top: 25px;
                padding: 14px;
                background: #5b3924;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 18px;
                cursor: pointer;
            }

            button:hover {
                background: #3d2618;
            }

            #result {
                margin-top: 20px;
                padding: 15px;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>🚗 Vintage Car Booking</h1>

            <form id="bookingForm">

                <label>Your Name</label>
                <input type="text" id="name" required>

                <label>Email</label>
                <input type="email" id="email" required>

                <label>Phone</label>
                <input type="text" id="phone" required>

                <label>Vintage Car</label>
                <select id="car">
                    <option value="Mustang">Ford Mustang</option>
                    <option value="Beetle">Volkswagen Beetle</option>
                    <option value="Porsche911">Porsche 911</option>
                </select>

                <label>Version / Year</label>
                <select id="version">
                    <option value="1965">1965</option>
                    <option value="1967">1967</option>
                    <option value="1969">1969</option>
                    <option value="1973">1973</option>
                </select>

                <label>Booking Date</label>
                <input type="date" id="booking_date" required>

                <button type="submit">
                    Book Vintage Car
                </button>

            </form>

            <div id="result"></div>

        </div>

        <script>
            document.getElementById("bookingForm").addEventListener(
                "submit",
                async function(event) {

                    event.preventDefault();

                    const data = {
                        name: document.getElementById("name").value,
                        email: document.getElementById("email").value,
                        phone: document.getElementById("phone").value,
                        car: document.getElementById("car").value,
                        version: document.getElementById("version").value,
                        booking_date:
                            document.getElementById("booking_date").value
                    };

                    const result = document.getElementById("result");

                    result.innerHTML = "⏳ Processing booking...";

                    try {

                        const response = await fetch("/book", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify(data)
                        });

                        const answer = await response.json();

                        if (answer.success) {

                            result.innerHTML = `
                                <h3>✅ Booking Successful!</h3>

                                <p>
                                    Booking ID:
                                    <strong>#${answer.booking_id}</strong>
                                </p>

                                <p>
                                    Car:
                                    <strong>${answer.car}</strong>
                                </p>

                                <p>
                                    Version:
                                    <strong>${answer.version}</strong>
                                </p>

                                <p>
                                    Price:
                                    <strong>$${answer.price}</strong>
                                </p>
                            `;

                        } else {

                            result.innerHTML = "❌ " + answer.error;

                        }

                    } catch (error) {

                        result.innerHTML =
                            "❌ Could not connect to server.";

                        console.error(error);
                    }
                }
            );
        </script>

    </body>
    </html>
    """


# BOOKING API
@app.route("/book", methods=["POST"])
def book():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "error": "Invalid JSON data"
        }), 400

    print("\n==============================")
    print("       NEW BOOKING")
    print("==============================")

    print("Name:", data.get("name"))
    print("Email:", data.get("email"))
    print("Phone:", data.get("phone"))
    print("Car:", data.get("car"))
    print("Version:", data.get("version"))
    print("Date:", data.get("booking_date"))

    print("==============================\n")

    return jsonify({
        "success": True,
        "booking_id": 1001,
        "car": data.get("car"),
        "version": data.get("version"),
        "price": 95000
    })


# HEALTH CHECK
@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "status": "running",
        "message": "Vintage Car Booking System is working"
    })


# START SERVER
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
