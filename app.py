from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for,make_response
import subprocess
from crawl import crawl
from cli import GetStdout



flaskapp = Flask(__name__)

database = SQLAlchemy()
flaskapp.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@db:5432/testdb'
database.init_app(flaskapp)


class WebPage(database.Model):
    __tablename__ = 'webpages'
    
    id = database.Column(database.Integer, primary_key=True)
    url = database.Column(database.String(255), nullable=False, unique=True)
    subURLCount =  database.Column(database.Integer)
    created_at = database.Column(database.DateTime, server_default=database.func.now())
    
    def __repr__(self):
        return f'<WebPage {self.url}>'

    



@flaskapp.route('/AddWebPage', methods=['POST'])
def add_webpage():
    data = request.json
    url = data.get('url')
    crawlReturn = crawl(url)
    subURLCount = crawlReturn[1]
    if url and subURLCount:
        webpage = WebPage(
            url = url,
            subURLCount = subURLCount
        )
        database.session.add(webpage)
        database.session.commit()
        return make_response(
            {"message":"URL added",
             "URLS found":crawlReturn[0]},
            200
        )
    return make_response(
        {"message":"Data was not entered correctly"},
        500
    )
    
@flaskapp.route('/GetCommandOutput', methods=['POST'])
def get_command():
    data = request.json
    command = data.get('command')
    output = GetStdout(command)
    return make_response(
        {"CLI Output:":output.decode('utf-8')},
        200
    )

if __name__ == "__main__":
    with flaskapp.app_context():
        database.create_all()
    flaskapp.run(host="0.0.0.0", port=5000, debug=True)

    



