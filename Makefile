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

# ================ Docker ================ #

dc := docker compose -f docker/docker-compose.yml

docker-up: # (Re)build and start the Docker container
	$(dc) up -d --build

docker-down: # Stop and remove the Docker container
	$(dc) down

docker-start: # Start the Docker container
	$(dc) start

docker-stop: # Stop the Docker container
	$(dc) stop

docker-build-bot: # (Re)build the bot service without building dependencies
	$(dc) up -d --force-recreate --no-deps --build bot
