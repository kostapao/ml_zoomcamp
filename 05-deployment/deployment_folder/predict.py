

import pickle


with open(output_file, 'rb') as f_in:
    (dv, model) = pickle.load(f_in)




dv, model


customer = {'gender' : 'female', 'seniorcitizen' : 0, 'partner':'yes', 'dependents':'no',
       'tenure':1, 'phoneservice':'no', 'multiplelines': 'no_phone_service', 'internetservice': 'dsl',
       'onlinesecurity':'no', 'onlinebackup':'yes', 'deviceprotection':'no', 'techsupport':'no',
       'streamingtv':'no', 'streamingmovies':'no', 'contract':'month_to_month', 'paperlessbilling':'yes',
       'paymentmethod':'electronic_check', 'monthlycharges':29.85, 'totalcharges':29.85}


X = dv.transform([customer])


model.predict_proba(X)[0,1] 

