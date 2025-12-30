import requests

INTERPRETER_URL = "http://localhost:8000/execute"

code = "print('Hello, World!')"

response = requests.post(INTERPRETER_URL, json={"code": code}, timeout=30)