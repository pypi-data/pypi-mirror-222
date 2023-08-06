from aiohttp import ClientSession, ClientResponse

class Waba360:
    BASE_URL = 'https://waba.360dialog.io/v1/'
    namespace: str

    def __init__(self, apikey: str, namespace: str):
        self.headers = {
            "Content-Type": "application/json",
            "D360-Api-Key": apikey,
        }
        self.namespace = namespace
        self.session = ClientSession(headers=self.headers)

    async def __handle_resp(self, response: ClientResponse):
        self.response = response
        if not str(response.status).startswith('2'):
            raise Exception(response, response.status, await response.text())
        try:
            return (r := await response.json()).get('data', r)
        except ValueError:
            txt = await response.text()
            raise Exception(f'Invalid Response: {txt}')

    async def _get(self, endpoint: str, params: dict = None):
        async with self.session.get(self.BASE_URL + endpoint, params=params) as resp:
            return await self.__handle_resp(resp)

    async def _post(self, endpoint: str, data: dict = None, params: dict = None):
        async with self.session.post(self.BASE_URL + endpoint, params=params, json=data) as resp:
            return await self.__handle_resp(resp)

    """ PUBLIC METHS """
    async def close(self):
        await self.session.close()

    async def set_wh(self, url: str):
        res = await self._post('configs/webhook', {"url": url})
        return res

    async def send_msg(self, phone: str, msg: str):
        prms = {
            "recipient_type": "individual",
            "to": phone,
            "type": "text",
            "text": {"body": msg}
        }
        res = await self._post('messages', prms)
        return res

    async def send_tmpl_msg(self, phone: str, tmpl_name: str):
        prms = {
            "to": phone,
            "type": "template",
            "category": "UTILITY",
            "template": {
                "namespace": self.namespace,
                "name": tmpl_name,
                "language": {"policy": "deterministic", "code": "es"},
                "components": []
            }
        }
        res = await self._post('messages', prms)
        return res
