# File to handling database as csv
import csv
import os
import shutil
import common

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story():
    """
    Takes all data from database
    and return them
    return: List of ordered dicts
    """

    try:
        with open(DATA_FILE_PATH, newline=None) as file:
            reader = csv.DictReader(file)
            all_stories = [story for story in reader]
            return common.convert_linebreaks_in_all_stories(all_stories)
    except ConnectionError:
        return 'There is problem with connection. Try again later'
    except FileNotFoundError:
        return 'There is no such file'


def append_stories_in_file(story):
    """
    Takes data as arg. and convert it into dictionary using headers as keys.
    And appends dict into database
    param story:
    return: None
    """
    try:
        with open(DATA_FILE_PATH, 'a') as file:
            writer = csv.DictWriter(file, fieldnames=DATA_HEADER)
            writer.writerow(story)
    except ConnectionError:
        return 'There is problem with connection. Try again later'
    except FileNotFoundError:
        return 'There is no such file'


def get_story_by_id(story_id):
    """
    Based on given id looks for story with matching id
    and returns it
    :param story_id:
    :return: story as a dict
    """
    try:
        with open(DATA_FILE_PATH, newline='') as file:
            reader = csv.DictReader(file)
            for story in reader:
                if story['id'] == story_id:
                    return common.convert_linebreaks_in_one(story)
    except ConnectionError:
        return 'There is problem with connection. Try again later'
    except FileNotFoundError:
        return 'There is no such file'


# rozwiązanie skompilowałam z:
# https://stackoverflow.com/questions/16020858/inline-csv-file-editing-with-python/16020923#16020923
# https://stackoverflow.com/questions/41574037/updating-a-specific-row-in-csv-file
# https://stackoverflow.com/questions/46126082/how-to-update-rows-in-a-csv-file
# polecana metoda aktualizowania - praca na pliku tymczasowym a nie źródłowym
# stąd moduł shutil, który pozwala zamykać, otwierać i kopiować pliki
def update_story_by_id(story_id, new_story):
    """
    Function finds story by given id and changes its data
    :param story_id:
    :param new_story:
    :return: no return
    """
    with open(DATA_FILE_PATH, 'r') as csv_file, open('output_file.csv', 'w') as output:
        reader = csv.DictReader(csv_file, fieldnames=DATA_HEADER)
        writer = csv.DictWriter(output, fieldnames=DATA_HEADER)
        for story in reader:
            if story['id'] == story_id:
                story = {k: new_story[k] for k in story}
            writer.writerow(story)
    shutil.move('output_file.csv', DATA_FILE_PATH)


def delete_story_by_id(story_id):
    """
    Function finds story by given id and deletes its data
    :param story_id:
    :return: no return
    """
    with open(DATA_FILE_PATH, 'r') as csv_file, open('output_file.csv', 'w') as output:
        reader = csv.DictReader(csv_file, fieldnames=DATA_HEADER)
        writer = csv.DictWriter(output, fieldnames=DATA_HEADER)
        for story in reader:
            if story['id'] != story_id:
                writer.writerow(story)
    shutil.move('output_file.csv', DATA_FILE_PATH)
