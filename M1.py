import asyncio

import aiohttp
from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/getData")
async def get_data(request):
    try:
        data = []
        async with aiohttp.ClientSession() as session:
            for number in range(1, 10001, 100):
                data.append(asyncio.create_task(session.get(f"http://127.0.0.1:8080/linkovi?max_index={number}")))
            final_results = await asyncio.gather(*data)
            final_results = [await x.json() for x in final_results]
            print(final_results)

        return web.json_response({"status": "ok"}, status=200)
    except Exception as e:
        return web.json_response({"status": "failed", "message": str(e)}, status=500)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8081)
