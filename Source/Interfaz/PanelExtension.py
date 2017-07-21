#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

class PanelExtension(wx.Panel):
    """
    Panel de manejo de extensiones.
    """

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):

        # Enviamos todos los parametros a la clase padre.
        super().__init__(parent, id, pos, size, style, name)

        self.principal = parent

        # Botón vaciar urna
        self.botonVaciarUrna = wx.Button(self, -1, 'Vaciar Urna')
        self.Bind(wx.EVT_BUTTON, self.OnVaciarUrna, self.botonVaciarUrna)

        # Boton opción 1
        self.botonOpcion1 = wx.Button(self, -1, 'Opción 1')
        self.Bind(wx.EVT_BUTTON, self.OnOpcion1, self.botonOpcion1)

        # Botón opción 2
        self.botonOpcion2 = wx.Button(self, -1, 'Opción 2')
        self.Bind(wx.EVT_BUTTON, self.OnOpcion2, self.botonOpcion2)


        # Configuramos el Border Layout del panel
        sizerLayout = wx.BoxSizer(wx.HORIZONTAL)

        sizerLayout.Add(self.botonVaciarUrna, 1, wx.EXPAND)
        sizerLayout.Add(self.botonOpcion1, 1, wx.EXPAND)
        sizerLayout.Add(self.botonOpcion2, 1, wx.EXPAND)

        self.SetSizer(sizerLayout)
        self.Fit()


    def OnVaciarUrna(self, event) -> None:
        """
        Manejo de eventos del usuario.
        @param event: Evento de usuario. event != None
        """
        self.principal.VaciarUrna()

    def OnOpcion1(self, event) -> None:
        """
        Manejo de eventos del usuario.
        @param event: Evento de usuario. event != None
        """
        self.principal.reqFuncOpcion1()

    def OnOpcion2(self, event) -> None:
        """
        Manejo de eventos del usuario.
        @param event: Evento de usuario. event != None
        """
        self.principal.reqFuncOpcion2()