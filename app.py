from . import app, db
from flask import request, redirect, url_for,make_response
from .models import WebPage
import subprocess
from . import crawl


@app.route('/AddWebPage', methods=['POST'])
def add_webpage():
    data = request.json
    url = data.get('url')
    subURLCount = crawl(url)[1]
    if url and subURLCount:
        webpage = WebPage(
            url = url,
            subURLCount = subURLCount
        )
        db.session.add(webpage)
        db.session.commit()
        return make_response(
            {"message":"URL added"},
            200
        )
    return make_response(
        {"message":"Data was not entered correctly"},
        500
    )

    



