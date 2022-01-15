include .env
export $(shell sed 's/=.*//' .env)

clean:

build:
	@docker image rm --force $(APP_NAME_BACKEND):$(APP_VERSION) || true
	@docker build -t $(APP_NAME_BACKEND):$(APP_VERSION) --build-arg VERSION=$(IMAGE_VERSION) .
