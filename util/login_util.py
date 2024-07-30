import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

xpath = {
   "decline_cookies": "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]",
    "save_login_not_now_button": "//div[contains(text(), 'Ahora no')]",
    "notification_not_now_button": "//button[contains(text(), 'Ahora no')]",
    "followers":"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a",
    "followings":"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a"
}

def quitar_cookies(driver):
    try:
        cookie_warning = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, xpath["decline_cookies"]))
        )
        cookie_warning[0].click()
    except:
        pass

def iniciar_sesion(driver, username, password):
    try:
        # Encontrar el campo de usuario y contraseña
        username_field = driver.find_element(By.NAME, 'username')
        password_field = driver.find_element(By.NAME, 'password')
        # Introducir las credenciales
        username_field.send_keys(username)
        password_field.send_keys(password)
        # Enviar el formulario
        password_field.send_keys(Keys.RETURN)
        
        try:
            verification_field = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.NAME, 'verificationCode'))
            )            
            # Solicitar al usuario que ingrese el código de verificación
            verification_code = input("Pulsa intro cuando estes en la pantalla de inicio: ")
            if verification_code !=verification_field:
                pass
            time.sleep(2)
         
            
            # Esperar a que el inicio de sesión sea exitoso después de la verificación
            WebDriverWait(driver, 7).until(
                EC.visibility_of_element_located((By.XPATH, f"//a[contains(@href, '/{username}/')]"))
            )
            print("\nCódigo verificado.")
        except:
            # Si no se requiere el código de verificación o falla la espera, continuar
            WebDriverWait(driver, 7).until(
                EC.visibility_of_element_located((By.XPATH, f"//a[contains(@href, '/{username}/')]"))
            )
            pass
            
    except Exception as e:
        print("\nError al iniciar sesión:")
        driver.quit()
        exit()
    
def quitar_save_login_info(driver):
    try:
        # Click "Not now" and ignore Save-login info prompt
        save_login_prompt = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, xpath["save_login_not_now_button"]))
        )
        save_login_prompt.click()
    except:
        pass
    
def quitar_notificaciones(driver):
    try:
        # Click "not now" on notifications prompt
        notifications_prompt = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, xpath["notification_not_now_button"]))
        )
        notifications_prompt.click()
    except:
        pass