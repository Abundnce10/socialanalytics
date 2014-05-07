from . import helpers
import requests

# Twitter API
TWITTER_ENDPOINT = "http://urls.api.twitter.com/1/urls/count.json?url="


def getShares(url):
	# Remove any URL tracking params
	url = helpers.removeParams(url)
	# Create Twitter API URL
	target_url = TWITTER_ENDPOINT + url
	# Hit Twitter API
	try:
		r = requests.get(target_url)
		j = r.json()
		# Return Count value
		return {'share_count': j['count'] }
	except Exception as e:
		return { 'error': e }
	
