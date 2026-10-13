import time

def ciclo():
    cnt = 0
    print(f"iniciando ciclo...")
    while True:
        try:
         print(f"{cnt}: Ciclo en ejecución...")
         cnt += 1
         time.sleep(1)
        except KeyboardInterrupt:
            print(f"{cnt}: Ciclo interrumpido por el usuario.")
            break

if __name__ == "__main__":
    ciclo()
    