FROM ubuntu:jammy

SHELL ["/bin/bash", "-c"]
RUN apt update -y && \
    # Install python base dependencies
    apt install -y python3-pip python3-venv curl lsb-release libicu-dev && \
    # Create development user
    useradd -s /bin/bash -d /home/dev-user -m dev-user && \
    # Install Azure Function Core Tools
    curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg && \
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-$(lsb_release -cs)-prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list && \
    apt update && \
    apt install -y azure-functions-core-tools-4 && \
    # Clean up packages
    apt clean all

USER dev-user
WORKDIR /home/dev-user
COPY requirements.txt /home/dev-user/requirements.txt

SHELL ["/bin/bash", "-c"]
RUN python3 -m venv web-dev && \
    source web-dev/bin/activate && \
    pip install -r requirements.txt && \
    echo -e "\nsource ${HOME}/web-dev/bin/activate" >> ${HOME}/.bashrc && \
    rm requirements.txt

WORKDIR /app