#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

class Candidato:
    """
    Candidato de la elección.
    """

    # ---------------------------------
    # Atributos
    # ---------------------------------



    # ---------------------------------
    # Constructor
    # ---------------------------------

    def __init__(self, nNombre, nApellido, nPartidoPolitico, nEdad):
        """
        Inicializa los datos del candidato con los valores que vienen por parámetro.
        @postcondition: El costo de campaña se inicializó en cero.
        @param nNombre: Nombre del candidato.
        @type nNombre: str
        @param nApellido: Apellido del candidato.
        @type nApellido: str
        @param nPartidoPolitico: Partido político del candidato.
        @type nPartidoPolitico: str
        @param nEdad: Edad del candidato.
        @type nEdad: int
        """

        self.nombre: str = nNombre
        self.apellido: str = nApellido
        self.partidoPolitico: str = nPartidoPolitico
        self.edad: int = nEdad
        self.costoCampanha: float = 0
        self.votos: int = 0

    # ---------------------------------
    # Métodos
    # ---------------------------------

    def GetNombre(self) -> str:
        """
        Devuelve el nombre del candidato.
        @return: Nombre del candidato.
        @rtype: str
        """
        return self.nombre

    def GetApellido(self) -> str:
        """
        Devuelve el apellido del candidato.
        @return: Apellido del candidato.
        @rtype: str
        """
        return self.apellido

    def GetPartidoPolitico(self) -> str:
        """
        Devuelve el partido político del candidato.
        @return: Partido político del candidato.
        @rtype: str
        """
        return self.partidoPolitico

    def GetEdad(self) -> int:
        """
        Devuelve la edad del candidato.
        @return: Edad del candidato.
        @rtype: int
        """
        return self.edad

    def GetCostoCampanha(self) -> float:
        """
        Devuelve el costo de campaña del candidato.
        @return: Costo de campaña del candidato.
        @rtype: float
        """
        return self.costoCampanha

    def GetVotos(self) -> int:
        """
        Devuelve el número de votos del candidato.
        @return: Número de votos obtenidos.
        @rtype: int
        """
        return self.votos

    def IngresarUnVoto(self) -> None:
        """
        Ingresa un voto al candidato.
        @postcondition: Se modificó el número de votos aumentándose el existente en 1.
        """
        self.votos += 1

    def AgregarVotoTelevision(self) -> None:
        """
        Adiciona un voto influenciado por la televisión.
        @postcondition: Se adiciona al costo de la camapaña
        la suma de $1000 y se incrementa el número de votos en 1.
        """
        self.costoCampanha += 1000
        self.IngresarUnVoto()

    def AgregarVotoRadio(self) -> None:
        """
        Adiciona un voto influenciado por la radio.
        @postcondition: Se adiciona al costo de la campaña la suma de $500 y se
        incrementa el número de votos en 1.
        """
        self.costoCampanha += 500
        self.IngresarUnVoto()

    def AgregarVotoInternet(self) -> None:
        """
        Adiciona un voto influenciado por internet.
        @postcondition: Se adiciona al costo de la camapaña la suma de $100
        y se incrementa el número de votos en 1.
        """
        self.costoCampanha += 100
        self.IngresarUnVoto()

    def ReiniciarConteoVotos(self) -> None:
        """
        Se reinicia el conteo de votos.
        @postcondition: self.votos = 0
        """
        self.votos = 0

    def ReiniciarCostoCampanha(self):
        """
        Se reinicia el costo de camapaña.
        @postcondition: self.costoCampanha = 0
        """
        self.costoCampanha = 0