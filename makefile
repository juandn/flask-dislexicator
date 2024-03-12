start:
	docker compose up -d
	docker compose logs -f
stop:
	docker compose down
logs:
	docker compose logs -f
restart:
	docker compose down
	docker compose up
