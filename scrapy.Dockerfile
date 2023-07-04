FROM mcr.microsoft.com/playwright:v1.35.0-focal
COPY . .
WORKDIR /
RUN apt-get update && apt-get install -y python3-pip
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN playwright install --with-deps
CMD ["scrapy", "crawl", "sreality"]