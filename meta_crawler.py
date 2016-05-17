import requests
import json

headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-US,en;q=0.8,fr;q=0.6",
"Connection": "keep-alive",
"Content-Length": 16,
"Content-Type": "application/json; charset=UTF-8",
"Cookie": "toShowIxigo=1; ASP.NET_SessionId=4eaauc550rqmmg55djarme45",
"Host": "mabhoomi.telangana.gov.in",
"Origin": "http://mabhoomi.telangana.gov.in",
"Referer": "http://mabhoomi.telangana.gov.in/GramaPahani.aspx",
"User-Agent": "runscope/0.1,Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.86 Safari/537.36",
"X-Requested-With": "XMLHttpRequest"}

def call(district_id):
	mandalpayload = {'DistrictId':district_id }
	url = "http://mabhoomi.telangana.gov.in/GramaPahani.aspx/PopulateMandals"
	response = requests.post(url=url,data=json.dumps(mandalpayload),headers=headers)
	results = json.loads(response.content)['d']
	for result in results:
		mandal_id = result['Value']
		villagepayload = json.dumps({'MandalId': mandal_id,'DistrictCode':district_id})
		villageurl = "http://mabhoomi.telangana.gov.in/GramaPahani.aspx/PopulateVillages"
		responseVillage = requests.post(url=villageurl,data=villagepayload,headers=headers)
		resultsVillage = json.loads(responseVillage.content)['d']
		for resultV in resultsVillage:
			print mandal_id+","+resultV['Value']

	


call(23)

# villagepayload = {'MandalId': ,'DistrictCode':}

