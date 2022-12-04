from fastapi import FastAPI
import pickle
import json
import numpy as np
from iso3166 import countries

app = FastAPI()
BLACKLISTEDCOMPANIES = ['Broadgate, Inc.','Spate Business Solutions, LLC','Cloudpoint Systems, Inc','Open Access Technology International, Inc.','Invensys, Inc']

BLACKLISTEDCOUNTRIES = ['Eritrea','Iran','Kyrgyzstan','Libya','Myanmar','Nigeria','North Korea','Somalia','Sudan','Syria',
'Tanzania','Venezuela','Yemen']

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
    inputData = input_data[1:]
    inputData = inputData[:-1]
    inputData = inputData.split(",")
    if len(inputData) == 6:
        if inputData[0]:
            with open('role_names.txt') as myfile:
                if inputData[0] not in myfile.read():
                    return json.dumps({"outcome" : "Denied"})
        if inputData[1]:
            with open('firm_names.txt') as myfile:
                if inputData[1] not in myfile.read():
                    return json.dumps({"outcome" : "Denied"})
        if inputData[1] in BLACKLISTEDCOMPANIES:
            return json.dumps({"outcome" : "Denied-B"})
        if int(inputData[2]) < int(inputData[3]):
            return json.dumps({"outcome" : "Denied-S"})
        if inputData[4] in BLACKLISTEDCOUNTRIES or inputData[4] not in countries:
            return json.dumps({"outcome" : "Denied-C"})
        if inputData[5] != "Yes":
            return json.dumps({"outcome" : "Denied-E"})
        else:
            return json.dumps({"outcome" : "Approved"})

    try:
         
        with open('model2.pickle', 'rb') as f:
            model = pickle.load(f)
        with open('encoder2.pickle', 'rb') as f:
            encoder = pickle.load(f)
        #10 & 12
        if int(inputData[10]) < int(inputData[11]):
            return json.dumps({"outcome" : "Denied-S"})
        # inputData = ['Software Developer','1','1','0','0','0','0','Google LLC','Yes','Yes','120000','Year','100000','Year','10','Yes','Yes','$60,000 or higher annual wage']
        print("Actual Data "+inputData)
        
        inputData= np.asarray(inputData)
        inputData = inputData.reshape(1,-1)

        inputData = encoder.transform(inputData)
        
        print("Reverse Encoding "+encoder.inverse_transform(inputData))

        predictedOutcome = model.predict(inputData)
        #print("Returning ",predictedOutcome)
        return json.dumps({"outcome" : (str("replace"[0]))})
    
    except:
        return json.dumps({"outcome":"ERROR"})

def hello():
  return {"Hello world!"}

def firstFunction():
    a = 5
    print("First Function")


if __name__ == "__main__":
    firstFunction()
