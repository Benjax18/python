import os
import time

for hora in range(24):
    for minuto in range(60):
        for segundos in range(60):
            print(f"{hora:02}:{minuto:02}:{segundos:02}")
            time.sleep(0.000000000000000002)
            os.system("cls")
