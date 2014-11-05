from . import helpers
import requests

# Google+ API
GOOGLE_ENDPOINT = "https://plusone.google.com/_/+1/fastbutton?url="

	

def getPlusOnes(url):
	# Remove any URL tracking params
	url = helpers.removeParams(url)
	# Encode URL
	url = helpers.encodeURL(url)
	# Create Google+ API URL
	target_url = GOOGLE_ENDPOINT + url
	try:
		# Hit Google+ API
		r = requests.get(target_url)
		# Look for a "window.__SSR" key
		if r.text.find("window.__SSR") != -1:
			# Parse count value from response
			window = r.text.find("window.__SSR")
			start = r.text.find("c:", window)
			end = r.text.find(',', start+1)
			key_len = len('c:')
			# Convert pin_count to integer
			plus_count = int(float(r.text[start+key_len:end].strip()))
			return { 'plus_count': plus_count }
		else:
			return { 'error': 'Remember to use http://...' }
	except ValueError as e:
		return { 'plus_count': 0 }
	except Exception as e:
		return { 'error': 'Please provide an actual URL. Remember to use http://...' }


def getEncodedURL(url):
	# Remove any URL tracking params
	url = helpers.removeParams(url)
	# Encode URL
	url = helpers.encodeURL(url)
	# Create Facebook API URL
	return GOOGLE_ENDPOINT + url

