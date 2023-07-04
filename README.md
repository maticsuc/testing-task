# Testing task
Use scrapy framework to scrape the first 500 items (title, image url) from sreality.cz (flats, sell) and save it in the Postgresql database. Implement a simple HTTP server in Python and show these 500 items on a simple page (title and image) and put everything to single docker-compose command so that "docker-compose up" can be ran in the Github repository and scraped ads are shown on http://127.0.0.1:8080 page. The task is not complex but you need to use different technologies to solve the task - it shows your problem-solving and coding skills.

## Frameworks used
- [scrapy](https://scrapy.org/) framework with [playwright](https://github.com/scrapy-plugins/scrapy-playwright) used to scrape 500 items from [sreality.sz](https://www.sreality.cz/)
- [postgresql](https://www.postgresql.org/) database used to save scraped items
- [Flask](https://flask.palletsprojects.com/en/2.3.x/) framework used for displaying the scraped items

## Docker
`docker-compose up` to run all 3 services. Dockerfiles:
- [scrapy](scrapy.Dockerfile)
- [postgresql](postgresql.Dockerfile)
- [flask](flask.Dockerfile)

## Issues - TODO
- ~~Scrapy spider sometimes scrapes less than 500 items due to not finding the next page link in time?~~
    - Fixed with Scrapy's [AutoThrottle](https://docs.scrapy.org/en/latest/topics/autothrottle.html) extension
- In docker-compose it is currently implemented for the Flask to run after scrapy spider finishes, otherwise the spider hangs and fails to scrape
    - Manually run the flask-app in Docker GUI to see ads on http://127.0.0.1:8080 while the spider scrapes items