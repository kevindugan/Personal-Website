FROM python:3.13-slim-bookworm

RUN apt update && \
    apt install -y curl lsb-release gnupg libicu-dev && \
    # Install Azure Functions
    curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg && \
    echo "deb [arch=amd64] https://packages.microsoft.com/debian/$(lsb_release -rs 2>/dev/null | cut -d'.' -f 1)/prod $(lsb_release -cs 2>/dev/null) main" > /etc/apt/sources.list.d/dotnetdev.list && \
    apt update && \
    apt install -y azure-functions-core-tools-4 && \
    apt clean all && \
    # Create development user
    useradd -s /bin/bash -d /home/dev-user -m dev-user

WORKDIR /app
USER dev-user
