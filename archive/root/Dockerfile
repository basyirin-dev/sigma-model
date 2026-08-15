FROM python:3.12-slim

WORKDIR /app

# System deps for PyTorch
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Layer caching: copy requirements first, then install
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy code and config
COPY code/ code/
COPY experiments/ experiments/
COPY tests/ tests/
COPY scripts/ scripts/
COPY pyproject.toml .
COPY README.md .

# Install the package in development mode
RUN pip install -e ".[dev]"

CMD ["make", "test"]
