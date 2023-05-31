![](./screenshoty/Aspose.Words.1d35b0d7-c9b0-4d8a-9bbe-6a9e4c5f230f.001.png)
![](./screenshoty/Aspose.Words.1d35b0d7-c9b0-4d8a-9bbe-6a9e4c5f230f.002.png)
# <a name="_d9gva4ohikyd"></a><a name="_nle527xs3ni2"></a>Programowanie Full-Stack w Chmurze Obliczeniowej 
**Sprawozdanie 1**


`								`Prowadzący 

Sebastian Słupny						Sławomir Przyłucki
**



**


**1. (max. 20%)** 
Proszę napisać program serwera (dowolny język programowania), który realizować będzie następującą funkcjonalność:


![](./screenshoty/Aspose.Words.1d35b0d7-c9b0-4d8a-9bbe-6a9e4c5f230f.003.png)

Kod server.py


**2. (max. 50%)** 
Opracować plik Dockerfile…

![](./screenshoty/Aspose.Words.1d35b0d7-c9b0-4d8a-9bbe-6a9e4c5f230f.004.png)
Plik Dockerfile

**3. (max. 30%)** 
Należy podać polecenia niezbędne do: 

1. zbudowania opracowanego obrazu kontenera

**docker build -t pwcho\_zad1:tag -f Dockerfile .**

Polecenie docker build buduje obraz na podstawie pliku Dockerfile znajdującego się w bieżącym katalogu

![](./screenshoty/Aspose.Words.1d35b0d7-c9b0-4d8a-9bbe-6a9e4c5f230f.005.png)

1. uruchomienia kontenera na podstawie zbudowanego obrazu, 

**docker run -p 8080:8080 pwcho\_zad1:tag**

8080 numer portu, na którym udostępniany jest kontener na hoście. 8080 numer portu, na którym serwer wewnątrz kontenera nasłuchuje. Polecenie docker run uruchamia kontener na podstawie określonego obrazu.


![](./screenshoty/Aspose.Words.1d35b0d7-c9b0-4d8a-9bbe-6a9e4c5f230f.006.png)


![](Aspose.Words.1d35b0d7-c9b0-4d8a-9bbe-6a9e4c5f230f.007.png)

1. sposobu uzyskania informacji, które wygenerował serwer w trakcie uruchamiana kontenera (patrz: punkt 1a), 

Można uzyskać informacje generowane przez serwer w trakcie uruchamiania kontenera, przekierowując logi kontenera na standardowe wyjście. Można to zrobić, dodając flagę -t (pseudo-TTY) i -i (interaktywność) do polecenia docker run

**docker run -t -i -p 8080:8080 pwcho\_zad1:tag**


Dzięki temu logi serwera będą widoczne na bieżąco w konsoli, w której uruchomiono kontener.

![](./screenshoty/Aspose.Words.1d35b0d7-c9b0-4d8a-9bbe-6a9e4c5f230f.008.png)


1. ` `sprawdzenia, ile warstw posiada zbudowany obraz.

Polecenie do sprawdzenia, ile warstw posiada zbudowany obraz:
**docker history pwcho\_zad1:tag


![](./screenshoty/Aspose.Words.1d35b0d7-c9b0-4d8a-9bbe-6a9e4c5f230f.009.png)**



**Repozytorium GitHub:** https://github.com/sebastianslupny4/pwcho\_zad1/

**Repozytorium DockerHub:** https://hub.docker.com/r/sebastianslupny/pwcho\_zad1
