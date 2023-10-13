import uuid

import shortuuid

from Services.Models.Elecciones.Candidates import Candidates
from Services.Models.Elecciones.Senator import Senator
from Services.Models.Personal.Personal import Personal
from Services.Models.Personal.PersonalCOVI import PersonalCOVI


def AddUUID():
    for personalCOVI in PersonalCOVI.select():
        personalCOVI.Serial = uuid.uuid4()
        personalCOVI.save()

    for personal in Personal.select():
        personal.Serial = uuid.uuid4()
        personal.save()


def AddUUIDCandidates():
    for candidate in Candidates.select():
        candidate.Serial = shortuuid.ShortUUID().random(length=6)
        candidate.save()


def ADDUUIDSenator():
    for senator in Senator.select():
        senator.Serial = shortuuid.ShortUUID().random(length=6)
        senator.save()
