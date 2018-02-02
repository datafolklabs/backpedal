.PHONY: all init test comply clean

all: init test test-coverage comply api-docs clean

init:
	pip install --upgrade -r requirements-dev.txt

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
	rm -rf doc/build
