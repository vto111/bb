import sys
sys.path.append('../')

from params import Params

class Template:

    def topCoin(self, data):
        # print(data)
        content = '<style type="text/css">.main th {font-size: 12px; text-align: right; border: solid 1px} .header {text-align: center !important;}</style>'
        content += '<table class="main">'
        content += '<tr class="header">'

        for coin_header in Params().descbb:
            content += '<th> ' + coin_header + ' </th>'
        content += '</tr>'

        for coin in data:
            content += '<tr>'
            for key in Params().descbb:

                content += '<th>' + data[coin][key] + '</th>'
                # print(data[coin][key])
            content +='</tr>'
        content += '<table>'
        return content

    def buttonReset(self):
        content = '<form action="http://bb.1cb.info:5000/reset"><button type="type="submit"">Reset</button></form>'
        return content

    def buttonBackHome(self):
        content = '<form action="http://bb.1cb.info:5000/"><button type="type="submit"">Back home</button></form>'
        return content