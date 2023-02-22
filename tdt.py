import streamlit as st
import requests
import json

# URL con la lista de canales
URL = "https://www.tdtchannels.com/lists/tv.json"

@st.cache_data
def obtener_datos(URL):
    res = requests.get(URL)
    data = res.json()
    return data


data = obtener_datos(URL)
#guardar json 
# with open('tdt.json', 'w') as f:
#     json.dump(data, f)


def get_countries(data):
    return [c['name'] for c in data['countries']]

def get_ambitos(data, country):
    pais = [a['name'] for a in data['countries'] if a['name'] == country][0]
    return [a['name'] for a in pais['ambits']]

def get_url(options):
    if options:
        return options[0]['url']
    else:
        return ''

def get_canales(data, country, ambito):
    pais = [a for a in data['countries'] if a['name'] == country][0]
    ambito = [a for a in pais['ambits'] if a['name'] == ambito][0]
    #devolver lista de: nombre, url y logo
    options = ambito['channels']
    return [{'name: ': c['name'], 
            'url': get_url(c['options']), 
            'logo': c['logo']} for c in ambito['channels']]


st.title("Aplicación canales TDT")
countries = get_countries(data)
zona = st.radio('Selecciona Zona', countries)
ambitos = get_ambitos(data, zona)
ambito = st.selectbox('Selecciona Ambito', ambitos)
# st.write(get_canales(data, zona, ambito))
canales = get_canales(data, zona, ambito)
for c in canales:
    nombre_url = f'[{c["name"]}]({c["url"]})'
    imagen = f'![{c["name"]}]({c["logo"]})'
    st.markdown(f'[{imagen}]({c["url"]})')
    # st.image(c['logo'], width=100)

## TODO
# - [ ] ver imagenes en columnas

