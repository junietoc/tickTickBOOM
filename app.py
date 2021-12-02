from flask import Flask, render_template,redirect,url_for
import formsControl
import databaseControl
from tick import Tick
from tick import Deadline
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xd?'

@app.route('/')
def index():
 return render_template("./home.html")

@app.route('/addTick',methods=['GET', 'POST'])
def addTick():
 tickForm = formsControl.tickForm()
 tomorrow = str(datetime.datetime.today() + datetime.timedelta(days=1)).split(" ")[0]

 if tickForm.validate_on_submit():
    formTitle = tickForm.tickTitle._value()
    formDate = tickForm.tickDate._value()
    tickDeadline = Deadline(formDate[0:4], formDate[5:7], formDate[8:10])
    newTick = Tick(formTitle, tickDeadline)
    tickId = databaseControl.uploadTick(newTick)
    return redirect(url_for("tick",tickId=tickId))

 return render_template("./addTick.html", tickForm=tickForm,tomorrow=tomorrow)

@app.route('/tick/<tickId>')
def tick(tickId):
    tickInfo = databaseControl.getTick("-"+str(tickId))
    print(tickInfo)
    today = datetime.datetime.today().date()
    tickDate = datetime.datetime.strptime(f"{tickInfo['day']}/{tickInfo['month']}/{tickInfo['year']}", "%d/%m/%Y").date()
    expired = tickDate < today
    tickInfo['expired'] = expired
    return render_template("./tick.html", tickInfo=tickInfo)

