
def predict_ENGCE101(ENGCC304,ENGCC304_Instructor,FUNMA105,FUNMA105_Instructor,FUNSC101,FUNSC101_Instructor,GEBLC103,GEBLC103_Instructor):
    import pickle
    predictor = pickle.load(open('predictApp\predictModel_ENGCE101.p','rb'))
    Predict_result = predictor.predict_proba([[ENGCC304,ENGCC304_Instructor,FUNMA105,FUNMA105_Instructor,FUNSC101,FUNSC101_Instructor,GEBLC103,GEBLC103_Instructor]])
    return Predict_result[0][1]*100