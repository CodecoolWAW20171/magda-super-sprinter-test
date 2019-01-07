# file to keep repeated functions, additional logic
import time
from flask import Flask, render_template, request, redirect, url_for, session
import data_handler


def generate_timestamp_as_id():
    """
    Generates id as current unix time stamp
    When user clicks on button 'add' id is generated
    :return: timestamp as integer
    """
    current_time = int(time.time())
    return current_time


def make_story(id):
    """
    Function takes data from form (except ID) and creates dictionary
    ID can be passed from another function or from form
    :param id:
    :return: story as  dictionary
    """
    title = request.form['title']
    user_story = request.form['user_story']
    acceptance_criteria = request.form['acceptance_criteria']
    business_value = request.form['business_value']
    estimation = request.form['estimation']
    status = request.form['status']
    story = {'id': id, 'title': title, 'user_story': user_story, 'acceptance_criteria': acceptance_criteria,
             'business_value': business_value, 'estimation': estimation, 'status': status}
    return story


# nie działa jak powinno.
def convert_linebreaks_in_all_stories(all_stories):
    for user_story in all_stories:
        user_story['user_story'] = convert_linebreaks_to_br(user_story['user_story'])
        user_story['acceptance_criteria'] = convert_linebreaks_to_br(user_story['acceptance_criteria'])
    return all_stories


def convert_linebreaks_in_one(user_story):
    user_story['user_story'] = convert_linebreaks_to_br(user_story['user_story'])
    user_story['acceptance_criteria'] = convert_linebreaks_to_br(user_story['acceptance_criteria'])
    return user_story


def convert_linebreaks_to_br(original_str):
    modified_str = original_str.replace('<br>', '\n')
    return modified_str

