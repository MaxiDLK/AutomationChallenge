from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome('/drivers/chromedriver.exe')
driver.maximize_window()

def ingresar(web):
    driver.get(web)
    time.sleep(1) 

def abrir_barra_busqueda():
    button = driver.find_element(By.CSS_SELECTOR, "#menu-principal > li.search-toggle-li > a")
    time.sleep(2)
    button.click()
    time.sleep(2)

def ingresar_busqueda(busqueda):
    search_bar = driver.find_element(By.NAME, "s")
    search_bar.send_keys(busqueda + Keys.ENTER)

def Checkear_url(url):
    assert url == driver.current_url
    print("se ingreso correctamente")

def cant_elementos():
    elementos = driver.find_elements(By.TAG_NAME, "article")
    print("Cantidad de articulos " + str(len(elementos)))

def clickear_resultado():
    pag = driver.find_element(By.CSS_SELECTOR,"#content > div > ul > li:nth-child(2) > a")
    pag.click()
    elemento = driver.find_element(By.CSS_SELECTOR, "#main #content article:nth-child(4) h2 a")
    elemento.click()

def seleccionar_nav():
    accion = ActionChains(driver)
    m = driver.find_element(By.CSS_SELECTOR, ".menu-item-107 a")
    accion.move_to_element(m).perform()
    m = driver.find_element(By.CSS_SELECTOR, ".menu-item-108 a")
    m.click()

def mover_a_footer():
    footer = driver.find_element(By.ID, "footer")
    actions = ActionChains(driver)
    actions.move_to_element(footer).perform()
    assert footer.is_displayed()

def validar_enviar():
    boton = driver.find_element(By.CSS_SELECTOR, "input[type=submit]")
    assert boton.is_enabled()
    print("Boton enviar habilitado")

def buscar_palabra(palabra):
    assert driver.page_source.__contains__(palabra)
    print("Palabra encontrada")


#Ingresa a la web
ingresar('https://www.samsistemas.com.ar')

#Abre la barra de busqueda y ingresa la busqueda
abrir_barra_busqueda()
ingresar_busqueda("devops")

#Chequea el url
Checkear_url("https://www.samsistemas.com.ar/?s=devops")

#Devuelve la cantidad de resultados
cant_elementos()

#Clickea en un resultado
clickear_resultado()

#Chequea el url
Checkear_url("https://www.samsistemas.com.ar/servicios-devops/automatizacion-de-pruebas/")

#Busca una palabra
buscar_palabra("Test Management")

#Selecciona una opcion del nav
seleccionar_nav()

#valida que el boton de enviar este habilitado
validar_enviar()

#Se mueve al footer y valida si es visible
mover_a_footer()

driver.quit()
