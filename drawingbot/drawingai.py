import joblib
import numpy as np
import pyttsx3
model = joblib.load(r'C:\Users\Talha\Desktop\project2\drawingbot\model_joblib')
model2 = joblib.load(r'C:\Users\Talha\Desktop\project2\drawingbot\model2_joblib')
model3 = joblib.load(r'C:\Users\Talha\Desktop\project2\drawingbot\model3_joblib')

def predict_img(lst, num):
    engine = pyttsx3.init()
    dic = {}
    dic_return = {}
    i = 0
    print(num)
    if num == 1:
        ai = model
    elif num == 2:
        ai = model2
    elif num == 3:
        ai = model3
    for img in lst:
        i += 1
        np_img = np.array(img)
        obj = ai.predict(np_img.reshape(1, 784))
        obj = obj[0]
        print(obj)
        if obj not in dic:
            dic[obj] = 1
        else:
            dic[obj] += 1
        dic_return[i] = obj
    for key in dic:
        engine.say("I see " + str(dic[key]) + str(key))
        engine.runAndWait()
    return dic_return

def model_update(num):
    if num == 1:
        ai = model
    elif num == 2:
        ai = model2
    elif num == 3:
        ai = model3
    #at this point we would update the model
    #However, since the machine learning model we are using is of kneighbours of sklearn, when adding
    #new data to this model, it overwrites the previous data. Thus, we cannot update this model.
    #However other ML models from sklearn have a partial_fit features which allows you to add new
    #data without overwriting the previous one to a model.
    #Todo: so we can use a different sklearn model like decisiontreeclassifier to do this.
