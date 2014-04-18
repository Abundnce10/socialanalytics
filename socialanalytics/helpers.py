import urllib

def removeParams(url):
	if url.find('?') == -1:
		return url
	else:
		return url[:url.find('?')]

def encodeURL(url):
	return urllib.quote(url, '')