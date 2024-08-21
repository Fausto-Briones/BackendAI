from flask import request, jsonify, render_template
from .models import Model
import pandas as pd
from .connectionAdapter import ConnectionAdapter

def register_routes(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/predict', methods=['POST'])
    def predict():
        try:
            data = request.json['input']
            df_input = pd.DataFrame(data)
            connection = ConnectionAdapter()
            model_input = connection.preprocess_validation_data(df_input)
            model = Model()

            predictions = []
            for _, row in model_input.iterrows():
                prediction = model.predict(row.to_frame().T)
                predictions.extend(prediction.tolist())
            
            return jsonify({'output': predictions})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/data', methods=['GET'])
    def get_data():
        data = pd.read_csv('data/database.csv')
        result = data.to_dict(orient='records')
        return jsonify(result)
