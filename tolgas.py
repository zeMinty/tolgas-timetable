from requests import post
from parsel import Selector
from re import match as matchRegex


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
            'submit_button': '%D0%9F%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C'  # Показать
        }

    def getTimetable(self, groupid: int, fromdate: str, todate: str):
        url = self.baseurl + self.timetablepath + '?id=0'
        params = self.params
        params['vr'] = groupid
        params['from'] = fromdate
        params['to'] = todate

        response = post(url, data=params)

        if response.status_code == 200:
            html = Selector(response.text)
            data = html.xpath('//div[@id="send"]//text()').getall()

            data = self._prepareTimetable(data)

            return data
        else:
            raise ValueError(f'Не удалось получить данные: status_code={response.status_code}')

    def _prepareTimetable(self, data: list):
        trimmedData = list(map(lambda s: s.strip('\n '+"\t"), data))
        filteredData = list(filter(lambda s: s != '', trimmedData))

        out = {}
        step = 0
        date = None
        num = None
        template = {
            'fromtime': '?',
            'totime': '?',
            'name': '?',
            'type': '?',
            'auditory': '?',
            'teacher': '?',
            'groups': '?'
        }
        info = list(template.keys())
        maxStep = len(info)-1
        for i in filteredData:
            if matchRegex(r'\d{2}\.\d{2}\.\d{4}', i):
                date = i
                out[date] = {}
                continue

            if matchRegex(r'^\d+$', i):
                step = 0
                num = i
                out[date][num] = template.copy()
                continue

            out[date][num][info[step]] = i

            step += 1
            if step > maxStep:
                step = 0

        return out
