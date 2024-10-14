install: 
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vvv --cov=app test_app.py

format:
	black *.py


lint:
	pylint --disable=R,C app.py

all: install lint test format
