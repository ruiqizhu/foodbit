from firebase import firebase
import json
import datetime

def upload(data):
    f = firebase.FirebaseApplication('https://foodbit.firebaseio.com', None)

    f.post('/foodinfo', data)
    result = f.get('/foodinfo', None)
    # print(json.dumps(result, sort_keys=True, indent=4))
    return True