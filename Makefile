install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest -vv --cov=gendiff --cov-report xml tests/

.PHONY: install lint test