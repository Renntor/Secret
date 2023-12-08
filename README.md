Creating a secret
---
___
A project to create and an opportunity to share with someone
___
To start the project you need to:
1) install dependencies 
2) configure .env
___

Command to start a container in Docker
```sh
docker-compose up --build
```
___
### Teach Stack
___
- [Docker](https://www.docker.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/)
___
API
---
| Method | URL                     | Description    |
|--------|-------------------------|----------------|
| `POST` | `/generate`             | Create secret. |
| `POST` | `/secrets/{secret_key}` | Get secret.    |

## Examples
### Create secret
/generate
```
{
    "secret": "My secret",
    "password": "my_password"
}
```
data to return
```
{
    "secret_key": "hgodsn498wh45tbwg89075bwg5459"
}
```
### Get secret
/secrets/hgodsn498wh45tbwg89075bwg5459
```
{
    "password": "my_password"
}
```
data to return
```
{
    "secret": "My secret"
}
```
___
Tests
---
The tests are written in pytest. To run them, run the command:
```sh
pytest
```
```
Name                  Stmts   Miss  Cover
-----------------------------------------
app/__init__.py           0      0   100%
app/main.py               5      0   100%
app/test_main.py         13      0   100%
config/__init__.py        0      0   100%
config/db.py              9      0   100%
models/__init__.py        0      0   100%
models/secret.py         11      0   100%
routers/__init__.py       0      0   100%
routers/secret.py        27      0   100%
schemas/__init__.py       0      0   100%
schemas/secret.py         6      1    83%
service/__init__.py       0      0   100%
service/service.py       15      0   100%
-----------------------------------------
TOTAL                    86      1    99%
```
