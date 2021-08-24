
def predict(x,y):
    import pickle
    predictor = pickle.load(open('predictApp\model.p','rb'))
    Ans = predictor.predict_proba([[x,y]])
    return Ans[0][1]