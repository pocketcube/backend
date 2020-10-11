FROM python:3.6-slim

COPY . /server
WORKDIR /server
RUN pip install -r requirements.txt

# ENV FLASK_APP run.py
EXPOSE 5000
CMD ["python", "run.py"]
