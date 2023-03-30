.PHONY: install test build deploy

install:
	poetry install

test:
	poetry run pytest tests/

build:
	docker build -t my_project .

deploy:
	kubectl apply -f deployment.yaml

