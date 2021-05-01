

class Classroom:
    def __init__(self, class_id, name, room, owner_id):
        self.class_id = class_id
        self.name = name
        self.room = room
        self.owner_id = owner_id


def from_json(json):
    return Classroom(json['id'], json['name'], json['room'], json['ownerId'])

# {'id': '321902745442', 'name': 'Edutech - Python - 25400133', 'section': 'CLETO, C E PROF-EF M',
# 'room': '1789648-530', 'ownerId': '110109762513133360015', 'creationTime': '2021-04-08T21:45:40.879Z',
# 'updateTime': '2021-04-30T13:34:52.775Z', 'courseState': 'ACTIVE', 'alternateLink':
# 'https://classroom.google.com/c/MzIxOTAyNzQ1NDQy', 'teacherGroupEmail':
# 'Edutech_Python_25401831_Tarde_CLETO_C_E_PROF_EF_M_teachers_17d23fa1@escola.pr.gov.br', 'courseGroupEmail':
# 'Edutech_Python_25401831_Tarde_CLETO_C_E_PROF_EF_M_a861ea39@escola.pr.gov.br', 'guardiansEnabled': False,
# 'calendarId': 'c_classroom87c6ad1f@group.calendar.google.com'}
