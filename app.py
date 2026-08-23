# app.py
import streamlit as st
import json
import os
import math

# Configuração de Página
st.set_page_config(
    page_title="Guia Premium de Enfermagem & Concursos",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    .main-header {
        background: linear-gradient(135deg, #0e7490 0%, #0369a1 100%);
        color: white; padding: 24px; border-radius: 12px; margin-bottom: 24px;
    }
    .main-header h1 { color: white !important; margin: 0; font-size: 2rem; }
    .gift-card {
        background: #f0fdf4; border-left: 5px solid #16a34a; padding: 16px 20px;
        border-radius: 8px; margin-bottom: 24px;
    }
    .result-badge {
        background-color: #e0f2fe; color: #0369a1; padding: 14px;
        border-radius: 8px; font-size: 1.2rem; font-weight: bold; text-align: center;
    }
    .stat-box {
        background-color: white; border-radius: 8px; padding: 15px;
        border: 1px solid #e2e8f0; text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Importando banco de dados
try:
    from banco_dados import DADOS_ESTUDO, QUESTOES_PROVA
except ImportError:
    st.error("Erro ao carregar banco_dados.py. Verifique se o arquivo está na pasta.")
    st.stop()

# Header
st.markdown("""
<div class="main-header">
    <h1>🩺 Plataforma Avançada de Estudos de Enfermagem</h1>
    <p>Preparação de Alto Desempenho para Concursos e Prática Assistencial</p>
</div>
""", unsafe_allow_html=True)

# Menu
st.sidebar.title("📌 Menu de Navegação")
menu = st.sidebar.radio(
    "Escolha uma seção:",
    ["🧮 Calculadoras Clínicas", "📚 Módulos Teóricos", "🎴 Flashcards Interativos", "📝 Simulado de Provas"]
)

# -----------------------------------------------------------------------------
# 1. CALCULADORAS CLÍNICAS
# -----------------------------------------------------------------------------
if menu == "🧮 Calculadoras Clínicas":
    st.title("🧮 Calculadoras Clínicas e Preditivas")
    aba_calc = st.tabs([
        "💧 Gotejamento de Soro", "💉 Dosagem e Soluções", "📅 DPP & IG (Obstetrícia)",
        "🧠 Escala de Glasgow (ECG-P)", "📊 Escala de Braden (LPP)", "⚖️ IMC & Superfície Corporal"
    ])
    
    with aba_calc[0]:
        st.subheader("💧 Calculadora de Gotejamento")
        col1, col2 = st.columns(2)
        with col1:
            volume = st.number_input("Volume total (mL):", min_value=1.0, value=500.0)
            tempo_tipo = st.selectbox("Unidade de tempo:", ["Horas", "Minutos"])
            tempo_val = st.number_input(f"Tempo ({tempo_tipo}):", min_value=1.0, value=8.0)
            tipo_equipo = st.selectbox("Equipo:", ["Macrogotas (Gotas/min)", "Microgotas (mcgotas/min)"])
        with col2:
            if tempo_tipo == "Horas":
                gotas = volume / (tempo_val * 3) if tipo_equipo.startswith("Macrogotas") else volume / tempo_val
            else:
                gotas = (volume * 20) / tempo_val if tipo_equipo.startswith("Macrogotas") else (volume * 60) / tempo_val
            unidade = "gotas/minuto" if tipo_equipo.startswith("Macrogotas") else "microgotas/minuto"
            st.markdown(f'<div class="result-badge">{math.ceil(gotas)} {unidade}<br><small>Exato: {gotas:.2f}</small></div>', unsafe_allow_html=True)

    with aba_calc[1]:
        st.subheader("💉 Dosagem de Medicamentos")
        c1, c2 = st.columns(2)
        with c1:
            presc = st.number_input("Prescrição Médica (mg):", min_value=0.1, value=250.0)
            disp_mg = st.number_input("Apresentação Disponível (mg):", min_value=0.1, value=500.0)
            disp_ml = st.number_input("Volume do Diluente (mL):", min_value=0.1, value=5.0)
        with c2:
            vol = (presc * disp_ml) / disp_mg
            st.markdown(f'<div class="result-badge">Aspirar: {vol:.2f} mL</div>', unsafe_allow_html=True)

    with aba_calc[2]:
        st.subheader("📅 Data Provável do Parto (DPP) & Idade Gestacional")
        import datetime
        dum = st.date_input("DUM (1º dia da última menstruação):", value=datetime.date.today())
        if dum:
            dia, mes, ano = dum.day + 7, dum.month, dum.year
            if mes in [1, 2, 3]: mes += 9
            else: mes -= 3; ano += 1
            try: dpp = datetime.date(ano, mes, dia)
            except: dpp = datetime.date(ano, mes, 1) + datetime.timedelta(days=(dia - 1))
            
            dias_g = (datetime.date.today() - dum).days
            st.markdown(f'<div class="result-badge">DPP: {dpp.strftime("%d/%m/%Y")} | IG: {dias_g//7} Semanas e {dias_g%7} Dias</div>', unsafe_allow_html=True)

    with aba_calc[3]:
        st.subheader("🧠 Escala de Coma de Glasgow (ECG-P)")
        c1, c2 = st.columns(2)
        with c1:
            ao = st.selectbox("Abertura Ocular:", ["4 - Espontânea", "3 - Verbal", "2 - Pressão", "1 - Ausente", "NT"])
            rv = st.selectbox("Resposta Verbal:", ["5 - Orientado", "4 - Confuso", "3 - Inadequado", "2 - Sons", "1 - Ausente", "NT"])
            rm = st.selectbox("Resposta Motora:", ["6 - Obedece", "5 - Localiza", "4 - Flexão Normal", "3 - Decorticação", "2 - Descerebração", "1 - Ausente", "NT"])
            rp = st.selectbox("Reatividade Pupilar:", ["0 - Ambas reagem", "-1 - Uma reage", "-2 - Nenhuma reage"])
        with c2:
            def v(x): return 0 if "NT" in x else int(x.split()[0])
            total = v(ao) + v(rv) + v(rm) + int(rp.split()[0])
            st.markdown(f'<div class="result-badge">Pontuação Glasgow: {total}</div>', unsafe_allow_html=True)

    with aba_calc[4]:
        st.subheader("📊 Escala de Braden (LPP)")
        c1, c2 = st.columns(2)
        with c1:
            p1 = st.slider("Percepção Sensorial:", 1, 4, 3)
            p2 = st.slider("Umidade:", 1, 4, 3)
            p3 = st.slider("Atividade:", 1, 4, 2)
            p4 = st.slider("Mobilidade:", 1, 4, 3)
            p5 = st.slider("Nutrição:", 1, 4, 3)
            p6 = st.slider("Fricção/Cisalhamento:", 1, 3, 2)
        with c2:
            score = p1+p2+p3+p4+p5+p6
            st.markdown(f'<div class="result-badge">Escore Braden: {score}</div>', unsafe_allow_html=True)

    with aba_calc[5]:
        st.subheader("⚖️ IMC & Superfície Corporal")
        c1, c2 = st.columns(2)
        with c1:
            peso = st.number_input("Peso (kg):", min_value=1.0, value=70.0)
            altura = st.number_input("Altura (cm):", min_value=30.0, value=170.0)
        with c2:
            imc = peso / ((altura/100)**2)
            sc = math.sqrt((peso * altura) / 3600)
            st.markdown(f'<div class="result-badge">IMC: {imc:.2f} kg/m²<br>SC: {sc:.2f} m²</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. MÓDULOS TEÓRICOS
# -----------------------------------------------------------------------------
elif menu == "📚 Módulos Teóricos":
    st.title("📚 Módulos Teóricos")
    materia = st.selectbox("Selecione a Disciplina:", options=list(DADOS_ESTUDO.keys()), format_func=lambda x: DADOS_ESTUDO[x]["titulo"])
    st.text_area("Resumo Técnico:", value=DADOS_ESTUDO[materia]["resumo"], height=450)

# -----------------------------------------------------------------------------
# 3. FLASHCARDS
# -----------------------------------------------------------------------------
elif menu == "🎴 Flashcards Interativos":
    st.title("🎴 Flashcards de Memorização")
    materia = st.selectbox("Disciplina:", options=list(DADOS_ESTUDO.keys()), format_func=lambda x: DADOS_ESTUDO[x]["titulo"])
    for idx, (p, r) in enumerate(DADOS_ESTUDO[materia]["flashcards"], 1):
        with st.expander(f"❓ Card {idx}: {p}"):
            st.success(f"💡 {r}")

# -----------------------------------------------------------------------------
# 4. SIMULADO COM ESTATÍSTICA EM TEMPO REAL
# -----------------------------------------------------------------------------
elif menu == "📝 Simulado de Provas":
    st.title("📝 Simulado de Questões com Estatísticas")

    # Inicializar estado da sessão para histórico
    if 'historico_respostas' not in st.session_state:
        st.session_state.historico_respostas = {}

    total_questoes = len(QUESTOES_PROVA)

    # Painel Superior de Estatísticas
    respostas = st.session_state.historico_respostas
    respondidas = len(respostas)
    acertos = sum(1 for v in respostas.values() if v['correto'])
    erros = respondidas - acertos
    taxa_acerto = (acertos / respondidas * 100) if respondidas > 0 else 0.0

    st.markdown("### 📊 Painel Geral de Desempenho")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Questões Respondidas", f"{respondidas} / {total_questoes}")
    c2.metric("Acertos", acertos, delta=f"{acertos} certas")
    c3.metric("Erros", erros, delta=f"-{erros}" if erros > 0 else "0", delta_color="inverse")
    c4.metric("Aproveitamento", f"{taxa_acerto:.1f}%")

    st.progress(respondidas / total_questoes if total_questoes > 0 else 0)
    st.markdown("---")

    # Navegação entre questões
    q_idx = st.number_input("Ir para a Questão número:", min_value=1, max_value=total_questoes, value=1, step=1) - 1
    q = QUESTOES_PROVA[q_idx]

    st.markdown(f"#### Questão {q_idx + 1} de {total_questoes}")
    st.info(q["pergunta"])

    opcao_sel = st.radio("Selecione a alternativa:", q["opcoes"], key=f"q_{q_idx}")

    col_btn, col_reset = st.columns([3, 1])
    
    with col_btn:
        if st.button("Confirmar Resposta", type="primary"):
            idx_sel = q["opcoes"].index(opcao_sel)
            is_correct = (idx_sel == q["correta"])
            
            # Salva na sessão
            st.session_state.historico_respostas[q_idx] = {
                'opcao': idx_sel,
                'correto': is_correct
            }
            st.rerun()

    with col_reset:
        if st.button("Reiniciar Simulado"):
            st.session_state.historico_respostas = {}
            st.rerun()

    # Feedback da questão atual se já respondida
    if q_idx in st.session_state.historico_respostas:
        dado = st.session_state.historico_respostas[q_idx]
        if dado['correto']:
            st.success("🎉 Você acertou esta questão!")
        else:
            st.error(f"❌ Você errou. A alternativa correta era: **{q['opcoes'][q['correta']]}**")
        
        st.markdown(f"**🔍 Comentário:** {q['explicacao']}")