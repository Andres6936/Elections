#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

class PanelExtension(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr):

        # Enviamos todos los parametros a la clase padre.
        super().__init__(parent, id, pos, size, style, name)

        self.principal = parent

        # Botón vaciar urna
        self.btnVaciarUrna = wx.Button(self, -1, 'Vaciar Urna')

        # Boton opción 1
        self.btnOpcion1 = wx.Button(self, -1, 'Opción 1')

        # Botón opción 2
        self.btnOpcion2 = wx.Button(self, -1, 'Opción 2')


        # Configuramos el Border Layout del panel
        sizerLayout = wx.BoxSizer(wx.HORIZONTAL)

        sizerLayout.Add(self.btnVaciarUrna, 1, wx.EXPAND)
        sizerLayout.Add(self.btnOpcion1, 1, wx.EXPAND)
        sizerLayout.Add(self.btnOpcion2, 1, wx.EXPAND)

        self.SetSizer(sizerLayout)
        self.Fit()


    def OnVaciarUrna(self):
        self.principal.VaciarUrna()

    def OnOpcion1(self):
        self.principal.reqFuncOpcion1()

    def OnOpcion2(self):
        self.principal.reqFuncOpcion2()