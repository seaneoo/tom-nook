# =============== Workspace =============== #

install: # Set up and install the Pipenv virtual environment
	pipenv install --python 3.11

# ================== App ================== #

run: # Run the bot
	pipenv run python -m bot
