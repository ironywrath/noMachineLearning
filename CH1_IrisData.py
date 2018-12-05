import os
import requests

PATH = os.path.dirname(os.path.abspath(__file__))
#print(PATH)
CWD = os.getcwd()
#print(CWD)

def DownloadIrisData(url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', filename='iris.data'):
    r = requests.get(url=url)
    with open(PATH+'/'+filename,'w') as f:
        f.write(r.text)
    return PATH

DownloadIrisData()