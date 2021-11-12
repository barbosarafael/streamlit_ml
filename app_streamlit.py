import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(
        page_title = "Hello world",
        page_icon = "chart_with_upwards_trend",
        layout="wide"
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

elif page == "Indicadores a nível Seller":

    st.header("Em construção")

elif page == "Indicadores a nível Customer":

    st.header("Em construção")

elif page == "Indicadores a nível Order":

    st.header("Em construção")


# @st.cache
# def load_data_order():

#     data_order = pd.read_csv("raw_data/olist_orders_dataset.csv")

#     data_order_item = pd.read_csv("raw_data/olist_order_items_dataset.csv")

#     data = data_order.merge(data_order_item, on = 'order_id', how = 'left')

#     return data


# data1 = load_data_order()    

# st.dataframe(data1.head())



