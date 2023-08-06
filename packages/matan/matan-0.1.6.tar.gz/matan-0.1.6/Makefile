SHELL := /bin/bash

upload:
	python3 -m build --sdist
	python3 -m twine upload dist/*
	rm -rf dist
