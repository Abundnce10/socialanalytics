import requests

# Pinterest API
pinterest_endpoint = "http://api.pinterest.com/v1/urls/count.json?url="


def getPins(url):
	try:
		target_url = pinterest_endpoint + url
		# Hit Pinterest API
		r = requests.get(target_url)
		# Parse response
		start = r.text.find('\"count\"')
		end = r.text.find(',', start+1)
		content = len('\"count\"')
		# Convert pin_count to integer
		pin_count = int(r.text[(start+content+1):end].strip().replace('"',''))
		return pin_count
	except Exception as e:
		return e
