from flask import Flask, render_template, request,redirect, url_for, session
import sorts

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "super secret key"

from login import login
import ml
import json


@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method == "POST":
        if login(request.form["userid"],request.form["password"]):
            return redirect('/main/'+request.form["userid"])
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")
    
@app.route("/main/<user_id>", methods=['GET', 'POST'])
def mainpage(user_id):
    if request.method == "POST":
        x = request.form["cart"]
        if(x==""):
            x=0
        return redirect('/main/'+user_id+'/cart/'+x)
    else:
        return render_template('main.html',
                           oneriler = ml.run(user_id),
                           pf = sorts.get_pf(user_id),
                           id = user_id,
                           en_son_satin_alinan_20 = sorts.en_son_satin_alinan_20(user_id),
                           en_cok_satilan_20 = sorts.en_cok_satilan_20(),
                           en_cok_satin_alinan_20 = sorts.clients_Most_Purchased_Items(user_id),
                           en_az_satin_alinan_20 = sorts.clients_Least_Purchased_Items(user_id),
                           tum_urunler = sorts.tum_urunler())

@app.route("/main/<user_id>/cart/<liste>", methods=['GET','POST'])
def cart(user_id,liste):
    if request.method == "POST":
        x = request.form["shoppinglist"]
        x = x.split(",")
        
        order_list = []
        for i in range(len(x)-1):
           order_list.append({'urun_kodu': x[i+1].split("+")[0], 'miktar': x[i+1].split("+")[1]})
             
        user = {'user_id':x[0],
                'order': order_list}
        with open("siparisler.json", "r") as json_file:
            file_content = json.load(json_file)
            file_content["orders"].append(user)
            print(file_content["orders"])

        return render_template('completed.html',id = user_id)
    else:
        return render_template('cart.html',id = user_id,liste = liste,tum_urunler = sorts.tum_urunler(),pf = sorts.get_pf(user_id))