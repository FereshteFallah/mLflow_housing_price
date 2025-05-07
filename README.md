
# Housing Price Prediction - XGBoost Model

This project is a housing price prediction model using the XGBoost algorithm. It allows you to predict the price of houses in California based on various features such as area, number of rooms, etc.

## Installation and Setup

### Prerequisites:
To set up the project, you will need the following tools and packages:

- Python 3.6 or higher
- Django 5.2
- XGBoost
- NumPy
- Other required libraries

### Installing Packages:
To install all the necessary packages, use the following command in the project directory:

```bash
pip install -r requirements.txt
```

### Running the Project:
To run the local server and test housing price prediction, use the following command:
```bash
python manage.py runserver
```
Then, go to the URL http://127.0.0.1:8000 to view the prediction form.

### URLs:
- /predict/ : For submitting housing features and receiving the predicted price.
- /admin/ : To access the Django admin panel.

### Usage:

- Go to the /predict/ page.
- Enter the housing features (such as area, number of rooms, etc.).
- After submitting the form, the predicted housing price will be displayed.
### Model Loading:

The XGBoost model is located in the api folder and is loaded using the path specified in the code.

### Using MLflow:

In this project, MLflow is used for model management and tracking. This tool allows us to:

- Save and evaluate different models.
- Track parameters and results.
- Load and use trained models in the future.
### Steps to Use MLflow:
- 1-  __Install MLflow:__
```bash
pip install mlflow
```
- 2- __Log Models with MLflow:__
During model training, MLflow is used to log parameters and results. After training, models are saved using __mlflow.log_model()__.
- 3- __Load Models:__
The XGBoost model saved in xgboost_model.json is loaded using MLflow. It is located in the api folder.
- 4- __Experiment Management with MLflow:__
MLflow allows us to compare different experiments and models, helping us select the best one for predictions.
### Conclusion:

In this project, the XGBoost algorithm is used for prediction, and MLflow is utilized for managing models and experiments to get more accurate results. This model can be used to predict housing prices based on various housing features, such as area, number of rooms, and other attributes.

