import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def split1000(s, sep=','):
    
   return s if len(s) <= 3 else split1000(s[:-3], sep) + sep + s[-3:]


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
    

    @st.cache(show_spinner=False)
    def load_data():
            
        load_order = pd.read_csv("raw_data/olist_orders_dataset.csv")

        load_order_item = pd.read_csv("raw_data/olist_order_items_dataset.csv")

        load_payment = pd.read_csv("raw_data/olist_order_payments_dataset.csv")

        load_customer = pd.read_csv("raw_data/olist_customers_dataset.csv")

        load_product = pd.read_csv("raw_data/olist_products_dataset.csv")

        load_sellers = pd.read_csv("raw_data/olist_sellers_dataset.csv")

        load_geolocation = pd.read_csv("raw_data/olist_geolocation_dataset.csv")

        load_order_reviews = pd.read_csv("raw_data/olist_order_reviews_dataset.csv")
        
        load_data_translate = pd.read_csv("raw_data/product_category_name_translation.csv")
        
        
        return load_order, load_order_item, load_payment, load_customer, load_product, load_sellers, load_geolocation, load_order_reviews, load_data_translate
    
    placeholder = st.empty()
    
    placeholder.info("Estamos carregando seus dados")  
        
    order, order_item, order_payments, customer, product, sellers, geolocation, order_reviews, translation = load_data()
    
    
    placeholder.success("Dados carregados")
    
    st.balloons()
    
    time.sleep(2)

    
    placeholder.empty()
    
    
    total_order_id = order['order_id'].drop_duplicates().shape[0]
    total_customer_id = customer['customer_id'].drop_duplicates().shape[0]
    total_seller_id = sellers['seller_id'].drop_duplicates().shape[0]

    col1, col2, col3 = st.columns(3)
    col1.metric(label = "Total de pedidos", value = split1000(str(total_order_id), sep = '.'), delta="1.2 °F")
    col2.metric(label = "Total de customers", value = split1000(str(total_customer_id), sep = '.'), delta = "-8%")
    col3.metric(label = "Total de sellers", value = split1000(str(total_seller_id), sep = '.'), delta = "-8%")


elif page == "Indicadores a nível Seller":

    st.header("Em construção")

elif page == "Indicadores a nível Customer":

    st.header("Em construção")

elif page == "Indicadores a nível Order":

    st.header("Em construção")