FROM python:3.13-slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y make && rm -rf /var/lib/apt/lists/*

RUN pip install uv

COPY . /app/

RUN make init
RUN uv sync --group inference

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
