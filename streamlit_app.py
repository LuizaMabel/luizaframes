import streamlit as st

st.title("Minha Página Interativa")
st.header("Bem-vindo ao meu primeiro app!")

nome = st.text_input("Qual é o seu nome?")
idade = st.number_input("Quantos anos você tem?", min_value=1, max_value=120)
cor = st.selectbox("Qual sua cor favorita?", ["Vermelho", "Verde", "Azul", "Amarelo"])

tecnologia = st.checkbox("Você gosta de tecnologia?")
nota_matematica = st.slider("Quanto você gosta de matemática?", 0, 10)

if st.button("Enviar"):
    st.write("Olá,", nome + "!")
    st.write("Você tem", idade, "anos.")
    st.write("Sua cor favorita é:", cor)
    
    if tecnologia:
        st.write("Que legal que você gosta de tecnologia!")
    else:
        st.write("Tudo bem se tecnologia não for sua praia.")
    
    st.write("Nota que você deu para matemática:", nota_matematica)

st.write("Obrigado por usar meu app.")
