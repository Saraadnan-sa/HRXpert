.PHONY: dev test lint

dev:
	conda env create -f environment.yml || echo "Env already exists"
	conda activate ai-env && pre-commit install

test:
	pytest

lint:
	black .
	isort .
	flake8 .
