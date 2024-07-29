import getpass
import os
from src.extract_data import ExtractData
from src.main_firefox import MainFirefox

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(current_dir, 'gecko\geckodriver.exe')
    username = input("\nUsuario: ")
    while True:

        print("\nOpciones:\n")
        print("\t1. Guardar datos de seguidores y seguidos")
        print("\t2. Ver quiénes te han dejado de seguir")
        print("\t3. Comparar quiénes no te siguen de los que tú sigues")
        print("\t0. Salir")

        option = input("\nSeleccione una opción: ")

        if option == "1":
            print(f'\nUsuario: {username}')
            password =  getpass.getpass(prompt='Contraseña: ')

            app = MainFirefox(driver_path, username, password)
            app.start()
            app.login()
            app.navigate_to_profile()
            app.click_followers_link()
            app.scroll_list()
            app.save_followers_unfollows()
            app.navigate_to_profile()
            app.click_followings_link()
            app.scroll_list()
            app.save_followings()
            
            app.compare_followers_and_followings()
            
            app.quit()

        elif option == "2":
            #username = input("Usuario: ")
            file_path = f'data/{username}/lost_followers.txt'
            print("\nUsuarios que han dejado de seguirte:\n")           

            ExtractData.get_data(file_path)

        elif option == "3":
            #username = input("Usuario: ")
            file_path = f'data/{username}/not_following_back.txt'
            print("\nUsuarios que no te siguen de vuelta:\n")           

            ExtractData.get_data(file_path)

            
        elif option == "0":
            print("\nSaliendo...\n")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.\n")
