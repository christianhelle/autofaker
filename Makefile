.PHONY: prepare debug release test package

all: debug release package test package

prepare:
	pip install -r requirements.txt

debug: prepare
	pip install -e .

release: prepare
	python -m pip install --upgrade pip
	pip install setuptools wheel twine

package:
	python -m build

test: debug
	pytest -v --cov --cov-report=xml --cov-report=term-missing
