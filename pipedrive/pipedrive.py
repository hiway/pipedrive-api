import requests


class PipeDriveError(Exception):
	def __init__(self, response):
		self.response = response

	def __str__(self):
		return self.response.get('error', 'No error provided.')


class PipeDrive(object):
	def __init__(self, api_token, version='v1'):
		self.api_token = api_token
		self.api_path = "https://api.pipedrive.com/%s/" % version

	def _build_url(self, endpoint, id, submethod):
		url = self.api_path + endpoint
		if id:
			url = url + '/' + str(id)
		if submethod:
			url = url + '/' + submethod
		return url

	def _request(self, url, method, data):
		params = dict(api_token=self.api_token)
		make_request = getattr(requests, method)
		result = make_request(url=url,
							  data=data,
							  params=params)
		try: response = result.json()
		except: response = result.text
		return response

	def __getattr__(self, name):
		def wrapper(method='get', data={}, id=None, submethod=None):
			url = self._build_url(endpoint=name, id=id, submethod=submethod)
			response = self._request(url=url, method=method.lower(), data=data)
			if 'error' in response:
				raise PipeDriveError(response)
			return response
		return wrapper
		