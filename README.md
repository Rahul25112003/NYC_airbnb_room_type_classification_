# NYC_airbnb_room_type_classification_


Machine Learning | Python | Scikit-learn | FastAPI

Project Overview

This project uses Machine Learning classification techniques to predict Airbnb room types in New York City based on listing characteristics. It analyzes property location, pricing, minimum stay requirements, availability, customer reviews, and host activity to classify listings into three categories:

- Entire Home/Apt
- Private Room
- Shared Room

The objective is to explore how listing characteristics and location-related factors relate to room-type categories and build a practical predictive analytics solution.

Live Application

🌐 Try the Application:
https://nyc-airbnb-room-type-classification-1-r492.onrender.com

📂 GitHub Repository:
https://github.com/Rahul25112003/NYC_airbnb_room_type_classification_

Key Features

- Predicts Airbnb room categories using a trained Machine Learning pipeline.
- Uses location, pricing, reviews, availability, and host-related features.
- Supports three-class room-type classification.
- Provides prediction probabilities alongside the predicted category.
- Offers an interactive interface for entering listing details and viewing predictions.

Dataset & Input Features

The model uses 10 input features:

Category| Features
Location| Latitude, Longitude, Borough, Neighbourhood
Pricing| Price per night
Stay Requirements| Minimum nights
Reviews| Total reviews, Reviews per month
Host Activity| Host listing count
Availability| Days available per year

Technology Stack

- Programming: Python
- Data Processing: Pandas
- Machine Learning: Scikit-learn, Imbalanced-learn
- Model Management: Joblib
- Backend: FastAPI
- Input Validation: Pydantic
- Deployment: Render

Project Workflow

1. Data Understanding: Explore Airbnb listing characteristics and relevant variables.
2. Data Preprocessing: Prepare numerical and categorical features for model development.
3. Model Development: Build a classification pipeline to predict room categories.
4. Model Evaluation: Assess classification performance and prediction reliability.
5. Deployment: Integrate the trained model into a prediction application.

Repository Structure

NYC_airbnb_room_type_classification_/
│
├── Main.py
├── Model_Pipeline.pkl
├── requirements.txt
├── runtime.txt
├── index.html
├── script.js
├── style.css
└── README.md

Run Locally

1. Clone the repository

git clone https://github.com/Rahul25112003/NYC_airbnb_room_type_classification_.git

2. Navigate to the project directory

cd NYC_airbnb_room_type_classification_

3. Install dependencies

pip install -r requirements.txt

4. Start the application

uvicorn Main:app --reload

Project Outcome

The project demonstrates the practical application of Machine Learning classification to real-world accommodation listing data. It combines data-driven analysis, predictive modelling, and model deployment to transform listing attributes into actionable classification results.

Author

Rahul Maji

GitHub: https://github.com/Rahul25112003

---

This project is developed for educational and practical learning purposes.
