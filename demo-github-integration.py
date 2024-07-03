#Get pull req information on a repo using pyhton
import requests


res = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
complete_detail = res.json()

for i in range(len(complete_detail)):
    print(complete_detail[i]["user"]["login"])