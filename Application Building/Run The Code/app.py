import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import Flask,render_template,request

app=Flask(__name__)
model=load_model("fruit_data.h5")
model2=load_model("vegetable_data.h5")
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        f=request.files['image']
        basepath=os.path.dirname(__file__)
        filepath=os.path.join(basepath,'uploads',f.filename)
        f.save(filepath)
        img=image.load_img(filepath,target_size=(128,128))
        x=image.img_to_array(img)
        x=np.expand_dims(x,axis=0)
        pred=np.argmax(model.predict(x),axis=1)
        #plant=request.form['plant']
        plant = request.form.get("data")
        if (plant=="fruit"):
            index=['Apple___Black_rot','Apple___healthy','Corn_(maize)___healthy','Corn_(maize)___Northern_Leaf_Blight','Peach___Bacterial_spot','Peach___healthy']
            if(pred[0]==0):
                text="The Classified Plant Disease is : " +str(index[pred[0]] + ". Fertilizers recommended are Captan and fungicides containing a strobulurin (FRAC Group 11 Fungicides) as an active ingredient are effective controlling black rot on fruit.")
            elif(pred[0]==3):
                text="The Classified Plant Disease is : " +str(index[pred[0]] + ". Fertilizers recommended are Bio-fungicides based on Trichoderma harzianum, or Bacillus subtilis can be applied at different stages to decrease the risk of infection. Application of sulfur solutions is also effective.")
            elif(pred[0]==4):
                text="The Classified Plant Disease is : " +str(index[pred[0]] + ". Fertilizers recommended are Copper-based sprays alone or together with an antibiotic can be used preventively with moderate efficacy. Dosage must be reduced progressively to avoid damage to leaves.")
            else:
                text="The Classified Plant is : " +str(index[pred[0]] + ". And the plant is healthy.")
        return text
        if (plant=="vegetable"):
            pred=model2.predict_classes(x)
            index=['Pepper,_bell___Bacterial_spot','Pepper,_bell___healthy','Potato___Early_blight','Potato___Late_blight','Potato___healthy','Tomato___Bacterial_spot','Tomato___Late_blight','Tomato___Leaf_Mold','Tomato___Septoria_leaf_spot']
            if(pred[0]==0):
                text="The Classified Plant Disease is : " +str(index[pred[0]] + ". Fertilizers recommended are Foliar applications of ammonium lignosulfonate (ALS), derived from the wood pulping process, and the fertilizer potassium phosphate (KP) were tested for their ability to control this disease under both greenhouse and field conditions. Acibenzolar-S-methyl is also included as a component for control.")
            elif(pred[0]==2):
                text="The Classified Plant Disease is : " +str(index[pred[0]] + ". Fertilizers recommended are Bio-fungicides based on Trichoderma harzianum, or Bacillus subtilis can be applied at different stages to decrease the risk of infection. Application of sulfur solutions is also effective.")
            elif(pred[0]==3):
                text="The Classified Plant Disease is : " +str(index[pred[0]] + ". Septum is effective right from the outset of the disease as it has both a preventive and curative effect. It produces the breakdown and dehydration of fungal tissues and interrupts sporulation of fungi.")
            elif(pred[0]==5):
                text="The Classified Plant Disease is : " +str(index[pred[0]] + ". Fertilizers recommended are  use Dithane (mancozeb) MZ or you can also use Tattoo C or Acrobat MZ. Acrobat used later in the season reduces late blight spores. Use just before topkilling if there is blight in the crop.")
            elif(pred[0]==6):
                text="The Classified Plant Disease is : " +str(index[pred[0]] + ". Fertilizers recommended are organic fungicides based on Bacillus subtilis or copper can help prevent or stop the spread of this tomato plant disease. Bicarbonate fungicides are also effective (including BiCarb, GreenCure, etc).")
            elif(pred[0]==7):
                text="The Classified Plant Disease is : " +str(index[pred[0]] + ". Fertilizers recommended are Organic fungicides based on Bacillus subtilis are somewhat effective in preventing this tomato plant disease when it’s first discovered in your area.")
            elif(pred[0]==8):
                text="The Classified Plant Disease is : " +str(index[pred[0]] + ". Fertilizers recommended are Organic fungicides based on copper or Bacillus subtilis are effective against septoria leaf spot, especially when used as a preventative measure.")
            else:
                text="The Classified Plant is : " +str(index[pred[0]] + ". And the plant is healthy.")
        return text
   

if __name__=='__main__':
    app.run(debug=False)