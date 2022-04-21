from datetime import datetime
import json

def print_it(data, smart=False):
    if type(data) == list:
        if smart == True:
            for line in data:
                if type(line) == dict:
                    print(json.dumps(line, indent=4))
                else:
                    print(line)
        else:
            for line in data:
                print(line)
    elif type(data) == dict:
        print(json.dumps(data, indent=4))
    else:
        print(data)

def time_msg(msg):
    return str(datetime.utcnow()) + " " + str(msg)

