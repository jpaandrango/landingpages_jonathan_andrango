from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

# Plantilla HTML con diseño moderno (CSS integrado) y lógica de reloj (JavaScript)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page - Reloj en Vivo</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&family=Orbitron:wght@500;700&display=swap" rel="stylesheet">
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Montserrat', sans-serif;
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: #ffffff;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }

        .container {
            text-align: center;
            backdrop-filter: blur(10px);
            background: rgba(255, 255, 255, 0.05);
            padding: 3rem 5rem;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
            animation: fadeIn 1.5s ease-in-out;
        }

        h1 {
            font-size: 1.5rem;
            text-transform: uppercase;
            letter-spacing: 4px;
            margin-bottom: 1.5rem;
            color: #00f2fe;
            font-weight: 300;
        }

        .clock {
            font-family: 'Orbitron', sans-serif;
            font-size: 5rem;
            letter-spacing: 2px;
            color: #fff;
            text-shadow: 0 0 20px rgba(0, 242, 254, 0.6);
            margin-bottom: 1rem;
        }

        .date {
            font-size: 1.3rem;
            font-weight: 400;
            color: #a5b1c2;
            letter-spacing: 2px;
        }

        .footer {
            margin-top: 3rem;
            font-size: 0.8rem;
            color: rgba(255, 255, 255, 0.3);
            letter-spacing: 1px;
        }

        /* Animación de entrada */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Ajustes para pantallas pequeñas */
        @media (max-width: 600px) {
            .container { padding: 2rem; width: 90%; }
            .clock { font-size: 3rem; }
            .date { font-size: 1rem; }
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Tiempo Real</h1>
        <div class="clock" id="live-clock">00:00:00</div>
        <div class="date" id="live-date">Cargando fecha...</div>
        <div class="footer">Dashboard Ejecutivo &copy; 2026</div>
    </div>

    <script>
        function updateTime() {
            const now = new Date();
            
            // Formatear la hora (HH:MM:SS)
            let hours = String(now.getHours()).padStart(2, '0');
            let minutes = String(now.getMinutes()).padStart(2, '0');
            let seconds = String(now.getSeconds()).padStart(2, '0');
            
            document.getElementById('live-clock').textContent = `${hours}:${minutes}:${seconds}`;
            
            // Formatear la fecha en español
            const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
            let dateString = now.toLocaleDateString('es-ES', options);
            
            // Capitalizar la primera letra del día
            dateString = dateString.charAt(0).toUpperCase() + dateString.slice(1);
            
            document.getElementById('live-date').textContent = dateString;
        }

        // Ejecutar inmediatamente y luego cada segundo
        updateTime();
        setInterval(updateTime, 1000);
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    # Forzamos explícitamente el puerto 5000
    app.run(debug=True, port=5000)