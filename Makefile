.PHONY: install-api-requirements
install-api-requirements:
	pip install -r backend/requirements.txt


.PHONY: format-api
format-api:
	black backend && \
	isort backend


PHONY: generate-openapi
generate-openapi:
	cd backend && python generate-openapi.py > openapi.json


.PHONY: run-api-locally
run-api-locally:
	cd backend && uvicorn main:fastapi_app --reload 