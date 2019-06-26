FROM ubuntu:18.04

#ENV http_proxy=http://IP_OU_DNS_DO_SERVIDOR_PROXY:3128
#ENV https_proxy=http://IP_OU_DNS_DO_SERVIDOR_PROXY:3128

RUN apt update && apt install -y python3 python3-pip && apt clean
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir watcher_one
WORKDIR /watcher_one
RUN mkdir watch_folder

COPY ./file-copy/ ./file-copy
RUN python3 -m pip install --upgrade setuptools pip wheel

COPY ./patience/ ./patience
RUN pip3 install ./patience

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

ENV WATCH_FOLDER=/watcher_one/watch_folder
ENV DESTINATION_FOLDER=/mnt/Novo_Ateme/input
ENV TIMEOUT=60
ENV WATCHDIR=/watcher_one/watch_folder
ENV TZ=America/Sao_Paulo

CMD ["python3", "/watcher_one/file-copy/run.py"]
