from flask import render_template, url_for, flash, redirect, request, abort
from drawingbot import app
from drawingbot.objectdetect import detect, create_img
from drawingbot.drawingai import predict_img, model_update
from drawingbot.forms import ConfirmForm

class DataStore():
    lst = []
    option = None


data = DataStore()

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    #engine.say("choose a category")
    return render_template('home.html', title = 'home')

@app.route("/draw/<option>", methods=['GET', 'POST'])
def draw(option):
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
        data.lst = lst
        lst1 = []
        for i in range(1, len(lst) + 1):
            lst1.append('<img src="http://localhost:5000/static/' + 'picture' + str(i) + '.jpg' +'" alt="bar" width="100%" height="100%">')
            print('<img src="http://localhost:5000/static/' + 'picture' + str(i) + '.jpg' +'" alt="bar" width="1000px" height="1000px">')
        data.option = option
        create_img(dic)
        #for key in dic:
            #flash("I see " + str(dic[key]) + str(key))
        return render_template('home.html', title = 'results', number = lst1, form = form, category = option)
        return redirect(url_for('confirm', lst1=lst1))
    else:
        return render_template('home.html', title = 'draw', category = option, form = form)


