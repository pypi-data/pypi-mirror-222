from aiohttp import web
from aiohttp.web_request import Request

async def wh(request: Request):
    data = await (request.json() if request.content_type == 'application/json' else request.text())
    print(data)
    return web.Response(text="Ok")

app = web.Application()
app.add_routes([web.get('/', wh)])
web.run_app(app)
