## How to run project:
    1.Download json file: [zip file](https://huggingface.co/datasets/codeparrot/codeparrot-clean/resolve/main/file-000000000040.json.gz)
    2.Database:
           CREATE TABLE githubLinkovi (
                 id       INTEGER PRIMARY KEY AUTOINCREMENT
                             NOT NULL,
            username TEXT    NOT NULL,
            ghlink   TEXT    NOT NULL,
            filename TEXT    NOT NULL,
            content  TEXT    NOT NULL
        );

    3.Run all 5 services (M0, M1, WTD, WTW, M0)
    4.GET request at http://0.0.0.0:8081/getData