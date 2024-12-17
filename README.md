
# Know Your Drug

This project utilizes machine learning to predict diseases based on user-inputted symptoms and provides personalized recommendations for medications, diets, and workouts. It is built using a Kaggle dataset for training the models.

## Project Structure

- **kaggle_dataset**: Includes CSV files with data on diseases, symptoms, training sets, recommended diets, medications, precautions, and workouts.
- **model**: Contains the trained Random Forest model (`RandomForest.pkl`) used for disease prediction.
- **templates**: Frontend HTML template (`index.html`).
- **static**: Frontend images (`img1.jpg`, `img.png`).
- **Project Files**:
  - `app.py`: Main entry point for the Flask web application.
  - `disease_prediction_system.ipynb`: Jupyter Notebook for data preprocessing and model training.


## How to Run
1. Install the necessary dependencies:
   ```bash
   pip install pandas scikit-learn flask ast numpy fuzzywuzzy pickle
   ```
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. Open the web interface at `http://localhost:5000`.

