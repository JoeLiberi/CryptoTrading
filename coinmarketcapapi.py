#! /usr/bin/python3
import http.client, urllib.parse, base64, json, sys, os, pprint


class Market():

	def __init__(self):
		self.conn = http.client.HTTPSConnection("api.coinmarketcap.com")


	def ticker(self, **kwargs):

		if 'currency' in kwargs.keys():
			url = "/v1/ticker/{currency}/".format(currency=kwargs['currency'])
		else:
			url = "/v1/ticker/"

		if 'params' in kwargs.keys():

			params = urllib.parse.urlencode(kwargs['params'])

			requestUrl = "{url}?{params}".format(url=url, params=params)

		else:

			requestUrl = "{url}".format(url=url)

		self.conn.request("GET", requestUrl)
		response = self.conn.getresponse()

		if response.status == 200:
			data = response.read().decode('utf-8')
			result = json.loads(data)
			return(result)

	def stats(self, **kwargs):

		url = "/v1/global/"

		if 'params' in kwargs.keys():

			params = urllib.parse.urlencode(kwargs['params'])
			requestUrl = "{url}?{params}".format(url=url, params=params)

		else:
			requestUrl = "{url}".format(url=url)

		self.conn.request("GET", requestUrl)
		response = self.conn.getresponse()

		if response.status == 200:
			data = response.read().decode('utf-8')
			result = json.loads(data)
			return(result)


if __name__ == "__main__":

	market = Market()

	params = {
		"convert": 'EUR'
	}

	pprint.pprint(market.ticker(currency='bitcoin'))