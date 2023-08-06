"""This module tests the methods of the file_index module in file_index.py."""

import pytest
from drivescanner import ingest


class TestReadBytes:
    test = [
        (
            "tests/testfiles/SQL test.sql",
            (b"select\t\t*\r\nfrom\t\tdbo.my_temp_table", None),
        ),
        (
            "tests/testfiles/R test.R",
            (
                b'# let\'s try something\r\np <- paste(p1, p2, sep = " ")\r\n\r\n# You can create a data frame with 3 columns and 4 rows like this:\r\nour_df <- data.frame(col1 = c(1,2,3,4), col2 = c("Y", "Y", "Y", "N"), col3 = c(T, F, F, T))\r\nour_df',
                None,
            ),
        ),
        (
            "tests/testfiles/Notebook test.ipynb",
            (
                b'{\r\n "cells": [\r\n  {\r\n   "attachments": {},\r\n   "cell_type": "markdown",\r\n   "metadata": {},\r\n   "source": [\r\n    "# This is a markdown cell with some text"\r\n   ]\r\n  },\r\n  {\r\n   "cell_type": "code",\r\n   "execution_count": 1,\r\n   "metadata": {},\r\n   "outputs": [],\r\n   "source": [\r\n    "def my_func(x, y):\\n",\r\n    "    return x + y"\r\n   ]\r\n  },\r\n  {\r\n   "cell_type": "code",\r\n   "execution_count": 2,\r\n   "metadata": {},\r\n   "outputs": [\r\n    {\r\n     "name": "stdout",\r\n     "output_type": "stream",\r\n     "text": [\r\n      "11\\n"\r\n     ]\r\n    }\r\n   ],\r\n   "source": [\r\n    "new_value = my_func(3, 8)\\n",\r\n    "print(new_value)"\r\n   ]\r\n  },\r\n  {\r\n   "cell_type": "code",\r\n   "execution_count": 3,\r\n   "metadata": {},\r\n   "outputs": [\r\n    {\r\n     "data": {\r\n      "text/plain": [\r\n       "\'wbeiuebvwekjcnkbv jwenv\'"\r\n      ]\r\n     },\r\n     "execution_count": 3,\r\n     "metadata": {},\r\n     "output_type": "execute_result"\r\n    }\r\n   ],\r\n   "source": [\r\n    "\\"wbeiuebvwe\\" + \\"kjcnkbv jwenv\\""\r\n   ]\r\n  },\r\n  {\r\n   "cell_type": "code",\r\n   "execution_count": null,\r\n   "metadata": {},\r\n   "outputs": [],\r\n   "source": []\r\n  }\r\n ],\r\n "metadata": {\r\n  "kernelspec": {\r\n   "display_name": "drivescanner",\r\n   "language": "python",\r\n   "name": "python3"\r\n  },\r\n  "language_info": {\r\n   "codemirror_mode": {\r\n    "name": "ipython",\r\n    "version": 3\r\n   },\r\n   "file_extension": ".py",\r\n   "mimetype": "text/x-python",\r\n   "name": "python",\r\n   "nbconvert_exporter": "python",\r\n   "pygments_lexer": "ipython3",\r\n   "version": "3.10.9"\r\n  },\r\n  "orig_nbformat": 4\r\n },\r\n "nbformat": 4,\r\n "nbformat_minor": 2\r\n}\r\n',
                None,
            ),
        ),
        (
            "tests/testfiles/test C.c",
            (
                b'#include <stdio.h>\r\nint main()\r\n{\r\n   char name[50];\r\n   int marks, i, num;\r\n\r\n   printf("Enter number of students: ");\r\n   scanf("%d", &num);\r\n\r\n   FILE *fptr;\r\n   fptr = (fopen("C:\\\\student.txt", "w"));\r\n   if(fptr == NULL)\r\n   {\r\n       printf("Error!");\r\n       exit(1);\r\n   }\r\n\r\n   for(i = 0; i < num; ++i)\r\n   {\r\n      printf("For student%d\\nEnter name: ", i+1);\r\n      scanf("%s", name);\r\n\r\n      printf("Enter marks: ");\r\n      scanf("%d", &marks);\r\n\r\n      fprintf(fptr,"\\nName: %s \\nMarks=%d \\n", name, marks);\r\n   }\r\n\r\n   fclose(fptr);\r\n   return 0;\r\n}',
                None,
            ),
        ),
        (
            "tests/testfiles/JSON test.json",
            (
                b'{\r\n    "glossary": {\r\n        "title": "example glossary",\r\n\t\t"GlossDiv": {\r\n            "title": "S",\r\n\t\t\t"GlossList": {\r\n                "GlossEntry": {\r\n                    "ID": "SGML",\r\n\t\t\t\t\t"SortAs": "SGML",\r\n\t\t\t\t\t"GlossTerm": "Standard Generalized Markup Language",\r\n\t\t\t\t\t"Acronym": "SGML",\r\n\t\t\t\t\t"Abbrev": "ISO 8879:1986",\r\n\t\t\t\t\t"GlossDef": {\r\n                        "para": "A meta-markup language, used to create markup languages such as DocBook.",\r\n\t\t\t\t\t\t"GlossSeeAlso": ["GML", "XML"]\r\n                    },\r\n\t\t\t\t\t"GlossSee": "markup"\r\n                }\r\n            }\r\n        }\r\n    }\r\n}',
                None,
            ),
        ),
        (
            "tests/testfiles/HTML test.html",
            (
                b"<!DOCTYPE html>\r\n<html>\r\n<body>\r\n\r\n<h1>My First Heading</h1>\r\n\r\n<p>My first paragraph.</p>\r\n\r\n</body>\r\n</html>",
                None,
            ),
        ),
        (
            "tests/testfiles/XML test.xml",
            (
                b'<!DOCTYPE glossary PUBLIC "-//OASIS//DTD DocBook V3.1//EN">\r\n <glossary><title>example glossary</title>\r\n  <GlossDiv><title>S</title>\r\n   <GlossList>\r\n    <GlossEntry ID="SGML" SortAs="SGML">\r\n     <GlossTerm>Standard Generalized Markup Language</GlossTerm>\r\n     <Acronym>SGML</Acronym>\r\n     <Abbrev>ISO 8879:1986</Abbrev>\r\n     <GlossDef>\r\n      <para>A meta-markup language, used to create markup\r\nlanguages such as DocBook.</para>\r\n      <GlossSeeAlso OtherTerm="GML">\r\n      <GlossSeeAlso OtherTerm="XML">\r\n     </GlossDef>\r\n     <GlossSee OtherTerm="markup">\r\n    </GlossEntry>\r\n   </GlossList>\r\n  </GlossDiv>\r\n </glossary>',
                None,
            ),
        ),
        (
            "tests/testfiles/HTM test.htm",
            (
                b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"\r\n   "http://www.w3.org/TR/html4/strict.dtd">\r\n<HTML>\r\n   <HEAD>\r\n      <TITLE>Understanding HTML File Format</TITLE>\r\n   </HEAD>\r\n   <BODY>\r\n      <P>Hello World!\r\n   </BODY>\r\n</HTML>',
                None,
            ),
        ),
        (
            "tests/testfiles/Python test.py",
            (
                b'# Use of String Formatting\r\nfloat1 = 563.78453\r\nprint("{:5.2f}".format(float1))\r\n\r\n# Use of String Interpolation\r\nfloat2 = 563.78453\r\nprint("%5.2f" % float2)',
                None,
            ),
        ),
        (
            "tests/testfiles/Lipsum.txt",
            (
                b"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas at erat at diam volutpat laoreet sit amet non leo.",
                None,
            ),
        ),
        (
            "tests/testfiles/circuits.csv",
            (
                b'circuitId,circuitRef,name,location,country,lat,lng,alt,url\r\n1,albert_park,Albert Park Grand Prix Circuit,Melbourne,Australia,-37.8497,144.968,10,http://en.wikipedia.org/wiki/Melbourne_Grand_Prix_Circuit\r\n2,sepang,Sepang International Circuit,Kuala Lumpur,Malaysia,2.76083,101.738,,http://en.wikipedia.org/wiki/Sepang_International_Circuit\r\n3,bahrain,Bahrain International Circuit,Sakhir,Bahrain,26.0325,50.5106,,http://en.wikipedia.org/wiki/Bahrain_International_Circuit\r\n4,catalunya,Circuit de Barcelona-Catalunya,Montmel\xcc_,Spain,41.57,2.26111,,http://en.wikipedia.org/wiki/Circuit_de_Barcelona-Catalunya\r\n5,istanbul,Istanbul Park,Istanbul,Turkey,40.9517,29.405,,http://en.wikipedia.org/wiki/Istanbul_Park\r\n6,monaco,Circuit de Monaco,Monte-Carlo,Monaco,43.7347,7.42056,,http://en.wikipedia.org/wiki/Circuit_de_Monaco\r\n7,villeneuve,Circuit Gilles Villeneuve,Montreal,Canada,45.5,-73.5228,,http://en.wikipedia.org/wiki/Circuit_Gilles_Villeneuve\r\n8,magny_cours,Circuit de Nevers Magny-Cours,Magny Cours,France,46.8642,3.16361,,http://en.wikipedia.org/wiki/Circuit_de_Nevers_Magny-Cours\r\n9,silverstone,Silverstone Circuit,Silverstone,UK,52.0786,-1.01694,,http://en.wikipedia.org/wiki/Silverstone_Circuit\r\n10,hockenheimring,Hockenheimring,Hockenheim,Germany,49.3278,8.56583,,http://en.wikipedia.org/wiki/Hockenheimring\r\n11,hungaroring,Hungaroring,Budapest,Hungary,47.5789,19.2486,,http://en.wikipedia.org/wiki/Hungaroring\r\n12,valencia,Valencia Street Circuit,Valencia,Spain,39.4589,-0.331667,,http://en.wikipedia.org/wiki/Valencia_Street_Circuit\r\n13,spa,Circuit de Spa-Francorchamps,Spa,Belgium,50.4372,5.97139,,http://en.wikipedia.org/wiki/Circuit_de_Spa-Francorchamps\r\n14,monza,Autodromo Nazionale di Monza,Monza,Italy,45.6156,9.28111,,http://en.wikipedia.org/wiki/Autodromo_Nazionale_Monza\r\n15,marina_bay,Marina Bay Street Circuit,Marina Bay,Singapore,1.2914,103.864,,http://en.wikipedia.org/wiki/Marina_Bay_Street_Circuit\r\n16,fuji,Fuji Speedway,Oyama,Japan,35.3717,138.927,,http://en.wikipedia.org/wiki/Fuji_Speedway\r\n17,shanghai,Shanghai International Circuit,Shanghai,China,31.3389,121.22,,http://en.wikipedia.org/wiki/Shanghai_International_Circuit\r\n18,interlagos,Aut\xcc_dromo Jos\xcc\xa9 Carlos Pace,S\xcc\xa3o Paulo,Brazil,-23.7036,-46.6997,,http://en.wikipedia.org/wiki/Aut%C3%B3dromo_Jos%C3%A9_Carlos_Pace\r\n19,indianapolis,Indianapolis Motor Speedway,Indianapolis,USA,39.795,-86.2347,,http://en.wikipedia.org/wiki/Indianapolis_Motor_Speedway\r\n20,nurburgring,N\xcc_rburgring,N\xcc_rburg,Germany,50.3356,6.9475,,http://en.wikipedia.org/wiki/N%C3%BCrburgring\r\n21,imola,Autodromo Enzo e Dino Ferrari,Imola,Italy,44.3439,11.7167,,http://en.wikipedia.org/wiki/Autodromo_Enzo_e_Dino_Ferrari\r\n22,suzuka,Suzuka Circuit,Suzuka,Japan,34.8431,136.541,,http://en.wikipedia.org/wiki/Suzuka_Circuit\r\n23,osterreichring,A1-Ring,Spielburg,Austria,47.2197,14.7647,,http://en.wikipedia.org/wiki/A1-Ring\r\n24,yas_marina,Yas Marina Circuit,Abu Dhabi,UAE,24.4672,54.6031,,http://en.wikipedia.org/wiki/Yas_Marina_Circuit\r\n25,galvez,Aut\xcc_dromo Juan y Oscar G\xcc\xc1lvez,Buenos Aires,Argentina,-34.6943,-58.4593,,http://en.wikipedia.org/wiki/Aut%C3%B3dromo_Oscar_Alfredo_G%C3%A1lvez\r\n26,jerez,Circuito de Jerez,Jerez de la Frontera,Spain,36.7083,-6.03417,,http://en.wikipedia.org/wiki/Circuito_Permanente_de_Jerez\r\n27,estoril,Aut\xcc_dromo do Estoril,Estoril,Portugal,38.7506,-9.39417,,http://en.wikipedia.org/wiki/Aut%C3%B3dromo_do_Estoril\r\n28,okayama,Okayama International Circuit,Okayama,Japan,34.915,134.221,,http://en.wikipedia.org/wiki/TI_Circuit\r\n29,adelaide,Adelaide Street Circuit,Adelaide,Australia,-34.9272,138.617,,http://en.wikipedia.org/wiki/Adelaide_Street_Circuit\r\n30,kyalami,Kyalami,Midrand,South Africa,-25.9894,28.0767,,http://en.wikipedia.org/wiki/Kyalami\r\n31,donington,Donington Park,Castle Donington,UK,52.8306,-1.37528,,http://en.wikipedia.org/wiki/Donington_Park\r\n32,rodriguez,Aut\xcc_dromo Hermanos Rodr\xcc_guez,Mexico City,Mexico,19.4042,-99.0907,,http://en.wikipedia.org/wiki/Aut%C3%B3dromo_Hermanos_Rodr%C3%ADguez\r\n33,phoenix,Phoenix street circuit,Phoenix,USA,33.4479,-112.075,,http://en.wikipedia.org/wiki/Phoenix_street_circuit\r\n34,ricard,Circuit Paul Ricard,Le Castellet,France,43.2506,5.79167,,http://en.wikipedia.org/wiki/Paul_Ricard_Circuit\r\n35,yeongam,Korean International Circuit,Yeongam County,Korea,34.7333,126.417,,http://en.wikipedia.org/wiki/Korean_International_Circuit\r\n36,jacarepagua,Aut\xcc_dromo Internacional Nelson Piquet,Rio de Janeiro,Brazil,-22.9756,-43.395,,http://en.wikipedia.org/wiki/Aut%C3%B3dromo_Internacional_Nelson_Piquet\r\n37,detroit,Detroit Street Circuit,Detroit,USA,42.3298,-83.0401,,http://en.wikipedia.org/wiki/Detroit_street_circuit\r\n38,brands_hatch,Brands Hatch,Kent,UK,51.3569,0.263056,,http://en.wikipedia.org/wiki/Brands_Hatch\r\n39,zandvoort,Circuit Park Zandvoort,Zandvoort,Netherlands,52.3888,4.54092,,http://en.wikipedia.org/wiki/Circuit_Zandvoort\r\n40,zolder,Zolder,Heusden-Zolder,Belgium,50.9894,5.25694,,http://en.wikipedia.org/wiki/Zolder\r\n41,dijon,Dijon-Prenois,Dijon,France,47.3625,4.89913,,http://en.wikipedia.org/wiki/Dijon-Prenois\r\n42,dallas,Fair Park,Dallas,USA,32.7774,-96.7587,,http://en.wikipedia.org/wiki/Fair_Park\r\n43,long_beach,Long Beach,California,USA,33.7651,-118.189,,"http://en.wikipedia.org/wiki/Long_Beach,_California"\r\n44,las_vegas,Las Vegas Street Circuit,Nevada,USA,36.1162,-115.174,,"http://en.wikipedia.org/wiki/Las_Vegas,_Nevada"\r\n45,jarama,Jarama,Madrid,Spain,40.6171,-3.58558,,http://en.wikipedia.org/wiki/Circuito_Permanente_Del_Jarama\r\n46,watkins_glen,Watkins Glen,New York State,USA,42.3369,-76.9272,,http://en.wikipedia.org/wiki/Watkins_Glen_International\r\n47,anderstorp,Scandinavian Raceway,Anderstorp,Sweden,57.2653,13.6042,,http://en.wikipedia.org/wiki/Scandinavian_Raceway\r\n48,mosport,Mosport International Raceway,Ontario,Canada,44.0481,-78.6756,,http://en.wikipedia.org/wiki/Mosport\r\n49,montjuic,Montju\xcc\xf8c,Barcelona,Spain,41.3664,2.15167,,http://en.wikipedia.org/wiki/Montju%C3%AFc_circuit\r\n50,nivelles,Nivelles-Baulers,Brussels,Belgium,50.6211,4.32694,,http://en.wikipedia.org/wiki/Nivelles-Baulers\r\n51,charade,Charade Circuit,Clermont-Ferrand,France,45.7472,3.03889,,http://en.wikipedia.org/wiki/Charade_Circuit\r\n52,tremblant,Circuit Mont-Tremblant,Quebec,Canada,46.1877,-74.6099,,http://en.wikipedia.org/wiki/Circuit_Mont-Tremblant\r\n53,essarts,Rouen-Les-Essarts,Rouen,France,49.3306,1.00458,,http://en.wikipedia.org/wiki/Rouen-Les-Essarts\r\n54,lemans,Le Mans,Le Mans,France,47.95,0.224231,,http://en.wikipedia.org/wiki/Circuit_de_la_Sarthe#Bugatti_Circuit\r\n55,reims,Reims-Gueux,Reims,France,49.2542,3.93083,,http://en.wikipedia.org/wiki/Reims-Gueux\r\n56,george,Prince George Circuit,Eastern Cape Province,South Africa,-33.0486,27.8736,,http://en.wikipedia.org/wiki/Prince_George_Circuit\r\n57,zeltweg,Zeltweg,Styria,Austria,47.2039,14.7478,,http://en.wikipedia.org/wiki/Zeltweg_Airfield\r\n58,aintree,Aintree,Liverpool,UK,53.4769,-2.94056,,http://en.wikipedia.org/wiki/Aintree_Motor_Racing_Circuit\r\n59,boavista,Circuito da Boavista,Oporto,Portugal,41.1705,-8.67325,,http://en.wikipedia.org/wiki/Circuito_da_Boavista\r\n60,riverside,Riverside International Raceway,California,USA,33.937,-117.273,,http://en.wikipedia.org/wiki/Riverside_International_Raceway\r\n61,avus,AVUS,Berlin,Germany,52.4806,13.2514,,http://en.wikipedia.org/wiki/AVUS\r\n62,monsanto,Monsanto Park Circuit,Lisbon,Portugal,38.7197,-9.20306,,http://en.wikipedia.org/wiki/Monsanto_Park_Circuit\r\n63,sebring,Sebring International Raceway,Florida,USA,27.4547,-81.3483,,http://en.wikipedia.org/wiki/Sebring_Raceway\r\n64,ain-diab,Ain Diab,Casablanca,Morocco,33.5786,-7.6875,,http://en.wikipedia.org/wiki/Ain-Diab_Circuit\r\n65,pescara,Pescara Circuit,Pescara,Italy,42.475,14.1508,,http://en.wikipedia.org/wiki/Pescara_Circuit\r\n66,bremgarten,Circuit Bremgarten,Bern,Switzerland,46.9589,7.40194,,http://en.wikipedia.org/wiki/Circuit_Bremgarten\r\n67,pedralbes,Circuit de Pedralbes,Barcelona,Spain,41.3903,2.11667,,http://en.wikipedia.org/wiki/Pedralbes_Circuit\r\n68,buddh,Buddh International Circuit,Uttar Pradesh,India,28.3487,77.5331,,http://en.wikipedia.org/wiki/Buddh_International_Circuit\r\n69,americas,Circuit of the Americas,Austin,USA,30.1328,-97.6411,,http://en.wikipedia.org/wiki/Circuit_of_the_Americas\r\n70,red_bull_ring,Red Bull Ring,Spielburg,Austria,47.2197,14.7647,,http://en.wikipedia.org/wiki/Red_Bull_Ring\r\n71,sochi,Sochi Autodrom,Sochi,Russia,43.4057,39.9578,,http://en.wikipedia.org/wiki/Sochi_Autodrom\r\n72,port_imperial,Port Imperial Street Circuit,New Jersey,USA,40.7769,-74.0111,,http://en.wikipedia.org/wiki/Port_Imperial_Street_Circuit\r\n73,BAK,Baku City Circuit,Baku,Azerbaijan,40.3725,49.8533,,http://en.wikipedia.org/wiki/Baku_City_Circuit',
                None,
            ),
        ),
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_read_bytes(self, input, expected):
        result = ingest._read_bytes(input)
        assert result == expected


class TestReadDocx:
    test = [
        (
            "tests/testfiles/Word test doc.docx",
            (
                "Deze tekst wordt gebruikt om te testen\n\nDeze tekst wordt gebruikt om te testen\n\n\n\n\n\n\n\n\n\nKomt deze tekst mee? :)",
                None,
            ),
        ),
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_read_docx(self, input, expected):
        result = ingest._read_docx(input)
        assert result == expected


class TestReadXlsx:
    test = [
        (
            "tests/testfiles/Excel test Excel.xlsx",
            "{'Tab_1':        Kolom1 Kolom2\n0  Test info!    abc\n1         #$%    XYZ, 'Tab2': Empty DataFrame\nColumns: [Komt deze mee?]\nIndex: []}",
        ),
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_read_xlsx(self, input, expected):
        result, _ = ingest._read_xlsx(input)
        assert result == expected


class TestReadPptx:
    test = [
        (
            "tests/testfiles/testpresentatie.pptx",
            (
                'Dit  is  een  test Dit  is de  subpagina ,  hier  zit  geen   gevoelige   informatie  in Maar we  kunnen   wel   doen   alsof  er  een  username  en  ww in zit  Wie  houdt  er  niet  van WordArt! ',
                None,
            ),
        ),
    ]

    @pytest.mark.parametrize("input, expected", test)
    def test_read_pptx(self, input, expected):
        result = ingest._read_pptx(input)
        assert result == expected
