import requests


class PipeDriveError(Exception):
    def __init__(self, response):
        self.response = response

    def __str__(self):
        return self.response.get('error', 'No error provided.')


class HttpMethod(object):
    def __init__(self, api_token, api_path, endpoint):
        self.api_token = api_token
        self.api_path = api_path
        self.endpoint = endpoint

    def __getattr__(self, method):
        def wrapper(data={}, id=None, submethod=None):
            url = self._build_url(endpoint=self.endpoint, id=id, submethod=submethod)
            response = self._request(url=url, method=method, data=data)
            if 'error' in response:
                raise PipeDriveError(response)
            return response
        return wrapper

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
        try: 
            if 'data' in result.json():
                response = result.json()['data']
            else:
                response = result.json()
        except: 
            response = result.text
        finally:
            return response        


class PipeDrive(object):
    def __init__(self, api_token, version='v1'):
        self.api_token = api_token
        self.api_path = "https://api.pipedrive.com/%s/" % version

    def __getattr__(self, endpoint):
        api_token = self.api_token
        api_path = self.api_path
        return HttpMethod(api_token, api_path, endpoint)
