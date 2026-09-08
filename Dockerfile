FROM python:3.11-slim
WORKDIR /app
RUN useradd -m -u 10001 appuser
COPY pyproject.toml README.md LICENSE ./
COPY src ./src
RUN pip install --no-cache-dir .
USER appuser
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health')"
CMD ["uvicorn", "agentforge.api:app", "--host", "0.0.0.0", "--port", "8000"]
