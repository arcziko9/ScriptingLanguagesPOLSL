import glob
from datetime import date

html = open("page.html", 'w', encoding="utf-8")
path_1 = "input/input_*.txt"
path_2 = "output/output_*.txt"
today = date.today()
d1 = today.strftime("%Y_%m_%d")

files_in = glob.glob(path_1)
files_out = glob.glob(path_2)

input = []
output = []

for name in files_in:
    with open(name) as f:
        word = f.readlines()
        input += word
        f.close()

inputString = ""
count = 0
for i in input:
    count += 1
    if count % 2 == 0:
        inputString += "D = " + str(i) + "\n"
    if count % 2 != 0:
        inputString += "R = " + str(i)

tab = inputString.splitlines()
for i in tab:
    if i == '':
        tab.remove('')
newTab = []
i = 0

for x in range(0, len(tab)):
    if len(tab) - 1 > i:
        newTab.append(tab[i] + ", " + tab[i + 1])
    i+=2

for name in files_out:
    with open(name) as f:
        word = f.readlines()
        output += word
        f.close()

html.write('<!DOCTYPE HTML>\n'
           '<html lang="pl">\n<head>'
           '    <meta charset="utf-8" />\n'
           '    <title>Jezyki Skryptowe Projekt</title>\n'
           '    <meta name="descripton" content="Projekt Języki Skryptowe Arkadiusz Kałuża"/>\n'
           '    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/> \n'
           '    <link rel="stylesheet" href="style.css" type="text/css" /> \n'
           '    <link href="https://fonts.googleapis.com/css?family=Lato&display=swap" rel="stylesheet"> \n'
           '</head> \n'
           '<body> \n'
           '    <div id="container"> \n'
           '        <div id="header"> \n'
           '            "KŁOPOT ROWERZYSTY" - Algorytmion 2014 \n         '
           '        </div> \n'
           '        <div id="content"> \n'
           '            <div id="tab">\n'
           '                <table>\n'
           '                    <tr>\n'
           '                        <th>Promień i Dystans</th>\n'
           '                        <th>Droga przebyta przez muche</th>\n'
           '                    </tr>\n')
i = 0
j = 0


while (i != len(tab) and j!=len(output)):
    html.write('                 <tr>\n                     '
               '                       <td>')
    html.write(newTab[i].replace('\n', ''))
    html.write('</td>\n                     <td>')
    html.write(output[j].replace('\n', ''))
    html.write('</td> \n                 </tr>\n')
    i += 1
    j += 1

html.write('                </table>\n'
           '            </div>\n'
           '            <div id="txt">Ponizej zestwaienie danych wejsciowych i wyjsciowych </div> \n'
           '            <img src="images/chart_' + d1 + '.png"/>\n'
           '           </div> \n'
           '           <div id="footer"> \n'
           '                &copy Arkadiusz Kałuża, RMS POLSL \n'
           '           </div> \n'
           '    </div> \n'
           '</body> \n')
html.close()