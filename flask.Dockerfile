FROM python:3.9
WORKDIR /
ENV FLASK_APP=main.py
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]