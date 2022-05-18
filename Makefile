.PHONY: install-api-requirements
install-api-requirements:
	pip install -r requirements.txt

.PHONY: format-api
format-api:
	black *.py && \
	isort *.py

.PHONY: generate-openapi
generate-openapi:
	source ./env-sample && python generate-openapi.py > application/openapi.json

.PHONY: run-api-locally
run-api-locally:
	uvicorn main:app --reload 

.PHONY: deploy
deploy:
	deta deploy

.PHONY: export-variables
export-variables:
	source environment-variables.sh