import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Conversor de Moedas",
    page_icon="💱",
    layout="centered"
)

# CSS personalizado
st.markdown("""
    <style>
        .main {
            background-color: #0f172a;
        }

        .titulo {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            color: white;
            margin-bottom: 10px;
        }

        .subtitulo {
            text-align: center;
            color: #94a3b8;
            margin-bottom: 40px;
        }

        .resultado {
            background-color: #1e293b;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            font-size: 28px;
            color: #38bdf8;
            margin-top: 25px;
            border: 1px solid #334155;
        }

        .stButton>button {
            width: 100%;
            height: 50px;
            font-size: 18px;
            border-radius: 12px;
            background-color: #2563eb;
            color: white;
            border: none;
        }

        .stButton>button:hover {
            background-color: #1d4ed8;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Taxas de conversão
taxas = {
    "Dólar 🇺🇸": 5.20,
    "Euro 🇪🇺": 5.70,
    "Libra 🇬🇧": 6.60,
    "Iene 🇯🇵": 0.035
}

# Título
st.markdown('<div class="titulo">💱 Conversor de Moedas</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitulo">Converta valores em reais para moedas internacionais</div>',
    unsafe_allow_html=True
)

# Entrada de valor
valor = st.number_input(
    "Digite o valor em reais (BRL)",
    min_value=0.0,
    format="%.2f"
)

# Seleção da moeda
moeda = st.selectbox(
    "Escolha a moeda de destino",
    list(taxas.keys())
)

# Conversão
if st.button("Converter"):
    taxa = taxas[moeda]
    resultado = valor / taxa

    st.markdown(
        f"""
        <div class="resultado">
            R$ {valor:.2f} <br><br>
            = <br><br>
            {resultado:.2f} {moeda}
        </div>
        """,
        unsafe_allow_html=True
    )