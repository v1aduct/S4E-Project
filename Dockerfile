FROM python:3.13.3

WORKDIR /app

RUN apt-get update && apt-get install -y curl unzip gcc libpq-dev && rm -rf /var/lib/apt/lists/*


RUN curl -sL https://github.com/projectdiscovery/katana/releases/download/v1.2.1/katana_1.2.1_linux_amd64.zip -o katana.zip \
    && unzip katana.zip \
    && mv katana /usr/local/bin/katana \
    && chmod +x /usr/local/bin/katana \
    && rm katana.zip


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_ENV =development
CMD ["flask", "run"]
