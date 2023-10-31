import matplotlib.pyplot as plt
import numpy as np
import json
import datetime as dt


def todayDate():
    return str(dt.date.today())

def openData(name):
    with open(name, 'r') as f:
        return json.load(f)

def newData(data,name):
     with open(name,'w') as f:
        json.dump(data,f,indent=4)
    
def showChartratio():
    data = openData("dataRatio.json")

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
    
def addDateJson(ratio1,error,dataName,dataType,ratio2=4.5):
    data = openData(dataName)
    date = todayDate()
    try:
        if float(ratio1) and float(ratio2):
            if dataType == "UP/DOWN":
                data["UP"][0][date] = float(ratio1)
                data["DOWN"][0][date] = float(ratio2)
            else:
                data[date] = float(ratio1)   
            error['text'] = ' '
            newData(data,dataName)
    except:
        error['text'] = 'Not a number'

def showChartUpDown():
    data = openData("dataUD.json")
    tabUD_x = []
    tabU_y = []
    tabD_y = []
    dateUPDOWN = list(data["UP"][0])
    nbrUP = list(data["UP"][0].values())
    nbrDOWN = list(data["DOWN"][0].values())
    t = 1
    for i in dateUPDOWN:
        try:
            tabUD_x.append((i,dateUPDOWN[t]))
        except:
            tabUD_x.append((i,i))
        t+=1
    t = 1
    for i in nbrUP:
        try:
            tabU_y.append((i,nbrUP[t]))
        except:
            tabU_y.append((i,i))
        t+=1
    t = 1
    for i in nbrDOWN:
        try:
            tabD_y.append((i,nbrDOWN[t]))
        except:
            tabD_y.append((i,i))
        t+=1  
    nbrUP.extend(nbrDOWN)
    plt.yticks(nbrUP)
    for i in range(len(tabUD_x)):
        x = np.array(tabUD_x[i])
        y = np.array(tabU_y[i])
        plt.plot(x, y,marker='o',color='green')
        x = np.array(tabUD_x[i])
        y = np.array(tabD_y[i])
        plt.plot(x, y,marker='o',color='red')
    plt.show()