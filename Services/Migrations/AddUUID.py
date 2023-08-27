import uuid

from Services.Models.Personal.Personal import Personal
from Services.Models.Personal.PersonalCOVI import PersonalCOVI


def AddUUID():
    for personalCOVI in PersonalCOVI.select():
        personalCOVI.Serial = uuid.uuid4()
        personalCOVI.save()

    for personal in Personal.select():
        personal.Serial = uuid.uuid4()
        personal.save()
