.PHONY: install
install: ## Installs the project using uv
	@echo "Creating virtual environment using uv"
	@uv sync
	@uv run pre-commit install

.PHONY: test
test: ## Run the tests in the 'tests' directory
	@uv run python -m unittest discover -s ./tests/ -p "*.py"
