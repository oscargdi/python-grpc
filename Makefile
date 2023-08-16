.PHONY: format
format:
	pipenv run black .
	pipenv run isort .

.PHONY: lint
lint:
	pipenv run pylint .
