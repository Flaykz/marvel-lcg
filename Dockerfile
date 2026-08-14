FROM node:22-bookworm-slim AS frontend
WORKDIR /app
COPY public/js ./public/js
RUN npm install -g typescript && cd public/js && tsc
FROM python:3.14-slim-bookworm
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY --from=frontend /app/public/js /app/public/js
EXPOSE 2345
CMD ["python", "main.py"]
