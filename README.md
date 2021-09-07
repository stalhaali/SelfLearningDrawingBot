# SelfLearningDrawingBot

Given 3 categories, shapes, fruits, and vehicles, each of which contain 4 drawing options, the user must choose a category then draw as many of the 4 drawing objects.
The drawing bot then predicts what the user tried to draw. If the prediction is correct, the drawing bot adds the drawings into its database and learns from this new data.

# Structure

1. The model is trained in python using sklearn's KNeighborsClassifier. (**trainingmodel/model.py**)
2. The dataset used to train the model is from Googles Quickdraw [game](https://quickdraw.withgoogle.com/) (**trainingmodel/Data.txt**)
3. A web app is created using Flask. It preprocesses the drawings sent from the front-end into a form readable by the trained model, using opencv, and then sends the trained model's prediction back to the front end. 
4. The front-end is made using html, css and js. Html's canvas is used to draw and the drawings are converted into a datauri and sent to the flask server. 

# Demo

Short demonstartion 

![Using drawing bot](https://github.com/stalhaali/SelfLearningDrawingBot/blob/main/readme_files/demo.gif "Gif of using app")

# Installation
See (**requirements.txt**) for all the required libraries. Open command prompt and type "pip install requirement" (for each requirement).

One must also have git lfs downloaded. Download from this [link](https://git-lfs.github.com/). Then open command prompt and type "git lfs install", to install. 

Now you can run the app :)

# How to run

Download this repository once all required libraries and git lfs are installed and then:

```bash
python run.py
```



