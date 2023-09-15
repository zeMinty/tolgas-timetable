from requests import post
from parsel import Selector


class tolgasAPI:
    def __init__(self) -> None:
        self.baseurl = 'https://www.tolgas.ru/'
        self.timetablepath = 'services/raspisanie/'

        self.params = {
            'rel': 0,
            'grp': 0,
            'prep': 0,
            'audi': 0,
            'vr': 0,
            'from': 0,
            'to': 0,
            'submit_button': '%D0%9F%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C'
        }

    def getTimetable(self, groupid=369, fromdate='02.10.2023', todate='08.10.2023'):
        url = self.baseurl + self.timetablepath + '?id=0'
        response = post(url, data=self.params)

        if response.status_code == 200:
            html = Selector(response.text)
            data = html.xpath('//div[@id="send"]//text()').getall()

            out = []
            for s in data:
                d = s.strip('\n '+"\t")
                if d != '':
                    out.append(d)
            data = "\n".join(out)

            if data is not None:
                with open('data.txt', 'w') as f:
                    f.write(data)

            print(data)
        else:
            raise ValueError('Не удалось получить данные')