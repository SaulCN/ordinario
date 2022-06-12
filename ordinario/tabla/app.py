
import pymongo
from flask import Flask, request,render_template, redirect, url_for,jsonify
client= pymongo.MongoClient("mongodb://root:s123@mongo_compose:27017/") 
db=client["transacciones"]
coll=db["moni"]
app= Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/usuario' ,methods=['POST'])
def usuario():
    inset_datos={}
   
    if coll.find_one({'_id':request.form['reference']})== None:
        inset_datos={}
        inset_datos["_id"]=request.form['reference']
        inset_datos["date"]=request.form["date"]
        inset_datos["amount"]=request.form["amount"]
        inset_datos["type"]=request.form["type"]
        inset_datos["category"]=request.form["category"]
        inset_datos["user_email"]=request.form["user_email"]

        result = coll.insert_one(inset_datos)
    else:
        return str("ya existe esa referencia: "+ request.form['reference'])

    return redirect(url_for('index'))

@app.route('/ver_usario' ,methods=['POST'])
def ver_usario():
    aux=ver(request.form["a"])
    return jsonify(aux)

@app.route('/ver_usarios' ,methods=['POST'])
def ver_usarios():
    b=[x for x in coll.find({},{'_id':0,"user_email":1})]
    aux1=[b[0]["user_email"]]
    for i in range (0,len(b),1):
        badera=False
        for j in range (0,len(aux1),1):
            if aux1[j]==b[i]["user_email"]:
                badera=True
        if badera==False:
            aux1.append(b[i]["user_email"])
                
                
    buck=[]
    for j in range (0,len(aux1),1):
        a=[x for x in coll.find({'user_email':aux1[j],'type':"outflow"},{'_id':0,"amount":1,'type':1})]
        operacion_on=0
        for i in range(0,len(a),1):
            if a[i]['type']=="outflow":
                operacion_on=operacion_on+float(a[i]["amount"])
        a=[x for x in coll.find({'user_email':aux1[j],'type':"inflow"},{'_id':0,"amount":1,'type':1})]
        operacion_in=0
        for i in range(0,len(a),1):
            if a[i]['type']=="inflow":
                operacion_in=operacion_in+float(a[i]["amount"])
        aux={
        "user_email":aux1[j],
        "total_inflow":str(operacion_in),
        "total_outflow":str(operacion_on)
        }
        buck.append(aux)

    return str(buck) #jsonify(buck)


def ver(nombre):
    num=nombre
    a=[x for x in coll.find({'user_email':num,'type':"outflow"},{'_id':0,"category":1,"amount":1 })]
    operacion_g=0
    operacion_r=0
    operacion_t=0
    for i in range(0,len(a),1):
        if a[i]["category"]=="groceries":
            operacion_g=operacion_g+float(a[i]["amount"])
        if a[i]["category"]=="rent":
            operacion_r=operacion_r+float(a[i]["amount"])
        if a[i]["category"]=="transfer":
            operacion_t=operacion_t+float(a[i]["amount"])
    a=[x for x in coll.find({'user_email':num,'type':"inflow"},{'_id':0,"category":1,"amount":1})]
    operacion_s=0
    operacion_ss=0
    for i in range(0,len(a),1):
        if a[i]["category"]=="salary":
            operacion_s=operacion_s+float(a[i]["amount"])
        if a[i]["category"]=="savings":
            operacion_ss=operacion_ss+float(a[i]["amount"])
    aux={
        "inflow":{
            "salary":str(operacion_s),
            "savings":str(operacion_ss)
        },
        "outflow":{
            "groceries":str(operacion_g),
            "rent":str(operacion_r),
            "transfer": str(operacion_t)
        }
    }
    return aux


if __name__ =='__main__':
    app.run(debug=True)