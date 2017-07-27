#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

class PanelImagen(wx.Panel):
    """
    Panel con la imagen.
    """

    # ---------------------------------
    # Constructor.
    # ---------------------------------

    def __init__(self, *args, **kwargs):
        """
        Constructor del panel.
        """

        # Enviamos todos los parametros a la clase padre.
        super().__init__(*args, **kwargs)

        self.SetBackgroundColour('White')

        rutaImagen = './Data/Encabezado.jpg'
        bitmap = wx.Bitmap(rutaImagen, wx.BITMAP_TYPE_JPEG)
        imagen = wx.StaticBitmap(self, -1, bitmap)

        sizerLayout = wx.BoxSizer(wx.VERTICAL)

        sizerLayout.Add(imagen, 1, wx.EXPAND)

        self.SetSizer(sizerLayout)