import joblib


def predict_svm(input_text):
    loaded_model = joblib.load('trained_model/lsvc_pipeline.pkl')
    text_list = []
    text_list.append(input_text)
    predicted_sentiment = loaded_model.predict(text_list)
    return predicted_sentiment