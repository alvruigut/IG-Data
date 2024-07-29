import os
import time
from datetime import datetime
from selenium import webdriver
from util import save_data
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MainFirefox:
    def __init__(self, driver_path, username, password):
        self.driver_path = driver_path
        self.username = username
        self.password = password

        self.url = "https://www.instagram.com"

        # Configuración del servicio de GeckoDriver
        self.service = Service(executable_path=self.driver_path)

        # Configuración de las opciones de Firefox
        self.web_options = Options()
        self.web_options.add_argument("--headless")  # Ejecutar en modo headless (sin interfaz gráfica)

        # Inicializar el navegador
        #self.driver = webdriver.Firefox(service=self.service, options=self.web_options)
        self.driver = webdriver.Firefox(service=self.service)
        
    def start(self):
        try:
            time.sleep(3)
            self.driver.get(self.url)
            print("\nNavegador iniciado.")
            time.sleep(3)
        except Exception as e:
            print("Error al iniciar el navegador:", e)
            self.driver.quit()
            exit()

    def login(self):
        try:
            # Encontrar el campo de usuario y contraseña
            username_field = self.driver.find_element(By.NAME, 'username')
            password_field = self.driver.find_element(By.NAME, 'password')

            # Introducir las credenciales
            username_field.send_keys(self.username)
            password_field.send_keys(self.password)

            # Enviar el formulario
            password_field.send_keys(Keys.RETURN)
            
            # Esperar a que el enlace del perfil sea visible para confirmar el inicio de sesión
            WebDriverWait(self.driver, 7).until(
                EC.visibility_of_element_located((By.XPATH, f"//a[contains(@href, '/{self.username}/')]"))
            )
            print("\nInicio de sesión exitoso.")
        except Exception as e:
            print("\nError al iniciar sesión.\n")
            self.driver.quit()
            exit()

 

    def navigate_to_profile(self):
        try:
            profile_url = f'https://www.instagram.com/{self.username}/'
            self.driver.get(profile_url)
            print("\nPerfil cargado.")
            time.sleep(5)
        except Exception as e:
            print("Error al navegar al perfil:", e)
            self.driver.quit()
            exit()

    def click_followers_link(self):
        try:
            followers_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "seguidores")
            followers_link.click()
            print("\nCargando lista de seguidores...")
            time.sleep(5)
        except Exception as e:
            print("Error al hacer clic en el enlace de seguidores:", e)
            self.driver.quit()
            exit()

    def click_followings_link(self):
        try:
            followings_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "seguidos")
            followings_link.click()
            print("\nCargando lista de seguidos...")
            time.sleep(5)
        except Exception as e:
            print("Error al hacer clic en el enlace de seguidos:", e)
            self.driver.quit()
            exit()

    def scroll_list(self):
        try:
            # Localizar el contenedor de seguidores usando la clase proporcionada
            modal = self.driver.find_element(By.CSS_SELECTOR, 'div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6')
            last_height = self.driver.execute_script("return arguments[0].scrollHeight", modal)
            print("\nLeyendo datos...\n")
            while True:
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                time.sleep(2)  # Esperar a que se cargue más contenido

                # Comprobar si el texto "Sugerencias para ti" está presente
                if "Sugerencias para ti" in self.driver.page_source:
                    break

                new_height = self.driver.execute_script("return arguments[0].scrollHeight", modal)
                if new_height == last_height:
                    break
                last_height = new_height

        except Exception as e:
            print("Error al desplazar la ventana:", e)
            self.driver.quit()
            exit()

    def save_followers_unfollows(self):
        data_dir = os.path.join(os.path.dirname(__file__), '../data', self.username)
        os.makedirs(data_dir, exist_ok=True)

        try:
            # Extraer el número de seguidores y los seguidores actuales
            num_followers = save_data.extract_number_of_followers(self.driver)
            spans = self.driver.find_elements(By.CSS_SELECTOR, 'span._ap3a._aaco._aacw._aacx._aad7._aade')
            current_followers = [follower.text for follower in spans[:num_followers]]

            # Ruta al archivo de la lista de seguidores
            followers_list_path = os.path.join(data_dir, 'followers_list.json')

            # Leer la lista de seguidores anterior
            previous_followers = save_data.read_previous_followers(followers_list_path)

            # Comparar listas y obtener nuevos seguidores y seguidores perdidos
            new_followers, lost_followers = save_data.compare_followers_lists(previous_followers, current_followers)

            # Verificar si hay cambios antes de escribir en los archivos
            if new_followers or lost_followers:
                # Guardar la lista actual si ha cambiado
                save_data.write_followers_list(followers_list_path, current_followers)

                # Crear archivo de registro con la fecha y hora
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                log_file_path = os.path.join(data_dir, f'followers_{timestamp}.txt')
                save_data.write_followers_log(log_file_path, current_followers)

                # Guardar usuarios que han dejado de seguir
                lost_followers_file_path = os.path.join(data_dir, 'lost_followers.txt')
                save_data.write_lost_followers(lost_followers_file_path, lost_followers)
            else:
                print("No hay cambios en la lista de seguidores.")

        except Exception as e:
            print("Error al extraer los seguidores:", e)
            self.driver.quit()
            exit()

    def save_followings(self):
        data_dir = os.path.join(os.path.dirname(__file__), '../data', self.username)
        os.makedirs(data_dir, exist_ok=True)

        try:
            # Extraer el número de seguidos y los seguidos actuales
            num_followings = save_data.extract_number_of_followings(self.driver)
            spans = self.driver.find_elements(By.CSS_SELECTOR, 'span._ap3a._aaco._aacw._aacx._aad7._aade')
            current_followings = [following.text for following in spans[:num_followings]]

            # Ruta al archivo de la lista de seguidos
            followings_list_path = os.path.join(data_dir, 'followings_list.json')

            # Leer la lista de seguidos anterior
            previous_followings = save_data.read_previous_followings(followings_list_path)

            # Verificar si hay cambios antes de escribir en los archivos
            if current_followings != previous_followings:
                # Guardar la lista actual si ha cambiado
                save_data.write_followings_list(followings_list_path, current_followings)

                # Crear archivo de registro con la fecha y hora
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                log_file_path = os.path.join(data_dir, f'followings_{timestamp}.txt')
                save_data.write_followings_log(log_file_path, current_followings)

            else:
                print("No hay cambios en la lista de seguidos.")

        except Exception as e:
            print("Error al extraer los seguidos:", e)
            self.driver.quit()
            exit()

    def compare_followers_and_followings(self):
        data_dir = os.path.join(os.path.dirname(__file__), '../data', self.username)
        os.makedirs(data_dir, exist_ok=True)

        try:
            # Rutas a los archivos de seguidores y seguidos
            followers_list_path = os.path.join(data_dir, 'followers_list.json')
            followings_list_path = os.path.join(data_dir, 'followings_list.json')

            # Leer las listas de seguidores y seguidos
            followers = save_data.read_previous_followers(followers_list_path)
            followings = save_data.read_previous_followings(followings_list_path)

            # Comparar listas para encontrar usuarios que sigues pero que no te siguen a ti
            not_following_back = list(set(followings) - set(followers))

            if not_following_back:
                not_following_back_file_path = os.path.join(data_dir, 'not_following_back.txt')
                save_data.write_not_following_back(not_following_back_file_path, not_following_back)
            else:
                print("Todos los usuarios a los que sigues también te siguen.")

        except Exception as e:
            print("Error al comparar seguidores y seguidos:", e)
            self.driver.quit()
            exit()
            

    def quit(self):
        self.driver.quit()
