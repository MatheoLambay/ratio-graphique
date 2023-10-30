import matplotlib.pyplot as plt
import numpy as np
import json
import datetime as dt


def todayDate():
    return str(dt.date.today())

def openData():
    with open('data.json', 'r') as f:
        return json.load(f)

def newData(data):
     with open('data.json','w') as f:
        json.dump(data,f,indent=4)
    
def showChart():
    data = openData()

    tab_x = []
    tab_y = []

    # X = date, Y = ratio
    t = 1
    for i,j in data.items():
        try:
            tab_x.append((i,list(data)[t]))
        except:
            tab_x.append((i,i))
        try:
            tab_y.append((j,list(data.values())[t]))   
        except:
            tab_y.append((j,j))
        t+=1
    plt.yticks(list(data.values()))

    for i in range(len(tab_x)):
        x = np.array(tab_x[i])
        y = np.array(tab_y[i])
        plt.plot(x, y,marker='o',color='green')
    plt.show()
    
def addDateJson(ratio,error):
    try:
        if float(ratio):
            data = openData()
            date = todayDate()
            data[date] = float(ratio)
            error['text'] = ' '
            newData(data)
    except:
        error['text'] = 'Not a number'