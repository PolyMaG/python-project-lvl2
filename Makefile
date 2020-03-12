install:
		poetry install

lint:
		poetry run flake8 gendiff

test:
		poetry run pytest --cov=gendiff tests/

.PHONY: install lint test