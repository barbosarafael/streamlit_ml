import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image



st.set_page_config(
        page_title = "Dashboard",
        page_icon = "chart_with_upwards_trend",
        layout = "wide"
    )

# Sidebar


page = st.sidebar.selectbox("Escolha uma página:", ['Considerações iniciais', 'Big Numbers', 'Indicadores a nível Seller', \
    'Indicadores a nível Customer', 'Indicadores a nível Order'])

st.sidebar.markdown('---')

st.sidebar.markdown('Criado com ❤️ por Rafael Barbosa')

st.sidebar.markdown("""

Github: [barbosarafael](https://github.com/barbosarafael)

LinkedIn: [Rafael Barbosa](https://www.linkedin.com/in/rafael-barbosa0/)

""")


@st.cache(show_spinner=False)

def load_data_order():

    data_order = pd.read_csv("raw_data/olist_orders_dataset.csv")

    return data_order

@st.cache(show_spinner=False)

def load_data_customers():

    data_order_customer = pd.read_csv("raw_data/olist_customers_dataset.csv")

    return data_order_customer  

def load_data_geolocation():

    data_geolocation = pd.read_csv("raw_data/olist_geolocation_dataset.csv")

    return data_geolocation    

def load_data_order():

    data_order = pd.read_csv("raw_data/olist_orders_dataset.csv")

    return data_order    

def load_data_order():

    data_order = pd.read_csv("raw_data/olist_orders_dataset.csv")

    return data_order    

def load_data_order():

    data_order = pd.read_csv("raw_data/olist_orders_dataset.csv")

    return data_order    

def load_data_order():

    data_order = pd.read_csv("raw_data/olist_orders_dataset.csv")

    return data_order    

def load_data_order():

    data_order = pd.read_csv("raw_data/olist_orders_dataset.csv")

    return data_order                
    



if page == 'Considerações iniciais':

    st.markdown("## 📈 Sobre os dados")

    st.markdown("""
    Os dados desse dashboard/relatório é relacionado à e-commerce disponibilizados pela [Olist Store](https://olist.com/pt-br/)\
    e contém informaçõe de 100k transações de 2016 a 2018, de diversos marketplaces no Brasil.
    

    Nos dados temos informações dos pedidos, sejam eles status, preço do pedido, tipo de pagamento e etc. Os dados \
    são anonimizados, então vossas pessoas nunca conseguirão saber qual transação está relacionada ao verdadeiro comprador, por exemplo.\


    Algumas considerações:

    - Assim que o cliente recebe o produto, ele recebe uma pesquisa de satisfação
    - Um pedido pode ter vários itens
    - Cada item pode ser faturado por atendido por um seller diferente
    - Todos os sellers são identificados como casas do Game of Thrones


    Segundo os autores do dataset temos várias opções tratar nos dados: 

    - NLP
    - Clusterização
    - Previsão de vendas
    - Desempenho na entrega
    - Qualidade produto 

    Se você quiser saber um pouco mais sobre a modelagem lógica das tabelas disponíveis, clique no botão abaixo

    """)


    modelagem_logica = st.button('Clique aqui para mostrar a modelagem lógica das tabelas 👈')


    if modelagem_logica: 

        imagem_modelagem_logica = Image.open('images/logical_model.png')

        st.image(imagem_modelagem_logica, caption = 'Modelagem lógica das tabelas')



elif page == "Big Numbers":


    st.header("Em construção")

    total_order_id = data1['order_id'].drop_duplicates().shape[0]
    total_customer_id = data1['customer_id'].drop_duplicates().shape[0]

    col1, col2 = st.columns(2)
    col1.metric(label = "Total de pedidos", value = total_order_id, delta="1.2 °F")
    col2.metric(label = "Total de customers", value = total_customer_id, delta = "-8%")


elif page == "Indicadores a nível Seller":

    st.header("Em construção")

elif page == "Indicadores a nível Customer":

    st.header("Em construção")

elif page == "Indicadores a nível Order":

    st.header("Em construção")