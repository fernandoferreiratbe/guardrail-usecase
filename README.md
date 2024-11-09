## Simple code to illustrate a basic use case in clean arch

### Setup on Mac OS

```bash
python -m venv venv
. .venv/bin/activate

pip install -r requirements.txt
```


### Run unit test and code coverage
```bash
pytest --cov=. --cov-report=term-missing tests
```