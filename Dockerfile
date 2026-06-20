FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies, including Rust toolchain for the high-speed backend
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add Rust to PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Compile the Rust extensions (if present) before running
RUN if [ -f "Cargo.toml" ]; then cargo build --release; fi

# Define the command to run your application
CMD ["python", "run.py"]
