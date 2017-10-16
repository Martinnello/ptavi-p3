#!/usr/bin/python3
# -*- coding: utf-8 -*-

import smallsmilhandler
import sys
import json
<<<<<<< HEAD
import urllib.request
=======
>>>>>>> e37c1fbb099b2e25c0ee28c38c67176c9f2cfcc8
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


<<<<<<< HEAD
class KaraokeLocal:                         # TAKE SMIL FILE & READ IT

    def __init__(self):

        try:
            File = sys.argv[1]
        except FileNotFoundError:
            sys.exit("	 File not found!")
        except IndexError:
            sys.exit("    Usage:   python3 karaoke.py file.smil")

        parser = make_parser()
        cHandler = smallsmilhandler.SmallSmilHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(File))
        self.Lista = cHandler.get_tags()

    def __str__(self):                          # GET ELEMENTS & ATRIBUTES

        self.Description = ""

        for name in self.Lista:
            Elemento = name[0]
            Atributos = name[1]
            self.Description += Elemento + "\t"

            for Atributo in Atributos:
                Valor = Atributos[Atributo]
                if Valor != "":
                    self.Description += Atributo + '= "' + Valor + '"\t'
            self.Description += "\n"

        print(self.Description)

    def to_json(self, F_Smil, F_Json=""):       # MAKE JSON FILE

        if F_Json == "":
            F_Json = F_Smil.replace(".smil", ".json")
        with open(F_Json, "w") as jsonfile:
            json.dump(self.Lista, jsonfile, indent=3)

    def do_local(self):                          # MAKE DOWNLOADS LOCAL

        for name in self.Lista:
            Elemento = name[0]
            Atributos = name[1]

            for Atributo in Atributos:
                if Atributo == "src":
                    url = Atributos[Atributo]
                    if url.startswith("http://"):
                        Download = url.split("/")[-1]
                        urllib.request.urlretrieve(url, Download)
                        Atributos[Atributo] = Download

if __name__ == "__main__":

    Smil = KaraokeLocal()
    Smil.__str__()
    Smil.to_json(sys.argv[1])
    Smil.do_local()
    Smil.to_json(sys.argv[1], "local.json")
    Smil.__str__()
=======
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
>>>>>>> e37c1fbb099b2e25c0ee28c38c67176c9f2cfcc8
