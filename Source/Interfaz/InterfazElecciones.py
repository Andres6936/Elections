#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

from Source.Mundo.Urna import Urna

class InterfazElecciones(wx.Frame):
    def __init__(self, *args, **kw):
        # Enviamos todos los parametros a la clase padre.
        super().__init__(*args, **kw)

        # Creamos la clase principal.
        self.urna = Urna()

        # Construye la forma.
        self.SetTitle('Elecciones Python')
        self.SetSize(wx.Size(800, 600))
        self.Show(True)