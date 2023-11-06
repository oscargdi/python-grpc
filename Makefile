.PHONY: format
format:
	pipenv run black .
	pipenv run isort .

.PHONY: lint
lint:
	pipenv run pylint .

.PHONY: protos
protos:
	pipenv run python -m grpc_tools.protoc -I ./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/com/grpc/**/*.proto

.PHONY: server
server:
	pipenv run python server.py

.PHONY: request
request:
	pipenv run python request.py
