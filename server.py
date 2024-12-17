# from flask import Flask, request, jsonify, render_template
# import joblib
# import pandas as pd
# import logging
# from fuzzywuzzy import process

# # Initialize Flask app
# app = Flask(__name__)

# # Configure logging
# logging.basicConfig(level=logging.INFO)

# # Load the list of symptoms from a CSV file
# try:
#     symptoms_df = pd.read_csv("symptoms_df.csv")  # Replace with your CSV filename
#     symptom_columns = ['Symptom_1', 'Symptom_2', 'Symptom_3', 'Symptom_4']  # List all symptom columns
#     symptom_list = pd.concat([symptoms_df[col] for col in symptom_columns]).unique().tolist()
#     logging.info("Symptom list loaded successfully.")
# except Exception as e:
#     logging.error(f"Error loading symptom list: {e}")
#     symptom_list = []

# # Load the trained machine learning model
# try:
#     model = joblib.load("RandomForest.pkl")  # Replace with your model filename
#     logging.info("Trained model loaded successfully.")
# except Exception as e:
#     logging.error(f"Error loading model: {e}")
#     model = None

# # Function to correct symptoms using fuzzy matching
# def correct_symptom(symptom, threshold=80):
#     match, score = process.extractOne(symptom, symptom_list)
#     if score >= threshold:
#         return match
#     return None

# # Define home route
# @app.route("/")
# def home():
#     return render_template("index.html")  # Ensure `index.html` exists in the templates folder

# # Define prediction route
# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         # Parse request data
#         data = request.get_json()  # Ensure the request content type is 'application/json'
        
#         if not data:
#             return jsonify({"error": "No data provided."}), 400
        
#         symptoms = data.get("symptoms", [])
        
#         if not symptoms:
#             return jsonify({"error": "No symptoms provided."}), 400

#         # Validate symptoms
#         corrected_symptoms = []
#         for symptom in symptoms:
#             corrected = correct_symptom(symptom)
#             if corrected:
#                 corrected_symptoms.append(corrected)
#             else:
#                 return jsonify({"error": f"Symptom '{symptom}' not recognized."}), 400

#         # Prediction logic
#         if model:
#             prediction = model.predict([corrected_symptoms])  # Update if input format differs
#             return jsonify({"prediction": prediction.tolist()})
#         else:
#             return jsonify({"error": "Model not available."}), 500
#     except Exception as e:
#         logging.error(f"Error during prediction: {e}")
#         return jsonify({"error": "Internal server error", "details": str(e)}), 500

# # Run the Flask app
# if __name__ == "__main__":
#     app.run(debug=True)
