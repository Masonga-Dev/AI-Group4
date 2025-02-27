from bottle import Bottle, request, template, static_file, run

app = Bottle()

def recommend_crop(temperature, rainfall, soil_type, altitude):
    recommendations = []

    # Temperature-based recommendations
    if 20 <= temperature <= 30:
        recommendations.append("Maize")
    if 15 <= temperature <= 25:
        recommendations.append("Potatoes")
    if temperature > 30:
        recommendations.append("Sorghum")

    # Rainfall-based recommendations
    if 600 <= rainfall <= 1200:
        recommendations.append("Beans")
    if rainfall > 1200:
        recommendations.append("Rice")
    if rainfall < 600:
        recommendations.append("Millet")

    # Soil Type-based recommendations
    if soil_type.lower() == "loamy":
        recommendations.append("Vegetables")
    elif soil_type.lower() == "clayey":
        recommendations.append("Wheat")
    elif soil_type.lower() == "sandy":
        recommendations.append("Cassava")

    # Altitude-based recommendations
    if altitude > 2000:
        recommendations.append("Pyrethrum")
    elif 1000 <= altitude <= 2000:
        recommendations.append("Coffee")
    elif altitude < 1000:
        recommendations.append("Bananas")
    
    return recommendations if recommendations else ["No suitable crop found"]

@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

@app.route('/')
def index():
    return template('index.html')

@app.route('/', method='POST')
def process_form():
    try:
        temperature = float(request.forms.get('temperature'))
        rainfall = float(request.forms.get('rainfall'))
        soil_type = request.forms.get('soil_type')
        altitude = float(request.forms.get('altitude'))
        recommendations = recommend_crop(temperature, rainfall, soil_type, altitude)
        return template('index.html', recommendations=recommendations)
    except ValueError:
        return template('index.html', error="Please enter valid numeric values.")

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=5000, debug=True)

