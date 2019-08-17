# file to handling server and passing data between user and database
from flask import Flask, render_template, request, redirect, url_for, Response
import data_handler
import common



app = Flask(__name__)


@app.route('/')
def route_list():
    """
    Function supports main page and /list page
    :return: main page with list of stories
    """
    user_stories = data_handler.get_all_user_story()
    headers = ['ID', 'TITLE', 'USER STORY', 'ACCEPTANCE CRITERIA', 'BUSINESS VALUE', 'ESTIMATION', 'STATUS']
    return render_template('list.html',
                           user_stories=user_stories,
                           headers=headers)


@app.route('/list')
def route_sorted_list():
    try:
        user_stories = data_handler.get_all_user_story()
        attribute = request.args.get('attribute')
        order = request.args.get('order')
        user_stories = common.convert_number_to_integer(user_stories)
        sorted_stories = common.sort_by_attributes(user_stories, attribute, order)
        headers = ['ID', 'TITLE', 'USER STORY', 'ACCEPTANCE CRITERIA', 'BUSINESS VALUE', 'ESTIMATION', 'STATUS']
        return render_template('list.html',
                               user_stories=sorted_stories,
                               headers=headers)
    except UnboundLocalError:
        return route_list()


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
    action_type = "Add"
    second_column = 'add_form'
    if request.method == 'GET':
        return render_template('story.html',
                               statuses=statuses,
                               current=current,
                               action_type=action_type,
                               form_url=url_for('route_add'),
                               second_column=second_column)
    else:
        time_id = common.generate_timestamp_as_id()
        story = common.make_story(time_id)
        data_handler.append_stories_in_file(story)
        return redirect('/')


@app.route('/story/<story_id>', methods=['GET', 'POST'])
def route_edit(story_id):
    """
    Function support webpage /story/<id> - editing and updating
    finds story by id (timestamp)
    Using two methods - if 'GET' - shows form with filled data from story
    if POST - execute saving updated data in database and redirect to /list page
    :param story_id:
    :return: depends of used method (but webpage)
    """
    try:
        statuses = data_handler.STATUSES
        action_type = "Update"
        if request.method == "GET":
            wanted_story = data_handler.get_story_by_id(story_id)
            current = wanted_story['status']
            return render_template('story.html',
                                   wanted_story=wanted_story,
                                   statuses=statuses,
                                   current=current,
                                   action_type=action_type,
                                   form_url=url_for('route_edit', story_id=story_id))
        else:
            new_story = common.make_story(story_id)
            data_handler.update_story_by_id(story_id, new_story)
            return redirect('/')
    except TypeError:
        return not_found_error(404)
    except KeyError:
        return bad_request_error(400)


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


@app.route('/sources')
def route_sources():
    return render_template('source.html')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(400)
def bad_request_error(error):
    return render_template('400.html'), 400


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
