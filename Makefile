# =============== Workspace =============== #

install: # Set up and install the Pipenv virtual environment
	pipenv install --python 3.11

format: # Format the code with Black
	pipenv run black bot

lint: # Lint the code with Pylint
	pipenv run pylint bot

format-lint: # Format and lint the code
	make format
	make lint

# ================== App ================== #

run: # Run the bot
	pipenv run python -m bot
