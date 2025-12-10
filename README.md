# Forest Cover Type Prediction

This project predicts the forest cover type (the predominant kind of tree cover) for a given location based on cartographic variables. It includes a machine learning model trained on cartographic data and a Streamlit web application for interactive predictions.

## 📌 Project Overview

The goal of this project is to classify forest cover types using geological and topographical features. The project consists of:

  * **Data Analysis & Modeling:** A Jupyter Notebook (`Forest_cover.ipynb`) that explores the dataset, trains multiple models (Logistic Regression, Decision Tree, Random Forest), and saves the best-performing model.
  * **Web Application:** A Streamlit app (`app.py`) that allows users to input feature values and receive a predicted forest cover type along with a visual representation.

## 📂 Project Structure

  * `Forest_cover.ipynb`: Jupyter Notebook containing data preprocessing, model training, evaluation, and serialization.
  * `app.py`: The main Streamlit application file for the user interface.
  * `rfc.pkl`: The trained Random Forest Classifier model (saved using pickle).
  * `requirements.txt`: List of Python dependencies required to run the project.
  * `train.csv`: The training dataset used for model building.
  * `img_[1-7].png`: Images representing the different forest cover types, displayed in the app upon prediction.

## 🌲 Forest Cover Types

The model predicts one of the following 7 cover types:

1.  **Spruce/Fir**
2.  **Lodgepole Pine**
3.  **Ponderosa Pine**
4.  **Cottonwood/Willow**
5.  **Aspen**
6.  **Douglas-fir**
7.  **Pine**

## ⚙️ Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2.  **Install dependencies:**
    It is recommended to use a virtual environment. Install the required packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

### Running the Web App

To start the Streamlit application:

```bash
streamlit run app.py
```

Once running, the app will open in your browser. You can enter the comma-separated feature values to get a prediction.

use the app here : [Forest Cover Type Prediction App](https://shounak-max-forest-cover-type-prediction-app-ozcxcy.streamlit.app/)

### Retraining the Model

If you wish to retrain the model or explore the data:

1.  Open `Forest_cover.ipynb` in Jupyter Notebook or JupyterLab.
2.  Run the cells to process `train.csv` and train the models.
3.  The notebook evaluates **Logistic Regression**, **Decision Trees**, and **Random Forests**.
4.  The final Random Forest model is saved as `rfc.pkl`.

## 📊 Model Details

The project uses a **Random Forest Classifier** which achieved an accuracy of approximately **81%** on the test set.

**Features used for prediction include:**

  * Elevation
  * Aspect
  * Slope
  * Horizontal & Vertical Distances to Hydrology
  * Horizontal Distance to Roadways & Fire Points
  * Hillshade measures (9am, Noon, 3pm)
  * Wilderness Areas (4 binary columns)
  * Soil Types (40 binary columns)