import asyncio
from aiohttp import ClientSession
from bs4 import BeautifulSoup as bs


class Asynchronous:
    async def get(self, url, session):
        async with session.get(url) as response:
            assert response.status == 200
            text = await response.read()
            return bs(text.decode('utf-8'), 'html.parser')

    async def request(self, urllist):
        tasks = []

        async with ClientSession as session:
            for i, url in enumerate(urllist):
                task = asyncio.ensure_future(self.get(url, session))
                tasks.append(task)
            responses = await asyncio.gather(*tasks)
            return responses

