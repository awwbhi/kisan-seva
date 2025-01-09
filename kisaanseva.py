from flask import Flask, request, jsonify

app = Flask(__name__)

class KisaanSeva:
    def __init__(self):
        self.soil_types = {
            'black': {
                'characteristics': ['dark colored', 'deep cracks when dry', 'sticky when wet', 'retains moisture'],
                'crops': ['cotton', 'sugarcane', 'wheat', 'groundnut', 'pulses'],
                'states': ['Maharashtra', 'Gujarat', 'Madhya Pradesh']
            },
            'alluvial': {
                'characteristics': ['light colored', 'fertile', 'plain areas', 'river deposits'],
                'crops': ['rice', 'wheat', 'sugarcane', 'maize', 'vegetables'],
                'states': ['Punjab', 'Haryana', 'Uttar Pradesh', 'Bihar', 'West Bengal']
            },
            'red': {
                'characteristics': ['reddish color', 'sandy texture', 'low water retention', 'poor fertility'],
                'crops': ['millets', 'groundnut', 'potato', 'oilseeds', 'pulses'],
                'states': ['Tamil Nadu', 'Karnataka', 'Andhra Pradesh', 'Telangana']
            },
            'laterite': {
                'characteristics': ['rich in iron', 'acidic', 'poor fertility', 'heavy rainfall areas'],
                'crops': ['rubber', 'coffee', 'coconut', 'cashew', 'tea'],
                'states': ['Kerala', 'Karnataka', 'Tamil Nadu', 'Maharashtra', 'Odisha']
            }
        }

    def identify_soil(self, color, texture, water_retention, state):
        if color == '1' and texture == '1' and water_retention == '1':
            return 'black'
        elif color == '2' and texture == '2' and water_retention == '2':
            return 'alluvial'
        elif color == '3' and texture == '3' and water_retention == '3':
            return 'red'
        elif color == '4' and texture == '4' and water_retention == '4':
            return 'laterite'

        for soil_type, data in self.soil_types.items():
            if state in data['states']:
                return soil_type
        
        return 'alluvial'

kisaan_seva = KisaanSeva()

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    state = data.get('state', '').title()
    color = data.get('color')
    texture = data.get('texture')
    water_retention = data.get('water_retention')

    soil_type = kisaan_seva.identify_soil(color, texture, water_retention, state)
    recommendations = {
        "soil_type": soil_type,
        "characteristics": kisaan_seva.soil_types[soil_type]['characteristics'],
        "crops": kisaan_seva.soil_types[soil_type]['crops'],
        "states": kisaan_seva.soil_types[soil_type]['states']
    }
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
