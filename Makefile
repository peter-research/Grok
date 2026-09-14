.PHONY: check test

check: test
	python3 grok.py check

test:
	python3 -m unittest -v test_grok.py
