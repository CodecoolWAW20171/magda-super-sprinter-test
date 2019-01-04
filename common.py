import data_handler

def check_id():
    all_stories = data_handler.get_all_user_story()
    for stories in all_stories:
        print(stories['id'])



check_id()
