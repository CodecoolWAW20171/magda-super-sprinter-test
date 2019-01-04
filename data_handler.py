import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story():
    with open('data.csv', newline='') as file:
        reader = csv.DictReader(file)
        all_stories = []
        for row in reader:
            all_stories.append(row)
        return all_stories


def append_stories_in_file(story):
    with open('data.csv', 'a', newline='') as file:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(story)


def get_story_by_id(id):
    with open('data.csv', newline='') as file:
        reader = csv.DictReader(file)
        for story in reader:
            if story['id'] == id:
                return story

# story1 = {'id':'01', 'title':'all list', 'user_story':'As a User', 'acceptance_criteria':'Given that', 'business_value':'20', 'estimation':'2', 'status':'done'}
# append_stories_in_file(story1)
print(get_story_by_id('2')['title'])