.PHONY: install

run:
	@echo "Running Python"
	@python main.py

install:
	@echo "Installing package: $(package)"
	@pip install $(package)
	@if ! grep -i -q "^$(package)==`pip show $(package) | grep Version | awk '{print $$2}'`" requirements.txt 2>/dev/null; then \
		echo "$(package)==`pip show $(package) | grep Version | awk '{print $$2}'`" >> requirements.txt; \
		echo "Added to requirements.txt"; \
	else \
		echo "Package already in requirements.txt"; \
	fi

clean-pycache:
	@echo "Removing __pycache__ files"
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@echo "__pycache__ files removed"
