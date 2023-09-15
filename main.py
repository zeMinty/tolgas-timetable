from tolgas import tolgasAPI

def main():
    tolgas = tolgasAPI()
    print(tolgas.getTimetable())

if __name__=='__main__':
    main()