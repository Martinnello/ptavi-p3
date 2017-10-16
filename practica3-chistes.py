#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class ChistesHandler(ContentHandler):
    """
    Clase para manejar chistes malos
    """

    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """
        self.calificacion = ""
        self.pregunta = ""
        self.inPregunta = 1
        self.respuesta = ""
        self.inRespuesta = 1

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'chiste':
            # De esta manera tomamos los valores de los atributos
            self.calificacion = attrs.get('calificacion', "")
            print self.calificacion

    def endElement(self, name):
        """
        Método que se llama al cerrar una etiqueta
        """
        if name == 'pregunta':
            self.inPregunta = 1
            print self.pregunta
        if name == 'respuesta':
            self.inRespuesta = 1
            print self.respuesta

    def characters(self, char):
        """
        Método para tomar contenido de la etiqueta
        """
        if self.inPregunta:
            self.pregunta = char
        if self.inRespuesta:
            self.respuesta = char

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = ChistesHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('chistes2.xml'))
