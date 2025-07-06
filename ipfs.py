import requests
import json


def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
	jwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJkMTc3MjExOC0wMWI4LTRiY2UtYWFiYy05MGZmOGM0NTM0MjAiLCJlbWFpbCI6InNydTI4QHNlYXMudXBlbm4uZWR1IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiRlJBMSJ9LHsiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiTllDMSJ9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6ImYyMWE3MDI0OGY4OGNhMDZiZjBhIiwic2NvcGVkS2V5U2VjcmV0IjoiZDU2NzBlYjYzNjA4NTYzYjA0ZWJjMGYwYWI4MjU0ZmUwODY5ZjBmNGY3YTFlNTM2MjVmOWNkYWNlYWZiZjAyZCIsImV4cCI6MTc4MzMwMTAxMH0.IE08PeWgO7CzjSgjJy_cfNhRfdAWKelJkGnyAEtRPnw'
	headers = {
		"Authorization": jwt,
		"Content-Type": "application/json"
	}
	response = requests.post(url, headers=headers, data=json.dumps(data))
	cid = response.json()["IpfsHash"]

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	url = f"https://gateway.pinata.cloud/ipfs/{cid}"
	response = requests.get(url)
	data = response.json
	
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
