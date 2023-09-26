FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/uploads

EXPOSE 6969

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "6969"]