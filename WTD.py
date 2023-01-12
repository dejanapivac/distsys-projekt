import aiohttp
from aiohttp import web

from util import filter_json

routes = web.RouteTableDef()


@routes.post("/filterUsernamesD")
async def filter_usernames(request):
    try:
        json_data = await request.json()
        filtered = filter_json(json_data["data"], "d")
        async with aiohttp.ClientSession() as session:
            message = await session.post("http://127.0.0.1:8084/gatherData", json=filtered)
            message = await message.json()
        return web.json_response({"service": "WTD", "status": message}, status=200)
    except Exception as e:
        return web.json_response({"status": "failed", "message": str(e)}, status=500)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8083)
