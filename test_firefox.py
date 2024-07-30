import getpass
import os
from src.extract_data import ExtractData
from src.main_firefox import MainFirefox

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(current_dir, 'gecko\geckodriver.exe')
    
    while True:

        print("\nOpciones:\n")
        print("\t1. Guardar datos de seguidores y seguidos de tu cuenta")
        print("\t2. Guardar datos de seguidores y seguidos de otro usuario")
        print("\t3. Ver quiénes te han dejado de seguir")
        print("\t4. Comparar quiénes no te siguen de los que tú sigues")
        print("\t0. Salir")

        option = input("\nSeleccione una opción: ")

        if option == "1":
            username = input("\nUsuario: ")
            password =  getpass.getpass(prompt='Contraseña: ')

            app = MainFirefox(driver_path, username, password)
            app.start()
            app.login()
            app.navigate_to_profile(username)
            app.click_followers_link()
            app.scroll_followers()
            app.save_followers_unfollows(username)
            app.navigate_to_profile(username)
            app.click_followings_link()
            app.scroll_followings()
            app.save_followings(username)
            
            app.compare_followers_and_followings(username)
            
            app.quit()
        
        elif option == "2":
            username = input("\nUsuario: ")
            password =  getpass.getpass(prompt='Contraseña: ')
            usernameToSearch = input("\nUsuario a buscar: ")
            app = MainFirefox(driver_path, username, password)
            app.start()
            app.login()
            app.navigate_to_profile(usernameToSearch)
            app.click_followers_link()
            app.scroll_followers()
            app.save_followers_unfollows(usernameToSearch)
            app.navigate_to_profile(usernameToSearch)
            app.click_followings_link()
            app.scroll_followings()
            app.save_followings(usernameToSearch)
            
            app.compare_followers_and_followings(usernameToSearch)
            
            app.quit()

        elif option == "3":
            username = input("Usuario: ")
            file_path = f'data/{username}/lost_followers.txt'
            print("\nUsuarios que han dejado de seguirte:\n")           

            ExtractData.get_data(file_path)

        elif option == "4":
            username = input("Usuario: ")
            file_path = f'data/{username}/not_following_back.txt'
            print("\nUsuarios que no te siguen de vuelta:\n")           

            ExtractData.get_data(file_path)

            
        elif option == "0":
            print("\nSaliendo...\n")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.\n")
