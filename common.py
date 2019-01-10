# file to keep repeated functions, additional logic
import time
from flask import Flask, render_template, request, redirect, url_for, session


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


def convert_linebreaks_to_br(original_string):
    """
    Function converts string with <br> to string with \n
    :param original_string:
    :return: modified_string (string)
    """

    modified_string = original_string.replace('<br>', '\n')
    return modified_string


def convert_linebreaks_in_all_stories(all_stories):
    """
    Function converts line breaks <br> to \n.
    for given keys in list of dictionaries
    :param all_stories: list of dictionaries
    :return: all_stories: list of dictionaries
    """

    for user_story in all_stories:
        convert_linebreaks_in_one(user_story)
    return all_stories


def convert_linebreaks_in_one(user_story):
    """
    Function converts line breaks <br> to \n.
    for given keys in dictionary
    :param user_story: dict
    :return: user_story: dict
    """
    user_story['user_story'] = convert_linebreaks_to_br(user_story['user_story'])
    user_story['acceptance_criteria'] = convert_linebreaks_to_br(user_story['acceptance_criteria'])
    return user_story


def convert_number_to_integer(all_stories):
    """
    Function converts data for business value and estimation into integers
    :param all_stories:all_stories - list of dict
    :return: all_stories - list of dict
    """
    for user_story in all_stories:
        user_story['business_value'] = int(user_story['business_value'])
        user_story['estimation'] = int(user_story['estimation'])
    return all_stories


def sort_by_attributes(all_stories, attribute, order):
    """
    Function sorts data based on given parameters
    :param all_stories: List of dict
    :param attribute: string
    :param order:
    :return: new_all_stories - list of dict
    """
    sort_order = None
    if order == 'desc':
        sort_order = True
    elif order == 'asc':
        sort_order = False
    new_all_stories = sorted(all_stories, key=lambda k: k[attribute], reverse=sort_order)
    return new_all_stories
