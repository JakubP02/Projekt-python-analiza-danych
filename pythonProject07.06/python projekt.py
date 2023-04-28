import pandas as pd
import matplotlib.pyplot as plt
import csv

def funkcja_wpisz_rok():
    df_btc_zloto_2014 = df_btc_zloto.iloc[0:364]
    df_btc_zloto_2015 = df_btc_zloto.iloc[364:729]
    df_btc_zloto_2016 = df_btc_zloto.iloc[729:1095]
    df_btc_zloto_2017 = df_btc_zloto.iloc[1095:1460]
    df_btc_zloto_2018 = df_btc_zloto.iloc[1460:1825]
    df_btc_zloto_2019 = df_btc_zloto.iloc[1825:2190]
    df_btc_zloto_2020 = df_btc_zloto.iloc[2190:2310]

    print("wpisz rok w przedziale 2014-2020, a obliczę dla Ciebie średnią, wartość min i max cene Btc i złota w danym roku  ")

    try:
        rok = int(input())

        if rok == 2014:
            print("btc najniższa wartość")
            print(df_btc_zloto_2014['BTC price [USD]'].min(), 'USD')
            print("btc największa wartość")
            print(df_btc_zloto_2014['BTC price [USD]'].max(), 'USD')
            print("btc średnia wartość")
            print(df_btc_zloto_2014['BTC price [USD]'].mean(), 'USD')
            print("złoto najniższa wartość")
            print(df_btc_zloto_2014['Gold price[USD]'].min(), 'USD')
            print("złoto największa wartość")
            print(df_btc_zloto_2014['Gold price[USD]'].max(), 'USD')
            print("złoto średnia wartość")
            print(df_btc_zloto_2014['Gold price[USD]'].mean(), 'USD')
            x = df_btc_zloto_2014['Date']
            y = df_btc_zloto_2014['BTC price [USD]']
            y2 = df_btc_zloto_2014['Gold price[USD]']

            plt.plot(x, y)
            plt.plot(x, y2)
            plt.legend(['cena btc', 'cena złota'])
            plt.show()

        if rok == 2015:
            print("btc najniższa wartość")
            print(df_btc_zloto_2015['BTC price [USD]'].min())
            print("btc największa wartość")
            print(df_btc_zloto_2015['BTC price [USD]'].max())
            print("btc średnia wartość")
            print(df_btc_zloto_2015['BTC price [USD]'].mean())
            print("złoto najniższa wartość")
            print(df_btc_zloto_2015['Gold price[USD]'].min(), 'USD')
            print("złoto największa wartość")
            print(df_btc_zloto_2015['Gold price[USD]'].max(), 'USD')
            print("złoto średnia wartość")
            print(df_btc_zloto_2015['Gold price[USD]'].mean(), 'USD')
            x = df_btc_zloto_2015['Date']
            y = df_btc_zloto_2015['BTC price [USD]']
            y2 = df_btc_zloto_2015['Gold price[USD]']

            plt.plot(x, y)
            plt.plot(x, y2)
            plt.legend(['cena btc', 'cena złota'])
            plt.show()

        if rok == 2016:
            print("btc najniższa wartość")
            print(df_btc_zloto_2016['BTC price [USD]'].min())
            print("btc największa wartość")
            print(df_btc_zloto_2016['BTC price [USD]'].max())
            print("btc średnia wartość")
            print(df_btc_zloto_2016['BTC price [USD]'].mean())
            print("złoto najniższa wartość")
            print(df_btc_zloto_2016['Gold price[USD]'].min(), 'USD')
            print("złoto największa wartość")
            print(df_btc_zloto_2016['Gold price[USD]'].max(), 'USD')
            print("złoto średnia wartość")
            print(df_btc_zloto_2016['Gold price[USD]'].mean(), 'USD')
            x = df_btc_zloto_2016['Date']
            y = df_btc_zloto_2016['BTC price [USD]']
            y2 = df_btc_zloto_2016['Gold price[USD]']

            plt.plot(x, y)
            plt.plot(x, y2)
            plt.legend(['cena btc', 'cena złota'])
            plt.show()
        if rok == 2017:
           print("btc najniższa wartość")
           print(df_btc_zloto_2017['BTC price [USD]'].min())
           print("btc największa wartość")
           print(df_btc_zloto_2017['BTC price [USD]'].max())
           print("btc średnia wartość")
           print(df_btc_zloto_2017['BTC price [USD]'].mean())
           print("złoto najniższa wartość")
           print(df_btc_zloto_2017['Gold price[USD]'].min(), 'USD')
           print("złoto największa wartość")
           print(df_btc_zloto_2017['Gold price[USD]'].max(), 'USD')
           print("złoto średnia wartość")
           print(df_btc_zloto_2017['Gold price[USD]'].mean(), 'USD')
           x = df_btc_zloto_2017['Date']
           y = df_btc_zloto_2017['BTC price [USD]']
           y2 = df_btc_zloto_2017['Gold price[USD]']

           plt.plot(x, y)
           plt.plot(x, y2)
           plt.legend(['cena btc', 'cena złota'])
           plt.show()

        if rok == 2018:
           print("btc najniższa wartość")
           print(df_btc_zloto_2018['BTC price [USD]'].min())
           print("btc największa wartość")
           print(df_btc_zloto_2018['BTC price [USD]'].max())
           print("btc średnia wartość")
           print(df_btc_zloto_2018['BTC price [USD]'].mean())
           print("złoto najniższa wartość")
           print(df_btc_zloto_2018['Gold price[USD]'].min(), 'USD')
           print("złoto największa wartość")
           print(df_btc_zloto_2018['Gold price[USD]'].max(), 'USD')
           print("złoto średnia wartość")
           print(df_btc_zloto_2018['Gold price[USD]'].mean(), 'USD')
           x = df_btc_zloto_2018['Date']
           y = df_btc_zloto_2018['BTC price [USD]']
           y2 = df_btc_zloto_2018['Gold price[USD]']

           plt.plot(x, y)
           plt.plot(x, y2)
           plt.legend(['cena btc', 'cena złota'])
           plt.show()

        if rok == 2019:
           print("btc najniższa wartość")
           print(df_btc_zloto_2019['BTC price [USD]'].min())
           print("btc największa wartość")
           print(df_btc_zloto_2019['BTC price [USD]'].max())
           print("btc średnia wartość")
           print(df_btc_zloto_2019['BTC price [USD]'].mean())
           print("złoto najniższa wartość")
           print(df_btc_zloto_2019['Gold price[USD]'].min(), 'USD')
           print("złoto największa wartość")
           print(df_btc_zloto_2019['Gold price[USD]'].max(), 'USD')
           print("złoto średnia wartość")
           print(df_btc_zloto_2019['Gold price[USD]'].mean(), 'USD')
           x = df_btc_zloto_2019['Date']
           y = df_btc_zloto_2019['BTC price [USD]']
           y2 = df_btc_zloto_2019['Gold price[USD]']

           plt.plot(x, y)
           plt.plot(x, y2)
           plt.legend(['cena btc', 'cena złota'])
           plt.show()

        if rok == 2020:
           print("btc najniższa wartość")
           print(df_btc_zloto_2020['BTC price [USD]'].min())
           print("btc największa wartość")
           print(df_btc_zloto_2020['BTC price [USD]'].max())
           print("btc średnia wartość")
           print(df_btc_zloto_2020['BTC price [USD]'].mean())
           print("złoto najniższa wartość")
           print(df_btc_zloto_2020['Gold price[USD]'].min(), 'USD')
           print("złoto największa wartość")
           print(df_btc_zloto_2020['Gold price[USD]'].max(), 'USD')
           print("złoto średnia wartość")
           print(df_btc_zloto_2020['Gold price[USD]'].mean(), 'USD')
           x = df_btc_zloto_2020['Date']
           y = df_btc_zloto_2020['BTC price [USD]']
           y2 = df_btc_zloto_2020['Gold price[USD]']

           plt.plot(x, y)
           plt.plot(x, y2)
           plt.legend(['cena btc', 'cena złota'])
           plt.show()
    except(rok > 2020 & rok < 2014):
        print('zły rok')


try:
    print("przedstwione dane dotyczą kursu ceny bitcoina i ceny złota od 2014r. do 2020r.")

    df = pd.read_csv('plik.csv')
    print(
        "teraz zobazcysz jak zmieniała się cena bitcoina i złota (w USD ) z dnia na dzień począwszy od 02.01.2014r do  29.04.2020r.")
    df_btc_zloto = df[['Date', 'BTC price [USD]', 'Gold price[USD]']].copy()
    print(df_btc_zloto)

    naj_btc = df_btc_zloto['BTC price [USD]'].min()
    najw_btc = df_btc_zloto['BTC price [USD]'].max()
    średnia_btc = df_btc_zloto['BTC price [USD]'].mean()

    print("najniższa wartość btc w analizowanym okresie to ", naj_btc)
    print("najwyższa wartość btc w analizowanym okresie to ", najw_btc)
    print("srednia btc w analizowanym okresie to ", średnia_btc)

    naj_zl = df_btc_zloto['Gold price[USD]'].min()
    najw_zl = df_btc_zloto['Gold price[USD]'].max()
    średnia_zl = df_btc_zloto['Gold price[USD]'].mean()

    print("najniższa wartość złota w analizowanym okresie to ", naj_zl)
    print("najwyższa wartość złota w analizowanym okresie to ", najw_zl)
    print("średnia wartość złota w analizowanym okresie to ", średnia_zl)

    list = ['najwyzsza wartosc BTC', 'najnizsza wartość btc', 'srednia btc', 'najnizsza wartosc złota',
            'najwyzsza wartosc złota ', 'srednia wartosc złota ']
    list2 = [najw_btc, naj_btc, średnia_btc, naj_zl, najw_zl, średnia_zl]

    try:
        with open('statystyka zapis.csv', 'w', newline='') as plikCSV:
            writer = csv.writer(plikCSV)
            for i in range(list.__len__()):
                writer.writerow([list[i], list2[i]])
    except(FileNotFoundError):
        print("brak pliku")

    df_btc_zloto['róznica w % miedzy BTC a ZL'] = round((df_btc_zloto['BTC price [USD]'] - df_btc_zloto['Gold price[USD]']) / df_btc_zloto['Gold price[USD]'] * 100, 2)
    df_btc_zloto.to_csv('plik zapis.csv')

    funkcja_wpisz_rok()

    x = df_btc_zloto['Date']
    y = df_btc_zloto['BTC price [USD]']
    y2 = df_btc_zloto['Gold price[USD]']

    plt.plot(x, y)
    plt.plot(x, y2)

    plt.legend(['cena btc', 'cena złota', 'róznica w % miedzy BTC a ZL'])
    plt.show()


    def wykres_róznica():
        x = df_btc_zloto['Date']
        y3 = df_btc_zloto['róznica w % miedzy BTC a ZL']
        plt.plot(x, y3)
        plt.legend(['róznica w % miedzy BTC a ZL'])
        plt.show()


    wykres_róznica()
except(FileNotFoundError):
    print("brak pliku")