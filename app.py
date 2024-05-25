import streamlit as st

# Título e Descrição do APP
st.title("Divisão de Conta com Gorjeta")
st.write("Divida sua conta de maneira rápida e fácil!")

# Obtendo os Valores do Usuário com Sliders e Seleção:

conta = st.number_input("Valor da Conta (R$)", min_value=0.00, step=0.01)
gorjeta = st.selectbox("Porcentagem da Gorjeta", options=[0, 10, 12, 15])
pessoas = st.number_input("Quantas Pessoas?", min_value=1)

# Calcular e Mostrar o Resultado:

total = (conta * (1 + (gorjeta / 100))) / pessoas
st.write(f"Cada pessoa paga: R$ {total:.2f}")