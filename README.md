# sekigae_app

<div id="top"></div>

## 使用技術一覧

<!-- シールド一覧 -->
<!-- 該当するプロジェクトの中から任意のものを選ぶ-->
- フロントエンドフレームワーク
  - Streamit
- バックエンドフレームワーク
  - FastAPI
## 目次

1. [プロジェクトについて](#プロジェクトについて)
2. [環境](#環境)
3. [開発環境構築](#開発環境構築)


## プロジェクト名

<a href="https://sekigaeapp.streamlit.app/">席替えアプリ<strong></strong></a>
<!-- プロジェクトについて -->

## プロジェクトについて
各生徒の席の希望順をもとに，DAアルゴリズムで席替えを行うアプリ


<!-- プロジェクトの概要を記載 -->

<p align="right">(<a href="#top">トップへ</a>)</p>

## 環境

<!-- 言語、フレームワーク、ミドルウェア、インフラの一覧とバージョンを記載 -->

| 言語・フレームワーク  | バージョン |
| --------------------- | ---------- |
| Python               |      |
| FastAPI(バックエンド)                |     |
| Streamit(フロントエンド)              |            |

<p align="right">(<a href="#top">トップへ</a>)</p>

## 開発環境構築

<!-- コンテナの作成方法、パッケージのインストール方法など、開発環境構築に必要な情報を記載 -->
1. `docker-compose up -d`でコンテナ作成，`docker exec -it コンテナ名 bash`でコンテナ内ログイン
2. `streamlit run app.py`でStreamitの立ち上げ
3. `uvicorn main:app --reload`でFastAPIの立ち上げ

<p align="right">(<a href="#top">トップへ</a>)</p>
