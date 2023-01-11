import asyncio
import json

import aiohttp
import pandas as pd

import aiosqlite
from aiohttp import web

from Projekt_o1_kod.util import filter_json

routes = web.RouteTableDef()


@routes.post("/filterUsernamesW")
async def filter_usernames(request):
    try:
        json_data = await request.json()
        filtered = filter_json(json_data["data"], "w")
        async with aiohttp.ClientSession() as session:
            await session.post("http://127.0.0.1:8084/gatherData", json=filtered)
        return web.json_response({"service": "WTW", "status": "ok"}, status=200)
    except Exception as e:
        return web.json_response({"status": "failed", "message": str(e)}, status=500)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8082)
