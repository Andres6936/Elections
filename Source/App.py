#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

from Source.Interfaz.InterfazElecciones import InterfazElecciones


class AplicationManager(wx.App):

    def __init__(self, redirect=True, filename=None, useBestVisual=False, clearSigInt=True):

        # Enviamos todos los parametros a la clase padre.
        wx.App.__init__(self, redirect, filename, useBestVisual, clearSigInt)

    def OnInit(self):
        self.frame = InterfazElecciones(parent=None, id=-1)
        self.SetTopWindow(self.frame)
        return True