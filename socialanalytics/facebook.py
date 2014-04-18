from . import helpers
import requests

FACEBOOK_ENDPOINT = "http://graph.facebook.com/fql?format=json&q=SELECT%20share_count,%20like_count%20,%20comment_count%20FROM%20link_stat%20WHERE%20url="


def getTotalInteractions(url):
	# Remove any URL tracking params
	url = helpers.removeParams(url)
	# Encode URL
	url = helpers.encodeURL(url)
	# Create Facebook API URL
	target_url = FACEBOOK_ENDPOINT + '%27' + url + '%27'
	# Hit Facebook API
	r = requests.get(target_url)
	j = r.json()
	if j['data']:
		# Sum shares, likes, and comments
		return sum(j['data'][0].values())
	else:
		return j['error']['message']


def getObject(url):
	# Remove any URL tracking params
	url = helpers.removeParams(url)
	# Encode URL
	url = helpers.encodeURL(url)
	# Create Facebook API URL
	target_url = FACEBOOK_ENDPOINT + '%27' + url + '%27'
	# Hit Facebook API
	r = requests.get(target_url)
	j = r.json()
	if j['data']:
		return j['data'][0]
	else:
		return j['error']['message']


def getShares(url):
	# Remove any URL tracking params
	url = helpers.removeParams(url)
	# Encode URL
	url = helpers.encodeURL(url)
	# Create Facebook API URL
	target_url = FACEBOOK_ENDPOINT + '%27' + url + '%27'
	# Hit Facebook API
	r = requests.get(target_url)
	j = r.json()
	if j['data']:
		return j['data'][0]['share_count']
	else:
		return j['error']['message']


def getLikes(url):
	# Remove any URL tracking params
	url = helpers.removeParams(url)
	# Encode URL
	url = helpers.encodeURL(url)
	# Create Facebook API URL
	target_url = FACEBOOK_ENDPOINT + '%27' + url + '%27'
	# Hit Facebook API
	r = requests.get(target_url)
	j = r.json()
	if j['data']:
		return j['data'][0]['like_count']
	else:
		return j['error']['message']


def getComments(url):
	# Remove any URL tracking params
	url = helpers.removeParams(url)
	# Encode URL
	url = helpers.encodeURL(url)
	# Create Facebook API URL
	target_url = FACEBOOK_ENDPOINT + '%27' + url + '%27'
	# Hit Facebook API
	r = requests.get(target_url)
	j = r.json()
	if j['data']:
		return j['data'][0]['comment_count']
	else:
		return j['error']['message']


def getEncodedURL(url):
	# Remove any URL tracking params
	url = helpers.removeParams(url)
	# Encode URL
	url = helpers.encodeURL(url)
	# Create Facebook API URL
	return FACEBOOK_ENDPOINT + '%27' + url + '%27'



