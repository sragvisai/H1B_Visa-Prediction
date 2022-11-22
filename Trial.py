from fastapi import FastAPI
import pickle
import json
import numpy as np

app = FastAPI()

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

@app.get("/")
async def predict(input_data : str):
    print("Input data ",input_data)
    inputData = input_data.split(",")
    with open('model2.pickle', 'rb') as f:
        model = pickle.load(f)
    with open('encoder2.pickle', 'rb') as f:
        encoder = pickle.load(f)

    # inputData = ['Software Developer','1','1','0','0','0','0','Google LLC','Yes','Yes','120000','Year','100000','Year','10','Yes','Yes','$60,000 or higher annual wage']

    inputData= np.asarray(inputData)
    inputData = inputData.reshape(1,-1)

    inputData = encoder.transform(inputData)
    
    predictedOutcome = model.predict(inputData)
    print("Returning ",predictedOutcome)
    return json.dumps({"outcome" : (str(predictedOutcome[0]))})

def hello():
  return {"Hello world!"}

def firstFunction():
    a = 5
    print("First Function")


if __name__ == "__main__":
    firstFunction()
