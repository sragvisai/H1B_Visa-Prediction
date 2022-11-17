import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve
import io

path = "C:/Users/nsrag/OneDrive/Desktop/UMBC/SEM3/SOC/TEAM_B_data606-main/TEAM_B_data606-main/Machine Learning"

h1b_2021Q4 = pd.DataFrame(pd.read_excel(path+"/LCA_Disclosure_Data_FY2021_Q4.xlsx"))
h1b_2021Q3 = pd.DataFrame(pd.read_excel(path+"/LCA_Disclosure_Data_FY2021_Q3.xlsx"))
h1b_2021Q2 = pd.DataFrame(pd.read_excel(path+"/LCA_Disclosure_Data_FY2021_Q2.xlsx"))
h1b_2021Q1 = pd.DataFrame(pd.read_excel(path+"/LCA_Disclosure_Data_FY2021_Q1.xlsx"))


sensitiveData = ['RECEIVED_DATE','SOC_CODE','BEGIN_DATE', 'END_DATE','EMPLOYER_ADDRESS1', 'EMPLOYER_ADDRESS2',
       'EMPLOYER_CITY','EMPLOYER_STATE', 'EMPLOYER_POSTAL_CODE',
       'EMPLOYER_COUNTRY', 'EMPLOYER_PROVINCE', 'EMPLOYER_PHONE',
       'EMPLOYER_PHONE_EXT', 'NAICS_CODE', 'EMPLOYER_POC_LAST_NAME',
       'EMPLOYER_POC_FIRST_NAME', 'EMPLOYER_POC_MIDDLE_NAME',
       'EMPLOYER_POC_JOB_TITLE', 'EMPLOYER_POC_ADDRESS1',
       'EMPLOYER_POC_ADDRESS2', 'EMPLOYER_POC_CITY', 'EMPLOYER_POC_STATE',
       'EMPLOYER_POC_POSTAL_CODE', 'EMPLOYER_POC_COUNTRY',
       'EMPLOYER_POC_PROVINCE', 'EMPLOYER_POC_PHONE', 'EMPLOYER_POC_PHONE_EXT',
       'EMPLOYER_POC_EMAIL','AGENT_ATTORNEY_LAST_NAME', 'AGENT_ATTORNEY_FIRST_NAME',
       'AGENT_ATTORNEY_MIDDLE_NAME', 'AGENT_ATTORNEY_ADDRESS1',
       'AGENT_ATTORNEY_ADDRESS2', 'AGENT_ATTORNEY_CITY',
       'AGENT_ATTORNEY_STATE', 'AGENT_ATTORNEY_POSTAL_CODE',
       'AGENT_ATTORNEY_COUNTRY', 'AGENT_ATTORNEY_PROVINCE',
       'AGENT_ATTORNEY_PHONE', 'AGENT_ATTORNEY_PHONE_EXT',
       'AGENT_ATTORNEY_EMAIL_ADDRESS', 'LAWFIRM_NAME_BUSINESS_NAME',
       'STATE_OF_HIGHEST_COURT', 'NAME_OF_HIGHEST_STATE_COURT','SECONDARY_ENTITY_BUSINESS_NAME', 'WORKSITE_ADDRESS1',
       'WORKSITE_ADDRESS2', 'WORKSITE_CITY', 'WORKSITE_COUNTY',
       'WORKSITE_STATE', 'WORKSITE_POSTAL_CODE','PW_TRACKING_NUMBER',  'PW_OES_YEAR', 'PREPARER_LAST_NAME',
       'PREPARER_FIRST_NAME', 'PREPARER_MIDDLE_INITIAL',
       'PREPARER_BUSINESS_NAME', 'PREPARER_EMAIL' ]


h1b_2021Q4.drop(sensitiveData,inplace=True,axis=1)
h1b_2021Q3.drop(sensitiveData,inplace=True,axis=1,errors = 'ignore')
h1b_2021Q2.drop(sensitiveData,inplace=True,axis=1,errors = 'ignore')
h1b_2021Q1.drop(sensitiveData,inplace=True,axis=1,errors = 'ignore')


colsWithNoImpact = ['APPENDIX_A_ATTACHED','EMPLOYER_POC_ADDRESS_2','PW_SURVEY_PUBLISHER','TRADE_NAME_DBA','PW_SURVEY_NAME','ORIGINAL_CERT_DATE',
                    'PUBLIC_DISCLOSURE','PW_OTHER_SOURCE','PW_OTHER_YEAR','WAGE_RATE_OF_PAY_TO','PW_WAGE_LEVEL','WAGE_RATE_OF_PAY_TO','WORKSITE_WORKERS','EMPLOYER_POC_ADDRESS_1']
h1b_2021Q3.drop(colsWithNoImpact,axis = 1, inplace = True , errors = 'ignore')
h1b_2021Q2.drop(colsWithNoImpact,axis = 1, inplace = True , errors = 'ignore')
h1b_2021Q1.drop(colsWithNoImpact,axis = 1, inplace = True , errors = 'ignore')
h1b_2021Q4.drop(colsWithNoImpact,axis = 1, inplace = True , errors = 'ignore')

h1b_2021Q1["SUPPORT_H1B"].fillna("NOT", inplace = True)
h1b_2021Q2["SUPPORT_H1B"].fillna("NOT", inplace = True)
h1b_2021Q3["SUPPORT_H1B"].fillna("NOT", inplace = True)
h1b_2021Q4["SUPPORT_H1B"].fillna("NOT", inplace = True)

h1b_2021Q1["STATUTORY_BASIS"].fillna("NOT", inplace = True)
h1b_2021Q2["STATUTORY_BASIS"].fillna("NOT", inplace = True)
h1b_2021Q3["STATUTORY_BASIS"].fillna("NOT", inplace = True)
h1b_2021Q4["STATUTORY_BASIS"].fillna("NOT", inplace = True)

h1b_2021Q1["WILLFUL_VIOLATOR"].fillna("NOT", inplace = True)
h1b_2021Q2["WILLFUL_VIOLATOR"].fillna("NOT", inplace = True)
h1b_2021Q3["WILLFUL_VIOLATOR"].fillna("NOT", inplace = True)
h1b_2021Q4["WILLFUL_VIOLATOR"].fillna("NOT", inplace = True)

h1b_2021Q1["H1B_DEPENDENT"].fillna("NOT", inplace = True)
h1b_2021Q2["H-1B_DEPENDENT"].fillna("NOT", inplace = True)
h1b_2021Q3["H1B_DEPENDENT"].fillna("NOT", inplace = True)
h1b_2021Q4["H-1B_DEPENDENT"].fillna("NOT", inplace = True)


h1b_2021Q1["EMPLOYER_NAME"].fillna("Other", inplace = True)
h1b_2021Q2["EMPLOYER_NAME"].fillna("Other", inplace = True)
h1b_2021Q3["EMPLOYER_NAME"].fillna("Other", inplace = True)
h1b_2021Q4["EMPLOYER_NAME"].fillna("Other", inplace = True)

h1b_2021Q3["WAGE_RATE_OF_PAY_FROM"].fillna(0, inplace = True)
h1b_2021Q3["PREVAILING_WAGE"].fillna(0, inplace = True)
h1b_2021Q3["PW_UNIT_OF_PAY"].fillna("N/A", inplace = True)
h1b_2021Q3["WAGE_UNIT_OF_PAY"].fillna("N/A", inplace = True)

h1b2021 = h1b_2021Q4.append(h1b_2021Q3, ignore_index = True)
h1b2021['H-1B_DEPENDENT'].fillna(h1b2021.H1B_DEPENDENT, inplace=True)
h1b2021 = h1b2021.append(h1b_2021Q2, ignore_index = True)
h1b2021 = h1b2021.append(h1b_2021Q1, ignore_index = True)
h1b2021['H-1B_DEPENDENT'].fillna(h1b2021.H1B_DEPENDENT, inplace=True)


#h1b_dependent has duplicate values change them
h1b2021['H-1B_DEPENDENT'] = np.where(h1b2021['H-1B_DEPENDENT'] == 'Y', 'Yes', h1b2021['H-1B_DEPENDENT'])
h1b2021['H-1B_DEPENDENT'] = np.where(h1b2021['H-1B_DEPENDENT'] == 'N', 'No', h1b2021['H-1B_DEPENDENT'])

h1b2021_copy = h1b2021.copy()

#willful violator has duplicate values change them
h1b2021_copy['WILLFUL_VIOLATOR'] = np.where(h1b2021_copy['WILLFUL_VIOLATOR'] == 'Y', 'Yes', h1b2021_copy['WILLFUL_VIOLATOR'])
h1b2021_copy['WILLFUL_VIOLATOR'] = np.where(h1b2021_copy['WILLFUL_VIOLATOR'] == 'N', 'No', h1b2021_copy['WILLFUL_VIOLATOR'])

#willful violator has duplicate values change them
h1b2021_copy['AGREE_TO_LC_STATEMENT'] = np.where(h1b2021_copy['AGREE_TO_LC_STATEMENT'] == 'Y', 'Yes', h1b2021_copy['AGREE_TO_LC_STATEMENT'])
h1b2021_copy['AGREE_TO_LC_STATEMENT'] = np.where(h1b2021_copy['AGREE_TO_LC_STATEMENT'] == 'N', 'No', h1b2021_copy['AGREE_TO_LC_STATEMENT'])


h1b2021_copy = h1b2021_copy[h1b2021_copy['CASE_STATUS'] != 'Withdrawn']
h1b2021_copy = h1b2021_copy[h1b2021_copy['CASE_STATUS'] != 'Certified - Withdrawn']
h1b2021_copy = h1b2021_copy[h1b2021_copy['VISA_CLASS'] != 'E-3 Australian']
h1b2021_copy = h1b2021_copy[h1b2021_copy['VISA_CLASS'] != 'H-1B1 Singapore']
h1b2021_copy = h1b2021_copy[h1b2021_copy['VISA_CLASS'] != 'H-1B1 Chile']

#drop columns
h1b2021_copy.drop(['CASE_NUMBER','DECISION_DATE','SOC_TITLE'],axis = 1, inplace = True)


h1b2021_copy.drop(['H1B_DEPENDENT'],axis =1 , inplace = True)

#converting all the column types to string
for i in range(0,len(h1b2021_copy.columns)):
    h1b2021_copy[h1b2021_copy.columns[i]] = h1b2021_copy[h1b2021_copy.columns[i]].astype('string')

from sklearn.preprocessing import OrdinalEncoder
enc = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)

data_y = h1b2021_copy['CASE_STATUS']
data_x = h1b2021_copy.drop(labels=['CASE_STATUS'], axis=1, inplace=False)

x_train, x_test, y_train, y_test = train_test_split(data_x,data_y,test_size = 0.3, random_state = 102,shuffle = True)

enc.fit(x_train)
x_train = enc.transform(x_train)
x_test = enc.transform(x_test)

from sklearn import preprocessing
label_encoder =  preprocessing.LabelEncoder()
label_encoder.fit(y_train)
y_train = label_encoder.transform(y_train)
y_test = label_encoder.transform(y_test)

from sklearn.ensemble import RandomForestClassifier

clf=RandomForestClassifier(n_estimators=50)

clf.fit(x_train,y_train)

y_pred=clf.predict(x_test)


from sklearn.metrics import accuracy_score
print("Accuracy Score:",accuracy_score(y_test,y_pred))

def undersample(df):
    classes = df['CASE_STATUS'].value_counts().to_dict()
    least_class_amount = min(classes.values())
    classes_list = []
    for key in classes:
        classes_list.append(df[df['CASE_STATUS'] == key]) 
    classes_sample = []
    for i in range(0,len(classes_list)-1):
        classes_sample.append(classes_list[i].sample(least_class_amount))
    df_maybe = pd.concat(classes_sample)
    final_df = pd.concat([df_maybe,classes_list[-1]], axis=0)
    final_df = final_df.reset_index(drop=True)
    return final_df


h1b_2021_under = undersample(h1b2021_copy)
data_y = h1b_2021_under['CASE_STATUS']
data_x = h1b_2021_under.drop(labels=['CASE_STATUS','VISA_CLASS','FULL_TIME_POSITION','NEW_CONCURRENT_EMPLOYMENT','AGREE_TO_LC_STATEMENT','WILLFUL_VIOLATOR'], axis=1, inplace=False)
x_train, x_test, y_train, y_test = train_test_split(data_x,data_y,test_size = 0.3, random_state = 102,shuffle = True)

x_train1 = x_train.copy()
y_train1 = y_train.copy()
x_test1 = x_test.copy()
y_test1 = y_train.copy()

enc.fit(x_train)
x_train = enc.transform(x_train)
x_test = enc.transform(x_test)

label_encoder =  preprocessing.LabelEncoder()
label_encoder.fit(y_train)
y_train = label_encoder.transform(y_train)
y_test = label_encoder.transform(y_test)

clf=RandomForestClassifier(n_estimators=50)

clf.fit(x_train,y_train)

y_pred=clf.predict(x_test)

print("Accuracy Score:",accuracy_score(y_test,y_pred))


import pickle
with open("encoder2.pickle", "wb") as f: 
    pickle.dump(enc, f)
f.close()
with open('model2.pickle', 'wb') as f:
    pickle.dump(clf, f)
