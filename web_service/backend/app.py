from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
import numpy as np

# Chargement du modèle
with open("best_xgb_model_top12.pkl", "rb") as f:
    model = pickle.load(f)

# Liste des features dans l'ordre exact attendu par le modèle
all_features = [
    'Weight', 'Type of Diet_5', 'Gender', 'Iron (mg)', 'Type of Diet_4',
    'Vitamin B7 (µg)', 'omega 3', 'Protein (%)', 'Height', 'wit. B1 - Tiamina',
    'BMI_Category', 'Vitamin B3 (mg)', 'Vitamin E (mg)', 'Cholesterol (mg/day)',
    'Omega 6 (g)', 'Age', 'Number of Meals per Day', 'Type of Diet_1',
    'Age_Category', 'Sodium (mg)', 'Type of Diet_3', 'Cholesterol LDL_y',
    'Dietary Fiber (g)', 'Type of Diet_6', 'Vitamin B12 (µg)', 'Potassium (mg)',
    'Physical Activity', 'Vitamin K (µg)', 'Vitamin C (mg)', 'Iodine (µg)',
    'Vitamin A (µg)', 'Carbohydrate_Fat_Ratio', 'Calcium (mg)', 'Phosphorus (mg)',
    'Magnesium (mg)', 'Height_m', 'Vitamin B6 (mg)', 'Type of Diet_2',
    'Cholesterol LDL_x', 'Fat (%)', 'Carbohydrates (%)', 'wit. B2 - Riboflavin',
    'Vitamin B5 (mg)', 'Copper (mg)', 'Zinc (mg)', 'Vitamin D (µg)', 'BMI',
    'Protein_Fat_Ratio', 'Selenium (µg)', 'Manganese (mg)'
]

# Valeurs par défaut pour les features manquantes
default_values = {
    'Weight': 70,
    'Type of Diet_5': 0,
    'Gender': 1,
    'Iron (mg)': 15,
    'Type of Diet_4': 0,
    'Vitamin B7 (µg)': 30,
    'omega 3': 1.6,
    'Protein (%)': 20,
    'Height': 170,
    'wit. B1 - Tiamina': 1.2,
    'BMI_Category': 2,
    'Vitamin B3 (mg)': 16,
    'Vitamin E (mg)': 15,
    'Cholesterol (mg/day)': 300,
    'Omega 6 (g)': 17,
    'Age': 35,
    'Number of Meals per Day': 3,
    'Type of Diet_1': 0,
    'Age_Category': 2,
    'Sodium (mg)': 2300,
    'Type of Diet_3': 0,
    'Cholesterol LDL_y': 100,
    'Dietary Fiber (g)': 25,
    'Type of Diet_6': 0,
    'Vitamin B12 (µg)': 2.4,
    'Potassium (mg)': 3500,
    'Physical Activity': 2,
    'Vitamin K (µg)': 120,
    'Vitamin C (mg)': 90,
    'Iodine (µg)': 150,
    'Vitamin A (µg)': 900,
    'Carbohydrate_Fat_Ratio': 1.5,
    'Calcium (mg)': 1000,
    'Phosphorus (mg)': 700,
    'Magnesium (mg)': 400,
    'Height_m': 1.7,
    'Vitamin B6 (mg)': 1.7,
    'Type of Diet_2': 0
}

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        print("Données reçues:", data)  # Debug log
        
        # Créer un dictionnaire avec les valeurs par défaut
        input_data = default_values.copy()
        
        # Mettre à jour avec les valeurs reçues
        for key, value in data.items():
            input_data[key] = value
        
        # Créer le DataFrame dans le bon ordre des colonnes
        input_df = pd.DataFrame([input_data], columns=all_features)
        print("Features dans le DataFrame:", input_df.columns.tolist())  # Debug log
        
        # Prédiction
        prediction = int(model.predict(input_df)[0])
        confidence = float(model.predict_proba(input_df)[0].max())
        
        return jsonify({
            "prediction": prediction,
            "confidence": round(confidence, 4)
        })
        
    except Exception as e:
        print(f"Erreur lors de la prédiction: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
