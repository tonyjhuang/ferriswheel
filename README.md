See flaskr/__init__.py for app init logic.

Uses:
- `requests`: for http requests
- `bs4`: for parsing html text
- `Flask-RESTful`: for REST api hookups
- `Whoosh`: for data indexing and searching

To run:

```bash
cd {PROJECT_DIR}
mkvirtualenv {PROJECT_NAME}
pip install -r requirements.txt
export FLASK_APP=flaskr
flask run
```

To use:
```bash
curl http://127.0.0.1:5000/search?query=hanks,spielberg
```

TODO: tests :P