
def predict_ENGCE101(ENGCC304,ENGCC304_Instructor,FUNMA105,FUNSC101,GEBLC103):
    import pickle
    predictor = pickle.load(open('predictApp\predictModel_ENGCE101.p','rb'))
    Predict_result = predictor.predict_proba([[ENGCC304,ENGCC304_Instructor,FUNMA105,FUNSC101,GEBLC103]])
    return Predict_result[0][1]*100