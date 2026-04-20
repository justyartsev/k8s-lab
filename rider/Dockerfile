FROM python:3.11-slim     
WORKDIR /rider
RUN apt-get update && apt-get install -y redis-tools && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY rider.py .
CMD ["python", "rider.py"]