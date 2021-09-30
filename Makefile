.PHONY: dev test comply comply-fix clean virtualenv deploy

dev:
	docker-compose up -d
	docker-compose exec backpedal pip install -r requirements-dev.txt
	docker-compose exec backpedal python setup.py develop
	docker-compose exec backpedal /bin/bash

test:
	python -m pytest -v \
		--cov=backpedal \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/

comply:
	flake8 backpedal/ tests/

comply-fix:
	autopep8 -ri backpedal/ tests/

clean:
	find . -name '*.py[co]' -delete
	rm -rf doc/build/ env/

virtualenv:
	virtualenv --prompt="|> backpedal <| " env/
	env/bin/pip install --upgrade -r requirements-dev.txt

dist: clean
	rm -rf dist/*
	python setup.py sdist
	python setup.py bdist_wheel

dist-upload:
	twine upload dist/*
