FROM python:3.10

RUN apt-get update && \
    apt-get -y install freetds-dev


ENV FLASK_APP sandbox
ENV FLASK_ENV development

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]
