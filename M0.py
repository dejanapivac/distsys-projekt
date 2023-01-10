import asyncio
import json

import aiosqlite
from aiohttp import web

routes = web.RouteTableDef()


async def get_fake_db_dataset():
    async with aiosqlite.connect("projektdb.db") as db:
        async with db.execute("SELECT COUNT(*) FROM githubLinkovi") as cur:
            result = await cur.fetchall()
            if result[0][0] == 0:
                with open("file-000000000040.json", "r") as f:
                    data = []
                    for index, json_object in enumerate(f):
                        if index == 10000:
                            break
                        json_dict = json.loads(json_object)
                        repo_name = json_dict["repo_name"].split("/")[1]
                        user_name = json_dict["repo_name"].split("/")[0]
                        file_name = json_dict["path"].split("/")[-1]
                        content = json_dict["content"]
                        gh_link = "https://github.com/" + user_name + "/" + repo_name
                        data.append((user_name, gh_link, file_name, content))
                    await db.executemany("INSERT INTO githubLinkovi(username, ghlink, filename, content) VALUES (?, ?, ?, ?)",
                                   data)
                print("ja")
                await db.commit()

def get_list_of_id(max_index):
    list = []
    for i in range(max_index, max_index+100):
        list.append(i)
    return list


@routes.get("/linkovi")
async def get_linkovi_db(request):
    max_index = int(request.query["max_index"])
    async with aiosqlite.connect("projektdb.db") as db:
        index_list = get_list_of_id(max_index)
        async with db.execute("SELECT * FROM githubLinkovi WHERE id IN {}".format(tuple(index_list))) as cur:
            user_names = []
            githubLinks = []
            fileNames = []
            content = []
            async for row in cur:
                user_names.append(row[1])
                githubLinks.append(row[2])
                fileNames.append(row[3])
                content.append(row[4])
            print(user_names)
            data = {"usernames": user_names, "githubLinks": githubLinks, "filenames": fileNames, "content": content}
        return web.json_response({"service": 0, "data": data}, status=200)


app = web.Application()
asyncio.run(get_fake_db_dataset())

app.router.add_routes(routes)

web.run_app(app)
