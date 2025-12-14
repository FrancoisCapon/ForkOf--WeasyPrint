FROM public.ecr.aws/x8v8d7g8/mars-base:latest

# build-essential \
RUN apt-get update && apt-get install -y --no-install-recommends \
    ghostscript \
    libcairo2 libcairo2-dev \
    libpango-1.0-0 libpango1.0-dev \
    libgdk-pixbuf2.0-0 libgdk-pixbuf2.0-dev \
    libffi-dev libglib2.0-0 libglib2.0-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN pip install pytest
RUN pip install --user --no-cache-dir -e .

CMD ["/bin/bash"]

# docker build -f Dockerfile -t shipd/weasyprint:lab-01 .