import streamlit as st

# Função matemática 
def calcular(num_1, num_2, operacao):
    if operacao == 'Adição': return num_1 + num_2
    elif operacao == 'Subtração': return num_1 - num_2
    elif operacao == 'Multiplicação': return num_1 * num_2
    elif operacao == 'Divisão':
        if num_2 != 0: return num_1 / num_2
        else: return "Erro: Divisão por zero não é permitida."

# === FUNÇÃO PARA LIMPAR OS CAMPOS ===
def limpar_campos():
    st.session_state["n1"] = 0.0
    st.session_state["n2"] = 0.0
    st.session_state["op"] = "Adição"

# --- VISUAL DA CALCULADORA ---

st.title("🧮 Calculadora Web")

with st.container(border=True):
    st.write("### Painel de Operações")
    
    col1, col2 = st.columns(2)
    with col1:
        # Adicionado o "key" para o Streamlit saber quem limpar
        num_1 = st.number_input("Primeiro número:", value=0.0, key="n1")
    with col2:
        num_2 = st.number_input("Segundo número:", value=0.0, key="n2")
    
    operacao = st.selectbox("Selecione a operação:", ["Adição", "Subtração", "Multiplicação", "Divisão"], key="op")
    
    # Criado duas colunas para os botões ficarem lado a lado
    btn_calc, btn_limpar = st.columns(2)
    
    with btn_calc:
        if st.button("Calcular"):
            resultado = calcular(num_1, num_2, operacao)
            st.success(f"O resultado é: {resultado}")
            
    with btn_limpar:
        # Quando o botão é clicado, ele chama a função que limpa a memória dos campos
        st.button("Limpar", on_click=limpar_campos)