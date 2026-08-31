# RPF v2.0 Clean-Room Docker Container
# Multi-stage build with Python 3.11 and Julia LTS

FROM python:3.11-slim-bookworm AS base

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    JULIA_VERSION=1.10.4

# Install base system dependencies and build essentials
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    wget \
    git \
    git-lfs \
    libopenblas-dev \
    liblapack-dev \
    pkg-config \
    graphviz \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Julia 1.10 LTS
RUN wget -q https://julialang-s3.julialang.org/bin/linux/x64/1.10/julia-${JULIA_VERSION}-linux-x86_64.tar.gz && \
    tar -xzf julia-${JULIA_VERSION}-linux-x86_64.tar.gz -C /opt/ && \
    ln -s /opt/julia-${JULIA_VERSION}/bin/julia /usr/local/bin/julia && \
    rm julia-${JULIA_VERSION}-linux-x86_64.tar.gz

# Pre-install DifferentialEquations.jl in Julia
RUN julia -e 'using Pkg; Pkg.add(["DifferentialEquations", "OrdinaryDiffEq", "LinearAlgebra", "StaticArrays"]); Pkg.precompile();'

# Set working directory
WORKDIR /workspace

# Install core scientific Python stack with pinned versions
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir \
    numpy==1.26.4 \
    scipy==1.13.1 \
    pandas==2.2.2 \
    matplotlib==3.8.4 \
    seaborn==0.13.2 \
    pyyaml==6.0.1 \
    pytest==8.2.2 \
    torch==2.3.1 \
    jax==0.4.28 \
    jaxlib==0.4.28 \
    diffrax==0.5.1 \
    pyhessian==0.1.0 \
    geomstats==2.7.0 \
    giotto-tda==0.6.0 \
    transformer-lens==1.14.0 \
    quarto-cli \
    snakemake==7.32.4

# Copy repository code
COPY . /workspace

# Install package in editable mode
RUN pip install --no-cache-dir -e . || true

# Default entrypoint runs phase exit verification
CMD ["python", "scripts/check_phase_exit.py", "P10"]
