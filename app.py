
from flask import Flask,render_template,request
#from flask import Flask,render_template,request
#import sklearn
app = Flask(__name__)
import pickle
model = pickle.load(open("placement_data.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/predict")
def predict():
    return render_template("predict.html")
@app.route("/predict")
def output():
    return render_template("output.html")
@app.route("/output")


@app.route('/index1', methods = ['POST','GET'])
def index1():
    if request.method =='POST':
        gender =float(request.form['gender'])
        ssc_p = float( request.form["ssc_p"])
        ssc_b = float(request.form["ssc_b"])
        hsc_p  = float( request.form["hsc_p"])
        
        hsc_b= float(request.form["hsc_b"])
        hsc_s = float(request.form["hsc_s"])
        degree_p = float(request.form["degree_p"])
        degree_t =float( request.form["degree_t"])
        
        workex = float(request.form["workex"])
        etest_p = float(request.form["etest_p"])
        specialisation = float(request.form["specialisation"])
        mba_p = float(request.form["mba_p"])
        salary = float(request.form["salary"])
        
    
        data = [[gender,ssc_p,ssc_b,hsc_p,hsc_b,hsc_s,degree_p,degree_t,workex,etest_p,specialisation,mba_p,salary]]
        prediction = model.predict(data)
        prediction = int(prediction[0])
        if prediction==0:
            return render_template("output.html",prediction="Not Placed")
        
        else:
            return render_template("output.html",prediction="Placed")
    
    
if __name__ == "__main__":
    app.run(debug = True)