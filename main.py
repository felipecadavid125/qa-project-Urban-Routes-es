import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

class SeleccionTarifaConfort:
    modo_personal = (By. CLASS_NAME, 'mode active')
    taxi = (By. CLASS_NAME, 'type active')
    reservar = (By. CLASS_NAME, 'buttom round')
    confort = (By. CLASS_NAME, 'tcard active')

    def __init__(self, driver):
        self.driver = driver

    def click_en_personal(self):
        self.driver.find_element(*self.modo_personal).click()

    def click_en_taxi(self):
        self.driver.find_element(*self.taxi).click()

    def click_en_reservar(self):
        self.driver.find_element(*self.reservar).click()

    def click_en_confort(self):
        self.driver.find_element(*self.confort).click()

class RellenarNumeroTelefono:
    numero_telefono = (By. ID, 'phone')
    boton_siguiente = (By. CLASS_NAME, 'button full')

    def __init__(self, driver):
        self.driver = driver

    def ingresar_telefono(self, telefono):
        self.driver.find_element(*self.numero_telefono).send_keys(telefono)

    def click_siguiente(self):
        self.driver.find_element(*self.boton_siguiente).click()

class Agregartarjeta:
    numero_tarjeta = (By.CLASS_NAME, 'card-number-imput')
    cvv = (By.CLASS_NAME, 'card-code')
    boton_agregar = (By. CLASS_NAME, 'button full')


    def __init__(self, driver):
        self.driver = driver

    def agregar_tarjeta(self, tarjeta):
        self.driver.find_element(*self.numero_tarjeta).send_keys(tarjeta)

    def click_agregar(self):
        self.driver.find_element(*self.boton_agregar).click()

class MensajeConductor:
    mensaje = (By. CLASS_NAME, 'input-container')

    def __init__(self, driver):
        self.driver = driver

    def mensaje_conductor(self, mensaje):
        self.driver.find_element(*self.mensaje).send_keys(mensaje)

class MantaPanuelos:
    manta_panuelos = (By. CLASS_NAME, 'r-ws')

    def __init__(self, driver):
        self.driver = driver

    def switch_manta(self):
        self.driver.find_element(*self.manta_panuelos).click()

class Helados:
    helados_contador = (By.CLASS_NAME, 'counter-plus')

    def __init__(self, driver):
        self.driver = driver

    def aumenta_cantidad_helados(self):
        self.driver.find_element(*self.helados_contador).click()





class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_tarifa_confort(self):
        self.driver.get(data.urban_routes_url)
        tarifa_confort = SeleccionTarifaConfort(self.driver)
        tarifa_confort.click_en_confort()

    def test_numero_telefono(self):
        self.driver.get(data.urban_routes_url)
        llenar_numero_telefono = RellenarNumeroTelefono(self.driver)
        numero = data.phone_number
        llenar_numero_telefono.ingresar_telefono(numero)

    def test_agregar_tarjeta(self):
        self.driver.get(data.urban_routes_url)
        agregar_tarjeta = Agregartarjeta(self.driver)
        numero_tarjeta = data.card_number
        agregar_tarjeta.agregar_tarjeta(numero_tarjeta)

    def test_mensaje_conductor(self):
        self.driver.get(data.urban_routes_url)
        mensaje_para_conductor = MensajeConductor(self.driver)
        mensaje_para_el_conductor = data.message_for_driver
        mensaje_para_conductor.mensaje_conductor(mensaje_para_conductor)

    def test_manta_panuelos(self):
        self.driver.get(data.urban_routes_url)
        manta_panuelos = MantaPanuelos(self.driver)
        manta_panuelos.switch_manta()

    def test_helados(self):
        self.driver.get(data.urban_routes_url)
        helados = Helados(self.driver)
        helados.aumenta_cantidad_helados()





    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
