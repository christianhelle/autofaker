.PHONY: prepare debug release test

all: debug release package test

prepare:
	pip install -r requirements.txt

debug: prepare
	pip install --no-build-isolation -e .

release: prepare
	python -m pip install --upgrade pip
	pip install setuptools wheel twine

package:
	python setup.py sdist bdist_wheel

test: debug
	pytest -v --cov --cov-report=xml --cov-report=term-missing
