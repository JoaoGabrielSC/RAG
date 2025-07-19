.PHONY: install

run:
	@echo "Running Python"
	@python main.py --dataset_path=$(dataset_path)

install:
	@echo "Installing package: $(pkg)"
	@pip install $(pkg)
	@if ! grep -i -q "^$(pkg)==`pip show $(pkg) | grep Version | awk '{print $$2}'`" requirements.txt 2>/dev/null; then \
		echo "$(pkg)==`pip show $(pkg) | grep Version | awk '{print $$2}'`" >> requirements.txt; \
		echo "Added to requirements.txt"; \
	else \
		echo "Package already in requirements.txt"; \
	fi

clean-pycache:
	@echo "Removing __pycache__ files"
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@echo "__pycache__ files removed"
