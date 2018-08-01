clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +

clean-shared-lib:
	find . -name '*.so' -exec rm -f {} +
	find . -name '*.dylib' -exec rm -f {} +
	
clean-cache:
	find . -name '__pycache__' -exec rm -rf {} +
	rm -rf .pytest_cache

clean-build:
	rm -rf build/
	rm -rf dist/
	find . -name '*.egg-info' -exec rm -rf {} +

clean: clean-pyc clean-shared-lib clean-cache clean-build

isort:
	sh -c "isort --skip-glob=.tox --recursive . "

lint:
	tox -e check

test: clean-pyc
	tox -v --workdir /tmp/tox

test-pyenv:
	pyenv local 3.4.3 3.5.4 3.6.4 pypy-5.7.1 pypy3.5-5.8.0 && tox -v --workdir /tmp/tox
