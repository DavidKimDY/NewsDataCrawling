import aiohttp

class HttpResponse:
    def __init__(self, response):
        self.response = response

    def check_response(self, response):
        status = response.status
        if 200 != status:
            raise