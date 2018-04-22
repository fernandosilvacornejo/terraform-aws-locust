from locust import HttpLocust, TaskSet
import random


CATEGORIES = [
    'electro',
    'tecnologia',
    'linea-blanca',
    'dormitorio',
    'muebles',
    'decohogar',
    'moda',
    'belleza',
    'top-calzado',
    'deportes',
    'ninos',
    'jugueteria'
]

ELECTRO_FILTERS = [
    'Audio',
    'HIFI',
    'Herramientas',
    'Drones'
]

PRODUCTS = [
    'drone-dji-spark-blanco-670824-PPP-?electro=Electro',
    'macbook-air-intel-core-i5-8gb-ram-128gb-13-3-237653-PPP-?tecnologia=Tecnolog%C3%ADa',
    'microondas-somela-fancy-wt1700-17-litros-582920-PPP-?linea-blanca=L%C3%ADnea%20Blanca',
    'divan-cama-ortopedic-black-1-5-plazas-set-attimo-cic-118105-ppp-?dormitorio=Dormitorio',
    'estuche-cuchilleria-74-piezas-attimo-753863-ppp-?decohogar=Deco',
    'smartwatch-vivoactive-hr-garmin-975282-PPP-?moda=Moda',
    'zapatilla-nike-revolution-3-running-hombre-641340-PPP-?top-calzado=Zapatos',
    'bicicleta-spinning-beat-30-muvo-121072-ppp-?deportes=Deportes',
    'silla-de-auto-butaca-7273-bebesit-7273-rojo-412659-PPP-?ninos=Ni%C3%B1os',
    'resbalin-columpio-3-en-1-talbot-571900-PPP-?jugueteria=Juguetes',
    'mesa-de-comedor-joyce-4-personas-attimo-620926-PPP-?muebles=Muebles&muebles-comedor=Comedor' +
    '&muebles-comedor-mesas-comedor=Mesas%20de%20Comedor',
    'depiladora-philips-lumea-essential-bri863-ipl-200-000-pulsaciones-993865-PPP-?' +
    'linea-blanca=L%C3%ADnea%20Blanca&belleza-cuidado-personal=Cuidado%20Personal' +
    '&belleza-cuidado-personal-depiladoras=Depiladoras'
]


def index(l):
    """Home page."""
    l.client.get("/")


def categories(l):
    """Random categories page."""
    category_url = "/categoria/{}".format(random.choice(CATEGORIES))
    l.client.get(category_url)


def electro_filters(l):
    """Random filter for the Electronics categories."""
    filter_url = "/categoria/electro?cat_2.raw=Electro/{}".format(
        random.choice(ELECTRO_FILTERS))
    l.client.get(filter_url)


def products(l):
    """Random categories page."""
    product_url = "/producto/{}".format(random.choice(PRODUCTS))
    l.client.get(product_url)


class UserBehavior(TaskSet):
    tasks = {index: 1,
             categories: 2,
             electro_filters: 2,
             products: 10}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
