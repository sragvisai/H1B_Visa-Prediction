from fastapi import FastAPI
import pickle
import json
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
import pickle_compat

app = FastAPI()
pickle_compat.patch()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/my-first-api")
def apiFunction():
    a = 10
    return {a}

@app.get("/getBlackListedCountries")
def returnCountries():
    blackListedCountries = ['Eritrea','Iran','Kyrgyzstan','Libya','Myanmar','Nigeria','North Korea','Somalia','Sudan','Syria',
                         'Tanzania','Venezuela','Yemen']
    return {blackListedCountries}

@app.get("/getBlackListedCompanies")
def returnCompanies():
    blackListedCompanies =  ['Broadgate, Inc.','Spate Business Solutions, LLC','Cloudpoint Systems, Inc','Open Access Technology International, Inc.','Invensys, Inc']
    return {blackListedCompanies}

@app.post("/")
async def predict(input_data : str):
    print("Input data ",input_data)
    input_data = input_data.split(",")
    with open('model2.pickle', 'rb') as f:
        model = pickle.load(f)
    with open('encoder2.pickle', 'rb') as f:
        encoder = pickle.load(f)

    inputData = ['Software Developer','1','1','0','0','0','0','Google LLC','Yes','Yes','120000','Year','100000','Year','10','Yes','Yes'
            ,'$60,000 or higher annual wage']
    inputData= np.asarray(inputData)
    inputData = inputData.reshape(1,-1)
    print("Here  ",inputData)
    inputData = encoder.transform(inputData)
    print("Predicted ",model.predict(inputData))
    predictedOutcome = model.predic(inputData)
    return predictedOutcome

def hello():
  return {"Hello world!"}

def firstFunction():
    a = 5
    print("First Function")


if __name__ == "__main__":
    firstFunction()
     # Load model
    encoder = OrdinalEncoder()
    #print(encoder.feature_names_in_)
    # with open('pickel.model', 'rb') as f:
    #     model = pickle.load(f)

    with open('encoder2.pickle', 'rb') as f:
        encoder = pickle.load(f)

    print(len(encoder.categories_))
    inputData = ['Software Developer','1','1','0','0','0','0','Google LLC','Yes','Yes','120000','Year','100000','Year','10','Yes','Yes','$60,000 or higher annual wage']
    inputData= np.asarray(inputData)
    inputData = inputData.reshape(1,-1)
    print(inputData)
    inputData = encoder.transform(inputData)
    print(encoder.inverse_transform(inputData)[0])
    
    # print("Model " +model)
    # print("Encode "+encoder)
