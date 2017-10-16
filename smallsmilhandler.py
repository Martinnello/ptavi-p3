#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSmilHandler(ContentHandler):      # Handler para manejar smils

    def __init__(self):
        self.List = []
        self.Dc_Smil = {"root-layout": ['width', 'height', 'background-color'],
                        "region": ['id', 'top', 'bottom', 'left', 'right'],
                        "img": ['src', 'region', 'begin', 'dur'],
                        "audio": ['src', 'begin', 'dur'],
                        "textstream": ['src', 'region']}

    def startElement(self, name, attrs):      # Añade atributos a la lista

        if name in self.Dc_Smil:
            Dc_Atr = {}

            for atr in self.Dc_Smil[name]:
                Dc_Atr[atr] = attrs.get(atr, "")

            self.List.append([name, Dc_Atr])

    def get_tags(self):                   # Devuelve la lista de atributos
            return (self.List)

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSmilHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
