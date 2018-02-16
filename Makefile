.PHONY: dev test comply comply-fix clean virtualenv deploy

dev:
	docker-compose up -d
	docker-compose exec backpedal /bin/ash

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

deploy: test comply
	python setup.py sdist upload
