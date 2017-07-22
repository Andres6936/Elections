#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

from Source.Mundo.Candidato import Candidato

class Urna:
    """
    Es la urna de votación con tres candidatos.
    """

    # ---------------------------------
    # Atributos
    # ---------------------------------



    # ---------------------------------
    # Constructor
    # ---------------------------------

    def __init__(self):
        """
        Inicializa los tres candidatos.
        @postcondition: Se inicializaron los tres candidatos con los valores por parámetro
        nombre, apellido, partido político y edad.
        """

        # Inicializa el candidato 1.
        self.candidato1 = Candidato('Felipe', 'Pitti', 'Independiente', 27)
        """
        El candidato número 1 de las elecciones.
        """

        # Inicializa el candidato 2.
        self.candidato2 = Candidato('Susanita', 'Chirusi', 'Revolucionario', 26)
        """
        El candidato número 2 de las elecciones.
        """

        # Inicializa el candidato 3.
        self.candidato3 = Candidato('Manolito', 'Goreiro', 'Tradicional', 26)
        """
        El candidato número 3 de las elecciones.
        """

    # ---------------------------------
    # Métodos
    # ---------------------------------


    def GetCandidato1(self) -> Candidato:
        """
        Devuelve el candidato 1.
        @return: Candidato 1
        """
        return self.candidato1

    def GetCandidato2(self) -> Candidato:
        """
        Devuelve el candidato 2.
        @return: Candidato 2.
        """
        return self.candidato2

    def GetCandidato3(self) -> Candidato:
        """
        Devuelve el candidato 3.
        @return: Candidato 3.
        """
        return self.candidato3

    def IngresarVotoTelevisionCandidato1(self) -> None:
        """
        Ingresa un voto influenciado por la televisión al candidato 1.
        """
        self.candidato1.AgregarVotoTelevision()

    def IngresarVotoRadioCandidato1(self) -> None:
        """
        Ingresa un voto influenciado por radio al candidato 1.
        """
        self.candidato1.AgregarVotoRadio()

    def IngresarVotoInternetCandidato1(self) -> None:
        """
        Ingresa un voto influenciado por internet al candidato 1.
        """
        self.candidato1.AgregarVotoInternet()

    def IngresarVotoTelevisionCandidato2(self) -> None:
        """
        Ingresa un voto influenciado por la televisión al candidato 2.
        """
        self.candidato2.AgregarVotoTelevision()

    def IngresarVotoRadioCandidato2(self) -> None:
        """
        Ingresa un voto influenciado por radio al candidato 2.
        """
        self.candidato2.AgregarVotoRadio()

    def IngresarVotoInternetCandidato2(self) -> None:
        """
        Ingresa un voto influenciado por internet al candidato 2.
        """
        self.candidato2.AgregarVotoInternet()

    def IngresarVotoTelevisionCandidato3(self) -> None:
        """
        Ingresa un voto influenciado por la televisión al candidato 3.
        """
        self.candidato3.AgregarVotoTelevision()

    def IngresarVotoRadioCandidato3(self) -> None:
        """
        Ingresa un voto influenciado por radio al candidato 3.
        """
        self.candidato3.AgregarVotoRadio()

    def IngresarVotoInternetCandidato3(self) -> None:
        """
        Ingresa un voto influenciado por internet al candidato 3.
        """
        self.candidato3.AgregarVotoInternet()

    def CalcularTotalVotos(self) -> int:
        """
        Devuelve el total de votos en la urna.
        @return: La sumatoria de los votos de los tres candidatos.
        @rtype: int
        """
        return self.candidato1.GetVotos() + self.candidato2.GetVotos() + self.candidato3.GetVotos()

    def CalcularCostoPromedioCampanha(self) -> float:
        """
        Devuelve el costo promedio de camapaña de los candidatos.
        @return: La razón de la sumatoria de los costos de la campaña de los
        candidatos y el número total de candidatos.
        @rtype: float
        """

        total: int = self.candidato1.GetCostoCampanha() + self.candidato2.GetCostoCampanha() + self.candidato3.GetCostoCampanha()
        promedio: float = total / 3

        return promedio

    def CalcularPorcentajeVotosCandidato1(self) -> float:
        """
        Devuelve el porcentaje de votos obtenidos por el candidato 1.
        @return: Porcentaje de votos obtenidos por el candidato 1.
        @rtype: float
        """

        numVotosCandidato1: int = self.candidato1.GetVotos()
        votosTotales: int = self.CalcularTotalVotos()

        porcentaje: float = numVotosCandidato1 / votosTotales * 100

        return porcentaje

    def CalcularPorcentajeVotosCandidato2(self) -> float:
        """
        Devuelve el porcentaje de votos obtenidos por el candidato 2.
        @return: Porcentaje de votos obtenidos por el candidato 2.
        @rtype: float
        """

        numVotosCandidato2: int = self.candidato2.GetVotos()
        votosTotales: int = self.CalcularTotalVotos()

        porcentaje: float = numVotosCandidato2 / votosTotales * 100

        return porcentaje

    def CalcularPorcentajeVotosCandidato3(self) -> float:
        """
        Devuelve el porcentaje de votos obtenidos por el candidato 3.
        @return: Porcentaje de votos obtenidos por el candidato 3.
        @rtype: float
        """

        numVotosCandidato3: int = self.candidato3.GetVotos()
        votosTotales: int = self.CalcularTotalVotos()

        porcentaje: float = numVotosCandidato3 / votosTotales * 100

        return porcentaje

    def VaciarUrna(self) -> None:
        """
        Restaura la urna al estado inicial, todos los candidatos qeudan sin votos y
        costo de campaña en 0.
        """

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

    def Metodo1(self) -> str:
        """
        Método para la extensión 1.
        @return: Respuesta 1.
        """
        return 'Respuesta 1'

    def Metodo2(self) -> str:
        """
        Método para la extensión 2.
        @return: Respuesta 2.
        """
        return 'Respuesta 2'