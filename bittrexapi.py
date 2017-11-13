#! /usr/bin/python3
import http.client, urllib.parse, base64, json, sys, os, pprint, time, hashlib, hmac
from secrets import api

class Bittrex():

	def __init__(self):
		self.conn = http.client.HTTPSConnection("bittrex.com")
		self.apikey = api['key']
		self.apisecret = api['secret']

	def account(self, **kwargs):

		url = "/api/v1.1/market/getopenorders"

		params = {
			'apikey': self.apikey,
			'nonce': time.time()
		}

		params = urllib.parse.urlencode(params)
		requestUrl = "{url}?{params}".format(url=url, params=params)
		uri = 'https://bittrex.com{}'.format(requestUrl)
		sign = hmac.new(uri.encode(), self.apisecret.encode(), hashlib.sha512).hexdigest()

		headersMap = {
			"apisign": sign.encode(),
		}

		print(uri)
		print(headersMap)

		self.conn.request("GET", requestUrl, headers=headersMap)
		response = self.conn.getresponse()

		print(response.status)

		if response.status == 200:
			data = response.read().decode('utf-8')
			result = json.loads(data)
			return(result)

if __name__ == "__main__":

	account = Bittrex()

	params = {
		"convert": 'EUR'
	}

	pprint.pprint(account.account())