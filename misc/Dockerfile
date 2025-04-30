# Base image
FROM python:3.11-slim
FROM rocker/r-ver:4.3.1

# System dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    git \
    curl \
    wget \
    unzip \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install pandas matplotlib seaborn

RUN R -e "install.packages(c('tidyverse', 'ggplot2'), repos='http://cran.rstudio.com/')"

# Set the working directory
WORKDIR /ml_studies

# Copy the current directory contents into the container at /ml_studies
COPY . .


