
FROM python:3.11-slim AS builder
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir fastapi uvicorn pydantic

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .
CMD ["uvicorn", "agentos_core.main:app", "--host", "0.0.0.0", "--port", "8000"]
