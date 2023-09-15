from tolgas import tolgasAPI


def main():
    tolgas = tolgasAPI()
    print(tolgas.getTimetable(groupid=0, fromdate='02.10.2023', todate='08.10.2023'))


if __name__ == '__main__':
    main()
