#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

class Candidato:

    # ---------------------------------
    # Atributos
    # ---------------------------------



    # ---------------------------------
    # Constructor
    # ---------------------------------

    def __init__(self, nNombre, nApellido, nPartidoPolitico, nEdad):

        self.nombre = nNombre
        self.apellido = nApellido
        self.partidoPolitico = nPartidoPolitico
        self.edad = nEdad
        self.costoCampanha = 0
        self.votos = 0

    # ---------------------------------
    # Métodos
    # ---------------------------------

    def GetNombre(self):
        return self.nombre

    def GetApellido(self):
        return self.apellido

    def GetPartidoPolitico(self):
        return self.partidoPolitico

    def GetEdad(self):
        return self.edad

    def GetCostoCampanha(self):
        return self.costoCampanha

    def GetVotos(self):
        return self.votos

    def IngresarUnVoto(self):
        self.votos += 1

    def AgregarVotoTelevision(self):
        self.costoCampanha += 1000
        self.IngresarUnVoto()

    def AgregarVotoRadio(self):
        self.costoCampanha += 500
        self.IngresarUnVoto()

    def AgregarVotoInternet(self):
        self.costoCampanha += 100
        self.IngresarUnVoto()

    def ReiniciarConteoVotos(self):
        self.votos = 0

    def ReiniciarCostoCampanha(self):
        self.costoCampanha = 0