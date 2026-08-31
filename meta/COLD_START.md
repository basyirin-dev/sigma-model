# Cold-Start Bootstrap Guide (RPF v2.0)

This document provides deterministic, step-by-step instructions to initialize and bootstrap this repository from a fresh clone on CachyOS / Arch Linux or any Linux workstation.

---

## One-Command Bootstrap (Quick Start)

Run the following command in your terminal:
```fish
paru -S --noconfirm python python-pip git-lfs && python3 -m venv hbar_env && source hbar_env/bin/activate.fish && pip install -e . && python scripts/check_phase_exit.py P00 && pi doctor
```

---

## Detailed Step-by-Step Procedure

### 1. System-Level Dependencies (CachyOS / Arch)
```fish
paru -S --noconfirm \
    base-devel \
    python \
    python-pip \
    git \
    git-lfs \
    docker \
    quarto-cli \
    graphviz
```

### 2. Python Environment Setup
```fish
# Create virtual environment if missing
if not test -d hbar_env
    python3 -m venv hbar_env
end

# Activate virtual environment in fish
source hbar_env/bin/activate.fish

# Upgrade packaging tools and install workspace dependencies
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
pip install -e .
```

### 3. Pi Agent Ecosystem Verification
Ensure global and project-local Pi packages and extensions are healthy:
```fish
pi doctor
pi list
```

### 4. Governance & Phase Check
Verify current phase readiness and generate compliance matrices:
```fish
python scripts/generate_compliance_matrix.py --standards planning/standards.md --output planning/compliance-matrix.md
python scripts/check_phase_exit.py P00
```

### 5. Docker Clean-Room Build (Optional for P00-P09, Mandatory for P10)
```fish
docker build -t sigma-rpf-cleanroom:latest .
```
