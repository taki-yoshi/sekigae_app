FROM python:3
ARG PROJECT_DIR
# RUN mkdir -p /sekigae-python-dir
RUN mkdir -p /${PROJECT_DIR}/docker
COPY ./ /${PROJECT_DIR}/docker

# 作業ディレクトリをworkspaceに変更
WORKDIR /${PROJECT_DIR}

# pipのアップデート
RUN pip install --upgrade pip
# pythonパッケージをインストール
RUN pip install -r ./docker/requirements.txt
