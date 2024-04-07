FROM python:3.11-slim
LABEL authors="{{ cookiecutter.github_username }}"
LABEL org.opencontainers.image.source=https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}

WORKDIR /code

EXPOSE 8080

COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./server.py /code/server.py

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "4"]