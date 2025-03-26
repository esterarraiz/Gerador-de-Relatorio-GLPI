from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime


class GLPIBot:
    def __init__(self, usuario, senha, url="https://chamados.idxdatacenters.com.br"):
        self.usuario = usuario
        self.senha = senha
        self.url = url
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login_name"]')))
        self.driver.find_element(By.XPATH, '//*[@id="login_name"]').send_keys(self.usuario)
        self.driver.find_element(By.XPATH, '//*[@id="login_password"]').send_keys(self.senha)

        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "submit")))
        login_button.click()

        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )


    # Extrair chamados Sem Técnico
    def extrair_chamados(self):
        self.driver.get(self.url + "/front/ticket.php?is_deleted=0&as_map=0&browse=0&criteria%5B0%5D%5Blink%5D=AND&criteria%5B0%5D%5Bfield%5D=5&criteria%5B0%5D%5Bsearchtype%5D=equals&criteria%5B0%5D%5Bvalue%5D=0&criteria%5B2%5D%5Blink%5D=AND&criteria%5B2%5D%5Bfield%5D=65&criteria%5B2%5D%5Bsearchtype%5D=under&criteria%5B2%5D%5Bvalue%5D=4&itemtype=Ticket&start=0&_glpi_csrf_token=3bebc0d0d35df647fbfd44cd950356c3e60fde64683e7584ab46c6ccd310943a&sort%5B%5D=19&order%5B%5D=DESC")

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))

        dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="massformTicket"]/div/div[3]/div/span[1]/select'))
        )
        select = Select(dropdown)
        select.select_by_value("100")

        time.sleep(3)

        chamados = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, '//table[contains(@class, "search-results")]//tbody/tr'))
        )

        lista_chamados = []
        for chamado in chamados:
            numero = chamado.find_element(By.XPATH, './td[2]/span').text.strip().replace(" ", "")
            titulo = chamado.find_element(By.XPATH, './td[3]').text.strip()  
            status = chamado.find_element(By.XPATH, './td[5]').text.strip()
            requerente=chamado.find_element(By.XPATH, './td[9]').text.strip()
            observador = chamado.find_element(By.XPATH, './td[18]').text.strip()  
            categoria = chamado.find_element(By.XPATH, './td[11]').text.strip()  
            if numero.isdigit() and status != "Fechado" and requerente != "Hostmaster Registro BR":
                lista_chamados.append({"numero": numero, "titulo" :titulo, "status": status, "observador": observador, "categoria": categoria})


        return lista_chamados

    # Extrair chamados SLAs Excedentes
    def extrair_chamados1(self):
        self.driver.get(self.url + "/front/ticket.php?is_deleted=0&as_map=0&browse=0&criteria%5B0%5D%5Blink%5D=AND&criteria%5B0%5D%5Bfield%5D=82&criteria%5B0%5D%5Bsearchtype%5D=equals&criteria%5B0%5D%5Bvalue%5D=1&criteria%5B1%5D%5Blink%5D=AND&criteria%5B1%5D%5Bfield%5D=65&criteria%5B1%5D%5Bsearchtype%5D=under&criteria%5B1%5D%5Bvalue%5D=4&criteria%5B2%5D%5Blink%5D=AND&criteria%5B2%5D%5Bfield%5D=12&criteria%5B2%5D%5Bsearchtype%5D=equals&criteria%5B2%5D%5Bvalue%5D=notold&itemtype=Ticket&start=0&_glpi_csrf_token=590607aff4390bcad557688b41bbd0c42df502ce53591dc6a4524736141b3229&sort%5B%5D=19&order%5B%5D=DESC")

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))

        """dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="massformTicket"]/div/div[3]/div/span[1]/select'))
        )
        select = Select(dropdown)
        select.select_by_value("150")

        time.sleep(3)"""

        chamados = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, '//table[contains(@class, "search-results")]//tbody/tr'))
        )
            
        lista_chamados1 = []
        for chamado in chamados:
            numero = chamado.find_element(By.XPATH, './td[2]/span').text.strip().replace(" ", "")  
            titulo = chamado.find_element(By.XPATH, './td[3]').text.strip()  
            observador = chamado.find_element(By.XPATH, './td[19]').text.strip()  
            categoria = chamado.find_element(By.XPATH, './td[11]').text.strip()  
            if numero.isdigit():
                lista_chamados1.append({"numero": numero, "titulo" :titulo, "observador": observador, "categoria": categoria})

        return lista_chamados1
    
    # Extrair chamados SLAs que vencem hoje
    def extrair_chamados2(self):
        chamados1 = self.extrair_chamados1()
        numeros_chamados1 = {chamado["numero"] for chamado in chamados1}  
        self.driver.get(self.url + "/front/ticket.php?is_deleted=0&as_map=0&browse=0&criteria%5B0%5D%5Blink%5D=AND&criteria%5B0%5D%5Bfield%5D=18&criteria%5B0%5D%5Bsearchtype%5D=morethan&_select_criteria%5B0%5D%5Bvalue%5D=TODAY&criteria%5B0%5D%5Bvalue%5D=TODAY&criteria%5B1%5D%5Blink%5D=AND&criteria%5B1%5D%5Bfield%5D=12&criteria%5B1%5D%5Bsearchtype%5D=equals&criteria%5B1%5D%5Bvalue%5D=notold&criteria%5B2%5D%5Blink%5D=AND&criteria%5B2%5D%5Bfield%5D=65&criteria%5B2%5D%5Bsearchtype%5D=under&criteria%5B2%5D%5Bvalue%5D=4&itemtype=Ticket&start=0&_glpi_csrf_token=75b1c0150f62b3402bde740fff0af737ddcd74680ffc009ab68548ab746e150f&sort%5B%5D=19&order%5B%5D=DESC")

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))

        """dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="massformTicket"]/div/div[3]/div/span[1]/select'))
        )
        select = Select(dropdown)
        select.select_by_value("150")

        time.sleep(3)"""

        chamados = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, '//table[contains(@class, "search-results")]//tbody/tr'))
        )
            
        lista_chamados2 = []
        data_hoje = datetime.today().date()

        """for chamado in chamados:
            numero = chamado.find_element(By.XPATH, './td[2]/span').text.strip().replace(" ", "")  
            if numero not in numeros_chamados1 and numero.isdigit():
                titulo = chamado.find_element(By.XPATH, './td[3]').text.strip()  
                observador = chamado.find_element(By.XPATH, './td[18]').text.strip()  
                categoria = chamado.find_element(By.XPATH, './td[11]').text.strip()  
                tempo_solucao = chamado.find_element(By.XPATH, './td[16]').text.strip().replace("-", "/")
                lista_chamados2.append({"numero": numero, "titulo": titulo, "observador": observador, "categoria": categoria})

        self.driver.quit()
        return lista_chamados2"""

        for chamado in chamados:
            numero = chamado.find_element(By.XPATH, './td[2]/span').text.strip().replace(" ", "")
            if numero not in numeros_chamados1 and numero.isdigit():
                titulo = chamado.find_element(By.XPATH, './td[3]').text.strip()
                status = chamado.find_element(By.XPATH, './td[5]').text.strip()
                observador = chamado.find_element(By.XPATH, './td[18]').text.strip()
                categoria = chamado.find_element(By.XPATH, './td[11]').text.strip()
                tempo_solucao = chamado.find_element(By.XPATH, './td[17]').text.strip().replace("-", "/")

                try:
                    data_solucao = datetime.strptime(tempo_solucao.split()[0], "%d/%m/%Y").date()

                    if data_solucao == data_hoje and status != "Pendente" and numero not in numeros_chamados1:
                        lista_chamados2.append({
                            "numero": numero,
                            "titulo": titulo,
                            "observador": observador,
                            "categoria": categoria
                        })
                except ValueError:
                    print(f"Erro ao converter a data: {tempo_solucao}")

        self.driver.quit()
        return lista_chamados2
    
