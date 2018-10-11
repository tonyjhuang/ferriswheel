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