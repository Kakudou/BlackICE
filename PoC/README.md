1) setup your python venv:
```bash
python3.13 -m venv .venv --prompt=PoC
source .venv/bin/activate
```

2) install requirements:
```bash
python -m pip install -e .
```

3) Then migrate the database for a first time:
```bash
evennia migrate
```

4) Then to run the server:
```bash
evennia start
```

5) Then to stop the server:
```bash
evennia stop
```


