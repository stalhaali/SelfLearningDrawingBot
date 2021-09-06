from flask import render_template, url_for, flash, redirect, request, abort
from drawingbot import app
from drawingbot.objectdetect import detect, create_img
from drawingbot.drawingai import predict_img, model_update
from drawingbot.forms import ConfirmForm


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    """Renders home page for web app
    """
    #engine.say("choose a category")
    return render_template('home.html', title = 'home')

@app.route("/draw/<option>", methods=['GET', 'POST'])
def draw(option):
    """Renders the drawing canvas page and prediction confirmation page.
    It is also used to communicate between front-end and trained models. 
    This function preprocesses the drawings sent from the front-end into a form readable
    by the trained model, using opencv, and then sends the trained model's 
    prediction back to the front end.
    """
    form = ConfirmForm()
    if option == "Vehicles":
        num = 2
    elif option == "Fruits":
        num = 1
    elif option == "Shapes":
        num = 3
    else:
        abort(403)
    print(num)
    if form.validate_on_submit():
        model_update(num)
        return render_template('home.html', title = 'draw', category = option, form = form)
    if request.method == "POST":
        data_url = request.form["nm"]
        lst = detect(data_url)
        print("THIS IS THE LENGHT" + str(len(lst)))
        dic = predict_img(lst, num)
        lst1 = []
        for i in range(1, len(lst) + 1):
            lst1.append('<img src="http://localhost:5000/static/' + 'picture' + str(i) + '.jpg' +'" alt="bar" width="100%" height="100%">')
            print('<img src="http://localhost:5000/static/' + 'picture' + str(i) + '.jpg' +'" alt="bar" width="1000px" height="1000px">')
        create_img(dic)
        #for key in dic:
            #flash("I see " + str(dic[key]) + str(key)) #ignore for now
        return render_template('home.html', title = 'results', number = lst1, form = form, category = option)
    else:
        return render_template('home.html', title = 'draw', category = option, form = form)


