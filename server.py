# file to handling server and passing data between user and database
from flask import Flask, render_template, request, redirect, url_for, session
import data_handler
import common

app = Flask(__name__)


# można wyrzucić stąd główną stronę i zrobić stronę wyboru projektu albo
# logowanie jako główną. Do przemyślenia
@app.route('/')
@app.route('/list')
def route_list():
    """
    Function supports main page and /list page
    :return: main page with list of stories
    """

    user_stories = data_handler.get_all_user_story()
    headers = ['ID', 'TITLE', 'USER STORY', 'ACCEPTANCE CRITERIA', 'BUSINESS VALUE', 'ESTIMATION', 'STATUS']
    return render_template('list.html', user_stories=user_stories, headers=headers)


# W tej funkcji użyłam funkcji z common:
# generowania id jako znacznika czasowego i tworzenia słownika z danymi ze strony
# wątpliwość - jako pierwszą metodę wskazałam GET natomiat POST bez konkretnego wskazania
# czy to dobrze?
@app.route('/story', methods=['GET', 'POST'])
def route_add():
    """
    Function supports /add page - adding data
    Using two methods - if GET - shows forms to fill
    if POST - execute saving data in database and redirect to /list page
    :return: depends of used method (but webpage)
    """
    statuses = data_handler.STATUSES
    current = 'planning'
    if request.method == 'GET':
        return render_template('add.html', statuses=statuses, current=current)
    else:
        time_id = common.generate_timestamp_as_id()
        story = common.make_story(time_id)
        data_handler.append_stories_in_file(story)
        return redirect('/')


@app.route('/story/<id>', methods=['GET', 'POST'])
def route_edit(id):
    """
    Function support webpage /story/<id> - editing and updating
    finds story by id (timestamp)
    Using two methods - if 'GET' - shows form with filled data from story
    if POST - execute saving updated data in database and redirect to /list page
    :param id:
    :return: depends of used method (but webpage)
    """
    try:
        statuses = data_handler.STATUSES
        if request.method == "GET":
            wanted_story = data_handler.get_story_by_id(id)
            current = wanted_story['status']
            return render_template('edit.html', wanted_story=wanted_story, statuses=statuses, current=current)
        else:
            new_story = common.make_story(id)
            data_handler.update_story_by_id(id, new_story)
            return redirect('/')
    except TypeError:
        return not_found_error(404)


@app.route('/story/delete/<story_id>')
def route_delete(story_id):
    """
    Function supports deleting stories by id
    :param story_id:
    :return: redirect to main page
    """
    data_handler.delete_story_by_id(story_id)
    return redirect('/')


@app.route('/make-story')
def route_make_story():
    return render_template('make_story.html')


# Znalezione w sieci. Działa, ale po co ten error w parametrach?
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
