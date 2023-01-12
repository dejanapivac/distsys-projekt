import aiofiles as aiofiles
from aiohttp import web

routes = web.RouteTableDef()

global temp_codes
temp_codes = []


@routes.post("/gatherData")
async def gather_data(request):
    try:
        json_request = await request.json()
        temp_codes.extend(json_request)

        if len(temp_codes) > 10:
            for code in temp_codes:
                filename = code['filename']
                code = code['content']
                async with aiofiles.open(f'files/{filename}', mode='w') as f:
                    await f.write(code)
            temp_codes.clear()
        return web.json_response({"service": 5, "status": "ok"}, status=200)
    except Exception as e:
        return web.json_response({"service": 5, "status": "failed", "message": str(e)}, status=500)


app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port=8084)
