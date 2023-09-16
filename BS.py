from flask import Flask,request,jsonify
import joblib
import pandas as pd
app=Flask(__name__)

#connect POST api call
@app.route('/bspredict',methods=['POST'])
def predict():
    feat_data=request.json
    df=pd.DataFrame(feat_data)
    df=df.reindex(columns=col_names)
    prediction=list(model.predict(df))
    
    return jsonify({'prediction':str(prediction)})

#load my model and column names

if __name__== '__main__':
    model=joblib.load("brainstroke_model.pkl")
    col_names=joblib.load('BS_col_names.pkl')
    app.run(debug=True)