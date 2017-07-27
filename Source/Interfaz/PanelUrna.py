#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

class PanelUrna(wx.Panel):
    """
    Panel que contiene la información de la urna de votos en la elecciones Cupi2.
    """

    # ---------------------------------
    # Constructor.
    # ---------------------------------

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):

        # Enviamos todos los parametros a la clase padre.
        super().__init__(parent, id, pos, size, style, name)

        # Etiqueta total votos
        self.etiquetaTotalVotos = wx.StaticText(self, -1, 'Total Votos')
        self.etiquetaTotalVotos.SetForegroundColour('Blue')

        # Etiqueta total costo de camapaña
        self.etiquetaPromedioCostoCampanha = wx.StaticText(self, -1, 'Costo Promedio Campaña: $')
        self.etiquetaPromedioCostoCampanha.SetForegroundColour('Blue')

        sizerLayout = wx.BoxSizer(wx.VERTICAL)

        sizerLayout.Add(self.etiquetaTotalVotos, 1, wx.CENTER)
        sizerLayout.Add(self.etiquetaPromedioCostoCampanha, 1, wx.CENTER)

        self.SetSizer(sizerLayout)

    # ---------------------------------
    # Métodos.
    # ---------------------------------

    def Actualizar(self, urna) -> None:
        """
        Actualiza la información.

        Args:
            urna (Urna): Urna de la cual se va a mostrar la información. urna != None.
        """
        self.etiquetaTotalVotos.SetLabelText('Total Votos: ' + str(urna.CalcularTotalVotos()))
        self.etiquetaPromedioCostoCampanha.SetLabelText('Costo Promedio Campaña: $ ' + str(urna.CalcularCostoPromedioCampanha()))

    def FormatearValorReal(self, valor):
        pass