FROM python:3.13.3-slim

WORKDIR /app
COPY ./src /app/src
COPY ./pyproject.toml .
RUN python3 -m pip install -e .

EXPOSE 8000

ENTRYPOINT ["dev2il-devops-app"]