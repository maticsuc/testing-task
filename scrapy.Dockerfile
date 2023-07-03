FROM mcr.microsoft.com/playwright:v1.35.0-focal
RUN apt-get update
RUN apt-get install -y python3-pip
WORKDIR /
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps
COPY . .
CMD ["scrapy", "crawl", "sreality"]
