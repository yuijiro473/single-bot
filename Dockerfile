FROM python:3.9-slim-buster
ENV PYTHONPATH "${PYTHONPATH}:/app"

# Add system dependencies for mysqlclient
RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev gcc

WORKDIR /app

COPY ./app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

CMD ["streamlit", "run", "single-bot/main.py"]