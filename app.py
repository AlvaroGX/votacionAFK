from flask import Flask, request
import joblib

app = Flask(__name__)
model = joblib.load("modelo_voto.pkl")

HTML = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Predicción de Voto</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: #1a1a2e;
            color: #eee;
            font-family: 'Segoe UI', sans-serif;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card {
            background: #16213e;
            padding: 3rem 2rem;
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.5);
            text-align: center;
            max-width: 400px;
            width: 90%;
        }
        h1 { font-size: 1.8rem; margin-bottom: 1.5rem; color: #e94560; }
        input {
            width: 100%;
            padding: 12px;
            border: none;
            border-radius: 10px;
            font-size: 1.1rem;
            text-align: center;
            background: #0f3460;
            color: #eee;
            outline: none;
        }
        button {
            margin-top: 1rem;
            padding: 12px 40px;
            border: none;
            border-radius: 10px;
            background: #e94560;
            color: #fff;
            font-size: 1.1rem;
            cursor: pointer;
            transition: background 0.3s;
        }
        button:hover { background: #c73650; }
        .result {
            margin-top: 1.5rem;
            font-size: 1.4rem;
            font-weight: bold;
            min-height: 3rem;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🗳️ Predicción de Voto</h1>
        <form method="POST">
            <input type="number" name="edad" placeholder="Ingresa tu edad" min="0" required>
            <button type="submit">Consultar</button>
        </form>
        <div class="result">{{ mensaje|safe }}</div>
    </div>
</body>
</html>"""

@app.route("/", methods=["GET", "POST"])
def index():
    mensaje = ""
    if request.method == "POST":
        try:
            edad = int(request.form["edad"])
            pred = model.predict([[edad]])[0]
            if pred == 1:
                mensaje = "✅ Puedes votar"
            else:
                mensaje = "❌ No puedes votar aún"
        except:
            mensaje = "⚠️ Ingresa una edad válida"
    return HTML.replace("{{ mensaje|safe }}", mensaje)

if __name__ == "__main__":
    app.run(debug=True)
