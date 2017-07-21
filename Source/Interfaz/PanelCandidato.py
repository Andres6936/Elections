#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

class PanelCandidato(wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr, nNumeroCandidato=None):

        # Enviamos todos los parametros a la clase padre.
        super().__init__(parent, id, pos, size, style, name)

        self.principal = parent
        self.numeroCandidato = nNumeroCandidato

        # Botón actualizar datos
        botonPorcentajeVotos = wx.Button(self, -1, 'Porcentaje Votos')
        botonPorcentajeVotos.SetSize(wx.Size(160, 20))

        # Botón votar
        botonVotar = wx.Button(self, -1, 'Votar')
        botonVotar.SetSize(wx.Size(160, 20))

        # Etiqueta nombre del candidato
        etiquetaNombreCandidato = wx.StaticText(self, -1, 'Nombre: ')

        # Etiqueta apellido del candidato
        etiquetaApellidoCandidato = wx.StaticText(self, -1, 'Apellido: ')

        # Etiqueta edad del candidato
        etiquetaEdadCandidato = wx.StaticText(self, -1, 'Edad: ')

        # Etiqueta partido político del candidato
        etiquetaPartidoPoliticoCandidato = wx.StaticText(self, -1, 'Partido Político: ')

        # Etiqueta costo campaña del candidato
        etiquetaCostoCampanhaCandidato = wx.StaticText(self, -1, 'Costo Campaña: $ ')

        # Etiqueta número de votos
        etiquetaNumeroVotos = wx.StaticText(self, -1, 'Numero de Votos: ')

        # Construye la forma del panel
        sizerLayout = wx.FlexGridSizer(rows=9, cols=1, vgap=1, hgap=1)
        sizerLayoutImagen = wx.BoxSizer(wx.VERTICAL)

        # Configuramos la imagen del candidato
        rutaImagen = './Data/Candidato' + str(self.numeroCandidato) + '.gif'
        bitmap = wx.Bitmap(rutaImagen, wx.BITMAP_TYPE_GIF)
        imagen = wx.StaticBitmap(self, -1, bitmap)

        sizerLayoutImagen.Add(imagen, 1, wx.EXPAND)
        sizerLayout.Add(sizerLayoutImagen, 1)
        sizerLayout.Add(etiquetaNombreCandidato, 1, wx.EXPAND)
        sizerLayout.Add(etiquetaApellidoCandidato, 1, wx.EXPAND)
        sizerLayout.Add(etiquetaEdadCandidato, 1, wx.EXPAND)
        sizerLayout.Add(etiquetaPartidoPoliticoCandidato, 1, wx.EXPAND)
        sizerLayout.Add(etiquetaCostoCampanhaCandidato, 1, wx.EXPAND)
        sizerLayout.Add(etiquetaNumeroVotos, 1, wx.EXPAND)
        sizerLayout.Add(botonPorcentajeVotos, 1, wx.EXPAND)
        sizerLayout.Add(botonVotar, 1, wx.EXPAND)

        self.SetSizer(sizerLayout)
        self.Fit()