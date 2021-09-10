def predict_ENGCE101(ENGCC304,FUNMA105,FUNSC101,GEBLC103):
    import pickle
    file = open('predictApp/predictModel_ENGCE101.p','rb')
    predictor = pickle.load(file)
    Predict_result = predictor.predict_proba([[ENGCC304,FUNMA105,FUNSC101,GEBLC103]])
    file.close()
    return Predict_result[0][1]*100

def predict_ENGCE102(ENGCC304,FUNMA105,FUNSC101,GEBLC103):
    import pickle
    file = open('predictApp/predictModel_ENGCE102.p','rb')
    predictor = pickle.load(file)
    Predict_result = predictor.predict_proba([[ENGCC304,FUNMA105,FUNSC101,GEBLC103]])
    file.close()
    return Predict_result[0][1]*100

def predict_ENGCE103(ENGCC304,ENGEE106,FUNSC101,GEBLC103):
    import pickle
    file = open('predictApp/predictModel_ENGCE103.p','rb')
    predictor = pickle.load(file)
    Predict_result = predictor.predict_proba([[ENGCC304,ENGEE106,FUNSC101,GEBLC103]])
    file.close()
    return Predict_result[0][1]*100

def predict_ENGCE104(ENGCE102,ENGCE106,ENGEE106,FUNSC101):
    import pickle
    file = open('predictApp/predictModel_ENGCE104.p','rb')
    predictor = pickle.load(file)
    Predict_result = predictor.predict_proba([[ENGCE102,ENGCE106,ENGEE106,FUNSC101]])
    file.close()
    return Predict_result[0][1]*100

def predict_ENGCE105(ENGCE102,ENGCE103,ENGCE106,ENGEL106,FUNMA105,FUNSC101):
    import pickle
    file = open('predictApp/predictModel_ENGCE105.p','rb')
    predictor = pickle.load(file)
    Predict_result = predictor.predict_proba([[ENGCE102,ENGCE103,ENGCE106,ENGEL106,FUNMA105,FUNSC101]])
    file.close()
    return Predict_result[0][1]*100

def predict_ENGCE106(ENGCE104,ENGEL106,FUNSC101,GEBLC103):
    import pickle
    file = open('predictApp/predictModel_ENGCE106.p','rb')
    predictor = pickle.load(file)
    Predict_result = predictor.predict_proba([[ENGCE104,ENGEL106,FUNSC101,GEBLC103]])
    file.close()
    return Predict_result[0][1]*100

def predict_ENGCE107(ENGCE102,ENGCE104,ENGCE106,FUNSC101):
    import pickle
    file = open('predictApp/predictModel_ENGCE107.p','rb')
    predictor = pickle.load(file)
    Predict_result = predictor.predict_proba([[ENGCE102,ENGCE104,ENGCE106,FUNSC101]])
    file.close()
    return Predict_result[0][1]*100

def predict_ENGCE108(ENGCE105,ENGCE111,ENGCE112):
    import pickle
    file = open('predictApp/predictModel_ENGCE108.p','rb')
    predictor = pickle.load(file)
    Predict_result = predictor.predict_proba([[ENGCE105,ENGCE111,ENGCE112]])
    file.close()
    return Predict_result[0][1]*100

def predict_ENGCE109(ENGCE104,ENGCE106,ENGEL106):
    import pickle
    file = open('predictApp/predictModel_ENGCE109.p','rb')
    predictor = pickle.load(file)
    Predict_result = predictor.predict_proba([[ENGCE104,ENGCE106,ENGEL106]])
    file.close()
    return Predict_result[0][1]*100

def predict_ENGCE110(ENGCC304,ENGEL105,ENGEL106):
    import pickle
    file = open('predictApp/predictModel_ENGCE110.p','rb')
    predictor = pickle.load(file)
    Predict_result = predictor.predict_proba([[ENGCC304,ENGEL105,ENGEL106]])
    file.close()
    return Predict_result[0][1]*100

def predict_ENGCE111(ENGCE103,ENGCE106,ENGEL106,GEBLC103):
    import pickle
    file = open('predictApp/predictModel_ENGCE111.p','rb')
    predictor = pickle.load(file)
    Predict_result = predictor.predict_proba([[ENGCE103,ENGCE106,ENGEL106,GEBLC103]])
    file.close()
    return Predict_result[0][1]*100

def predict_ENGCE112(ENGCC304,ENGCE102,GEBLC103):
    import pickle
    file = open('predictApp/predictModel_ENGCE112.p','rb')
    predictor = pickle.load(file)
    Predict_result = predictor.predict_proba([[ENGCC304,ENGCE102,GEBLC103]])
    file.close()
    return Predict_result[0][1]*100

def predict_ENGEL105(ENGCE106,ENGEL106,FUNSC101,GEBLC103):
    import pickle
    file = open('predictApp/predictModel_ENGEL105.p','rb')
    predictor = pickle.load(file)
    Predict_result = predictor.predict_proba([[ENGCE106,ENGEL106,FUNSC101,GEBLC103]])
    file.close()
    return Predict_result[0][1]*100

def predict_ENGEL106(ENGCE102,ENGCE106,ENGEE106,FUNMA105,FUNSC101):
    import pickle
    file = open('predictApp/predictModel_ENGEL106.p','rb')
    predictor = pickle.load(file)
    Predict_result = predictor.predict_proba([[ENGCE102,ENGCE106,ENGEE106,FUNMA105,FUNSC101]])
    file.close()
    return Predict_result[0][1]*100