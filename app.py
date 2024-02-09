from src.Dni import Dni

def main():
    inputDni = input('\nWrite the Dni to checkit: ')
    dni_user = Dni(inputDni)

    if dni_user.checkDni() is True:
        print(f"""The DNI "{inputDni}" is valid""")
    else:
        print(f"""The DNI "{inputDni}" is'nt valid""")

if __name__ == "__main__":
    main()
