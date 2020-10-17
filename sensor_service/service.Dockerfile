FROM python:3.6-slim

COPY . /server
WORKDIR /server
RUN pip install -r requirements.txt

CMD ["python", "run.py"]
