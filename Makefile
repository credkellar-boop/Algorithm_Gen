.PHONY: install test clean format

install:
	pip install -r requirements.txt

test:
	python -m unittest discover -s tests

format:
	black generator/ tests/

clean:
	rm -rf __pycache__
	rm -rf generator/__pycache__
	rm -rf .pytest_cache
