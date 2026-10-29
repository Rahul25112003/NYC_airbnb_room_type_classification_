from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel, Field
import joblib
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

COLUMNS= ['latitude', 'longitude', 'price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month', 
          'calculated_host_listings_count', 'availability_365', 'neighbourhood_group', 'neighbourhood'    ]


model =joblib.load("Model_Pipeline.pkl")  # Load the trained model pipeline 

#pydantic model = the input validation 
class Features(BaseModel):
    latitude: float = Field(..., ge=-90, le=90, description="Latitude must be between -90 and 90")
    longitude: float = Field(..., ge=-180, le=180, description="Longitude must be between -180 and 180")
    price: float = Field(..., gt=0, description="Price must be greater than 0")
    minimum_nights: int = Field(..., ge=1, description="Minimum nights must be at least 1")
    number_of_reviews: int = Field(..., ge=0, description="Number of reviews must be non-negative")
    reviews_per_month: float = Field(..., ge=0, description="Reviews per month must be non-negative")
    calculated_host_listings_count: int = Field(..., ge=0, description="Calculated host listings count must be non-negative")
    availability_365: int = Field(..., ge=0, le=365, description="Availability must be between 0 and 365")
    neighbourhood_group: str = Field(..., min_length=1, description="Neighbourhood group must be a string")
    neighbourhood: str = Field(..., min_length=1, description="Neighbourhood must be a string")

@app.get('/')
def greet():
    return "Hello Guys!!"

@app.get('/predict')
def predict(features):
    row = pd.DataFrame([features.dict()], columns=COLUMNS, index=[0])
    prediction = model.predict(row)
    probability = model.predict_proba(row)
    return {"prediction": prediction[0],
            "probability": probability.tolist()}

