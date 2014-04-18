from . import helpers
import requests

# Pinterest API
PINTEREST_ENDPOINT = "http://api.pinterest.com/v1/urls/count.json?url="


def getPins(url):
	try:
		# Remove any URL tracking params
		url = helpers.removeParams(url)
		# Create Pinterest API URL
		target_url = PINTEREST_ENDPOINT + url
		# Hit Pinterest API
		r = requests.get(target_url)
		# Look for a "count" key
		if r.text.find("count") != -1:
			# Parse count value from response
			start = r.text.find('\"count\"')
			end = r.text.find(',', start+1)
			key_len = len('\"count\"')
			# Convert pin_count to integer
			pin_count = int(r.text[(start + key_len + 1):end].strip().replace('"',''))
			return pin_count
		else:
			# Parse error
			start = r.text.find('\"error\"')
			end = r.text.find(',', start+1)
			key_len = len('\"error\"')
			# Return error message
			return r.text[(start + key_len + 1):end].strip().replace('"', '')
	except Exception as e:
		return e

