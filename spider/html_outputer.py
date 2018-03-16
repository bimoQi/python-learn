# coding;utf-8

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        file = open('result.html', 'a+')

        file.write("<html>\n")
        file.write("\t<head>\n")
        file.write("\t\t<meta charset='utf-8'>\n")
        file.write("\t</head>\n")
        file.write("\t<body>\n")
        file.write("\t\t<table>\n")
        for data in self.datas:
            file.write("\t\t\t<tr width='100px'>\n")
            file.write("\t\t\t\t<td>")
            file.write(data['url'])
            file.write("</td>\n")
            file.write("\t\t\t\t<td>")
            file.write(data['title'])
            file.write("</td>\n")
            file.write("\t\t\t\t<td>")
            file.write(data['discript'])
            file.write("</td>\n")
            file.write("\t\t\t</tr>\n")
       
        file.write("\t\t</table>\n")
        file.write("\t</body>\n")
        file.write("</html>")

        file.close()
