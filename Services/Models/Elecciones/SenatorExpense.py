from peewee import TextField

from Services.Models.Elecciones.EleccionesBase import EleccionesBase


class SenatorExpense(EleccionesBase):
    Serial = TextField(primary_key=True)
    CND_NOMBRE = TextField()
    CLA_NOMBRE = TextField()
    DEP_NOMBRE = TextField()
    ORG_NOMBRE = TextField()
    CAN_TIPO_IDENTIFICACION = TextField()
    CAN_IDENTIFICACION = TextField()
    NOMBRE_CANDIDATO = TextField()
    CCO_ID = TextField()
    NOMBRE_GASTO = TextField()
    NOMBRE_PERSONA = TextField()
    TIPO_PERSONA = TextField()
    GAS_VALOR = TextField()
    GAS_CONCEPTO = TextField()
    TIPO_PROPAGANDA = TextField()
    Senator = TextField()
    UUID = TextField()
