def removeParams(url):
	if url.find('?') == -1:
		return url
	else:
		return url[:url.find('?')]