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


# tu jest problem z tym dodawaniem point i h.
# zobaczyć czy nie da się tego rozwiązać jakoś css albo html
# żeby tylko  wyświetlało points/h ale nie dodawało do pliku csv.
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
    business_value = request.form['business_value'] + ' point'
    estimation = request.form['estimation'] + ' h'
    status = request.form['status']
    story = {'id': id, 'title': title, 'user_story': user_story, 'acceptance_criteria': acceptance_criteria,
             'business_value': business_value, 'estimation': estimation, 'status': status}
    return story

