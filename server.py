from flask import Flask, render_template, request, redirect, url_for, session

import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_story()
    headers = ['ID', 'TITLE', 'USER STORY', 'ACCEPTANCE CRITERIA', 'BUSINESS VALUE', 'ESTIMATION', 'STATUS']
    return render_template('list.html', user_stories=user_stories, headers=headers)


@app.route('/add-story', methods=['GET', 'POST'])
def route_add():
    statuses = data_handler.STATUSES
    story = None
    if request.method == 'GET':
        return render_template('add-story.html', statuses=statuses)
    else:  # czy to jest prawidłowo czy nie powinno byc ze wskazaniem na post?
        id = request.form['id']
        title = request.form['title']
        user_story = request.form['user_story']
        acceptance_criteria = request.form['acceptance_criteria']
        business_value = request.form['business_value']
        estimation = request.form['estimation']
        status = request.form['status']
        story = {'id': id, 'title': title, 'user_story': user_story, 'acceptance_criteria': acceptance_criteria,
                 'business_value': business_value, 'estimation': estimation, 'status': status}
        data_handler.append_stories_in_file(story)
        return redirect('/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
