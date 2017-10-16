#!/usr/bin/python3
# -*- coding: utf-8 -*-

import smallsmilhandler
import sys
import json
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


if __name__ == "__main__":

    try:
        File = sys.argv[1]
        Fich = open(File)
        Fich.close()
    except FileNotFoundError:
        sys.exit("	 File not found!")
    except IndexError:
        sys.exit("    Usage:   python3 karaoke.py file.smil")

    parser = make_parser()
    cHandler = smallsmilhandler.SmallSmilHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(File))

    Lista = cHandler.get_tags()
    Descripcion = ""

    for name in Lista:

        Elemento = name[0]
        Atributos = name[1]
        Descripcion += Elemento + "\t"

        for Atributo in Atributos:
            Valor = Atributos[Atributo]

            if Valor != "":
                Descripcion += Atributo + '=' + Valor + "\t"

        Descripcion += "\n"

    print(Descripcion)

    FichJson = File.replace(".smil", ".json")

    with open(FichJson, "w") as jsonfile:
        json.dump(Lista, jsonfile, indent=3)
