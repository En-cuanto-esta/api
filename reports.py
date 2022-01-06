import resources

def all_resources():
    yadio = resources.resource_yadio_io()
    cambios_rya = resources.resource_cambios_rya()
    akb = resources.resource_akb_fintech()
    localbitcoins = resources.resource_localbitcoins()
    bcv = resources.resource_bcv()
    return {
        "yadio": yadio,
        "cambiosRya": cambios_rya,
        "akb": akb,
        "localbitcoins": localbitcoins,
        "bcv": bcv,
        "promedio": (yadio + remove_unit_string(cambios_rya) + remove_unit_string(akb) + remove_unit_string(localbitcoins) + remove_unit_string(bcv)) / 5
    }

def remove_unit_string(text):
    characters = ' BS/USD'
    without_unit = ''.join( x for x in text if x not in characters)
    return float(without_unit.replace(',', '.'))