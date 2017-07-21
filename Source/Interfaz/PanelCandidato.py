#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

class PanelCandidato(wx.Panel):
    """
    Panel que contiene la información de un candidato.
    """

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.TAB_TRAVERSAL, name=wx.PanelNameStr, nNumeroCandidato=None):

        # Enviamos todos los parametros a la clase padre.
        super().__init__(parent, id, pos, size, style, name)

        self.principal = parent
        self.numeroCandidato = nNumeroCandidato

        # Botón actualizar datos
        self.botonPorcentajeVotos = wx.Button(self, -1, 'Porcentaje Votos')
        self.botonPorcentajeVotos.SetSize(wx.Size(160, 20))
        self.Bind(wx.EVT_BUTTON, self.OnPorcentajeVotos, self.botonPorcentajeVotos)

        # Botón votar
        self.botonVotar = wx.Button(self, -1, 'Votar')
        self.botonVotar.SetSize(wx.Size(160, 20))
        self.Bind(wx.EVT_BUTTON, self.OnVotar, self.botonVotar)

        # Etiqueta nombre del candidato
        self.etiquetaNombreCandidato = wx.StaticText(self, -1, 'Nombre: ')

        # Etiqueta apellido del candidato
        self.etiquetaApellidoCandidato = wx.StaticText(self, -1, 'Apellido: ')

        # Etiqueta edad del candidato
        self.etiquetaEdadCandidato = wx.StaticText(self, -1, 'Edad: ')

        # Etiqueta partido político del candidato
        self.etiquetaPartidoPoliticoCandidato = wx.StaticText(self, -1, 'Partido Político: ')

        # Etiqueta costo campaña del candidato
        self.etiquetaCostoCampanhaCandidato = wx.StaticText(self, -1, 'Costo Campaña: $ ')

        # Etiqueta número de votos
        self.etiquetaNumeroVotos = wx.StaticText(self, -1, 'Numero de Votos: ')
        self.etiquetaNumeroVotos.SetForegroundColour('Red')

        # Construye la forma del panel
        sizerLayout = wx.FlexGridSizer(rows=9, cols=1, vgap=1, hgap=1)
        sizerLayoutImagen = wx.BoxSizer(wx.VERTICAL)

        # Configuramos la imagen del candidato
        rutaImagen = './Data/Candidato' + str(self.numeroCandidato) + '.gif'
        bitmap = wx.Bitmap(rutaImagen, wx.BITMAP_TYPE_GIF)
        imagen = wx.StaticBitmap(self, -1, bitmap)

        sizerLayoutImagen.Add(imagen, 1, wx.EXPAND)
        sizerLayout.Add(sizerLayoutImagen, 1)
        sizerLayout.Add(self.etiquetaNombreCandidato, 1, wx.ALIGN_LEFT)
        sizerLayout.Add(self.etiquetaApellidoCandidato, 1, wx.ALIGN_LEFT)
        sizerLayout.Add(self.etiquetaEdadCandidato, 1, wx.ALIGN_LEFT)
        sizerLayout.Add(self.etiquetaPartidoPoliticoCandidato, 1, wx.ALIGN_LEFT)
        sizerLayout.Add(self.etiquetaCostoCampanhaCandidato, 1, wx.ALIGN_LEFT)
        sizerLayout.Add(self.etiquetaNumeroVotos, 1, wx.ALIGN_CENTER)
        sizerLayout.Add(self.botonPorcentajeVotos, 0, wx.ALIGN_CENTER)
        sizerLayout.Add(self.botonVotar, 0, wx.ALIGN_CENTER)

        self.SetSizer(sizerLayout)
        self.Fit()

    def Actualizar(self, candidato):
        self.etiquetaNombreCandidato.SetLabelText( 'Nombre: ' + candidato.GetNombre() )
        self.etiquetaApellidoCandidato.SetLabelText( 'Apellido: ' + candidato.GetApellido())
        self.etiquetaEdadCandidato.SetLabelText( 'Edad: ' + str(candidato.GetEdad()) )
        self.etiquetaPartidoPoliticoCandidato.SetLabelText( 'Partido Poítico: ' + candidato.GetPartidoPolitico() )
        self.etiquetaCostoCampanhaCandidato.SetLabelText( 'Costo Campaña: $ ' + str(candidato.GetCostoCampanha()) )
        self.etiquetaNumeroVotos.SetLabelText( 'Número de Votos: ' + str(candidato.GetVotos()) )


    def FormatearValorReal(self):
        pass

    def OnPorcentajeVotos(self, event) -> None:
        """
        Manejo de eventos del usuario
        @param event: Evento de usuario. event != None
        """
        self.principal.MostrarDialogoPorcentajeVotos( self.numeroCandidato )

    def OnVotar(self, event) -> None:
        """
        Manejo de eventos del usuario.
        @param event: Evento de usuario. event != None
        """
        self.principal.AdicionarVotoCandidato( self.numeroCandidato )