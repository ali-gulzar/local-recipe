.PHONY: install-api-requirements
install-api-requirements:
	pip install -r requirements.txt


.PHONY: format-api
format-api:
	black *.py && \
	isort *.py


.PHONY: generate-openapi
generate-openapi:
	source ./env-sample && python generate-openapi.py > app/openapi.json


.PHONY: run-api-locally
run-api-locally:
	uvicorn main:fastapi_app --reload 

.PHONY: export-variables
export-variables:
	source ./backend/environment-variables.sh