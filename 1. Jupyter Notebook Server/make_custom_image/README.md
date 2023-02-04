## 블로그 작성글
블로그 링크: [주피터 노트북 서버 - 커스텀 이미지 사용](https://github.com/Seokii/Study-MLOps/tree/main/1.%20Jupyter%20Notebook%20Server)  
&nbsp;<br>

## 1. 도커파일 작성
- 다음과 같이 도커파일을 작성합니다.
```
FROM python:3.8

WORKDIR /home/jovyan

USER root

RUN pip install jupyter -U && pip install jupyterlab

RUN apt-get update && apt-get install -yq --no-install-recommends \
       apt-transport-https \
       build-essential \
       bzip2 \
       ca-certificates \
       curl \
       g++ \
       git \
       gnupg \
       graphviz \
       locales \
       lsb-release \
       openssh-client \
       sudo \
       unzip \
       vim \
       wget \
       zip \
       emacs \
       python3-pip \
       python3-dev \
       python3-setuptools \
       && apt-get clean && \
       rm -rf /var/lib/apt/lists/*

RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
RUN echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
RUN apt-get update
RUN apt-get install -y kubectl

RUN pip install jupyterlab && \
    jupyter serverextension enable --py jupyterlab --sys-prefix


# Install base python3 packages
RUN pip3 --no-cache-dir install \
    kubeflow-fairing==1.0.2 \
    msrestazure==0.6.4 \
    kfp==1.7.0 \
    scikit-learn==1.0.1 \
    mlflow==1.21.0 \
    dill==0.3.4 \
    numpy==1.20.0 \
    kfserving==0.4.0 \
    pandas==1.3.5 \
    xgboost \
    tensorflow==2.8.0 \
    torch==1.10.0


# Configure container startup
ARG NB_USER=jovyan

EXPOSE 8888

ENV NB_USER $NB_USER
ENV NB_UID=1000
ENV HOME /home/$NB_USER
ENV NB_PREFIX /

CMD ["sh", "-c", "jupyter lab --notebook-dir=/home/jovyan --ip=0.0.0.0 --no-browser --allow-root --port=8888 --LabApp.token='' --LabApp.password='' --LabApp.allow_origin='*' --LabApp.base_url=${NB_PREFIX}"]
```
&nbsp;<br>
- 아래의 예시처럼 도커 허브에 이미지 빌드 및 푸시를 진행합니다.
```
docker build -t seokii/kubeflow-jupyter-custom:0.0.3 .
docker push seokii/kubeflow-jupyter-custom:0.0.3
```
&nbsp;<br>

## 2. 주피터 노트북 서버 생성
- 아래의 예시처럼, 커스텀 이미지를 지정하여 주피터 노트북 서버를 생성합니다.
![image](https://user-images.githubusercontent.com/80209977/216770694-74a64cd6-004d-4659-ba3c-b4281eb17c1a.png)
