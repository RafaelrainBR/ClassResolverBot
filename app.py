from model.class_model import from_json
from service import oauth_service as classroom


class App:

    def __init__(self):
        pass

    def ask_auth(self):
        flow = classroom.create_flow()
        credentials = flow.run_console()

        courses = classroom.get_courses(credentials)
        classes = [from_json(course) for course in courses]

        for classe in classes:
            print(classe.name)
        pass

    pass
