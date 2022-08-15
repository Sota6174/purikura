.PHONY: build-up
build-up: build up

.PHONY: build
build:
	docker-compose build

.PHONY: up
up:
	docker-compose up -d

.PHONY: exec
exec:
	docker-compose exec dev bash

.PHONY: down
down:
	docker-compose down
