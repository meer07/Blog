# Blog

#Overview
Python/Djangoで制作しているブログの簡単なサンプルです。  

## Description

このサンプルアプリはPythonとDjangoで制作した、簡単なブログです。  
記事の投稿•管理はDjango標準の管理画面から行います。  
また、今回は以下の開発環境で制作しました。
- Python 2.7.8
- Django 1.7
- sqlite3

## Requirement

このブログでは特別なPythonライブラリは使用していません。(Pythonの標準ライブラリとDjangoのライブラリのみ)
ただし、Viewを生成する際に[BootStrap](http://getbootstrap.com)と[JQuery](http://jquery.com)を使用しています。

## Usage

- Djangoをインストールします  
sudo pip install django==1.7.1

- ダウンロードしたプロジェクトのディレクトリに移動し、データベースの初期設定をします。  
cd blog  
python manage.py migrate  
python manage.py createsuperuser  

- manage.pyを以下のように実行し、サーバーを動作させます。  
python manage.py runserver  

- 後は、以下のURLにアクセスするとブログのトップページが閲覧できます。  
http://127.0.0.1:8000/cms/blog/  

- また、管理画面にアクセスしたい場合は以下のURLにアクセスします。  
http://127.0.0.1:8000/admin/

## Licence

[MIT](http://opensource.org/licenses/mit-license.php)

## Author

[meer07](https://github.com/meer07)
