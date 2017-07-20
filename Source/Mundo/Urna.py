#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

from Source.Mundo.Candidato import Candidato

class Urna:

    # ---------------------------------
    # Constructor
    # ---------------------------------

    def __init__(self):

        # Inicializa el candidato 1.
        self.candidato1 = Candidato('Felipe', 'Pitti', 'Independiente', 27)

        # Inicializa el candidato 2.
        self.candidato2 = Candidato('Susanita', 'Chirusi', 'Revolucionario', 26)

        # Inicializa el candidato 3.
        self.candidato3 = Candidato('Manolito', 'Goreiro', 'Tradicional', 26)

    # ---------------------------------
    # Métodos
    # ---------------------------------


    def GetCandidato1(self):
        return self.candidato1

    def GetCandidato2(self):
        return self.candidato2

    def GetCandidato3(self):
        return self.candidato3

    def IngresarVotoTelevisionCandidato1(self):
        self.candidato1.AgregarVotoTelevision()

    def IngresarVotoRadioCandidato1(self):
        self.candidato1.AgregarVotoRadio()

    def IngresarVotoInternetCandidato1(self):
        self.candidato1.AgregarVotoInternet()

    def IngresarVotoTelevisionCandidato2(self):
        self.candidato2.AgregarVotoTelevision()

    def IngresarVotoRadioCandidato2(self):
        self.candidato2.AgregarVotoRadio()

    def IngresarVotoInternetCandidato2(self):
        self.candidato2.AgregarVotoInternet()

    def IngresarVotoTelevisionCandidato3(self):
        self.candidato3.AgregarVotoTelevision()

    def IngresarVotoRadioCandidato3(self):
        self.candidato3.AgregarVotoRadio()

    def IngresarVotoInternetCandidato3(self):
        self.candidato3.AgregarVotoInternet()

    def CalcularTotalVotos(self):
        return self.candidato1.GetVotos() + self.candidato2.GetVotos() + self.candidato3.GetVotos()

    def CalcularCostoPromedioCampanha(self):

        total: int = self.candidato1.GetCostoCampanha() + self.candidato2.GetCostoCampanha() + self.candidato3.GetCostoCampanha()
        promedio: float = total / 3

        return promedio

    def CalcularPorcentajeVotosCandidato1(self):

        numVotosCandidato1: int = self.candidato1.GetVotos()
        votosTotales: int = self.CalcularTotalVotos()

        porcentaje: float = numVotosCandidato1 / votosTotales * 100

        return porcentaje

    def CalcularPorcentajeVotosCandidato2(self):

        numVotosCandidato2: int = self.candidato2.GetVotos()
        votosTotales: int = self.CalcularTotalVotos()

        porcentaje: float = numVotosCandidato2 / votosTotales * 100

        return porcentaje

    def CalcularPorcentajeVotosCandidato3(self):

        numVotosCandidato3: int = self.candidato3.GetVotos()
        votosTotales: int = self.CalcularTotalVotos()

        porcentaje: float = numVotosCandidato3 / votosTotales * 100

        return porcentaje

    def VaciarUrna(self):

        # Reiniciar candidato 1.
        self.candidato1.ReiniciarConteoVotos()
        self.candidato1.ReiniciarCostoCampanha()

        # Reiniciar candidato 2.
        self.candidato2.ReiniciarConteoVotos()
        self.candidato2.ReiniciarCostoCampanha()

        # Reinicia candidato 3.
        self.candidato3.ReiniciarConteoVotos()
        self.candidato3.ReiniciarCostoCampanha()

    # ---------------------------------
    # Punto de Extensión
    # ---------------------------------

    def Metodo1(self):
        return 'Respuesta 1'

    def Metodo2(self):
        return 'Respuesta 2'