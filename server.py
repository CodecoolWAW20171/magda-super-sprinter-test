from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()
    headers = data_handler.DATA_HEADER
    return render_template('list.html', user_stories=user_stories, headers=headers)


@app.route('/add')
def route_add():
    return render_template('add.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
