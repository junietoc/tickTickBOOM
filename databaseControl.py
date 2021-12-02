import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("ticktickboom-firebase-adminsdk.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://ticktickboom-34c77-default-rtdb.firebaseio.com/'})

def uploadTick(tick):
    route = "ticks"
    ref = db.reference(route)
    tickInfo = {
        'title' : tick.title,
        'year' : tick.date.year,
        'month' : tick.date.month,
        'day' : tick.date.day
    }
    tickId = ref.push(tickInfo)
    return tickId.key[1:]

def getTick(tickId):
    route = "ticks/" + str(tickId)
    ref = db.reference(route)
    info = ref.get()
    return info
