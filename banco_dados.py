# banco_dados.py

DADOS_ESTUDO = {
    "anatomia_humana": {
        "titulo": "🦴 Anatomia e Fisiologia Humana",
        "resumo": """🦴 RESUMO TÉCNICO COMPLETO: ANATOMIA E FISIOLOGIA HUMANA

1. SISTEMA CARDIOVASCULAR:
• Pequena Circulação (Pulmonar): Ventrículo Direito -> Artéria Pulmonar -> Pulmões (Hematose) -> Veias Pulmonares -> Átrio Esquerdo.
• Grande Circulação (Sistêmica): Ventrículo Esquerdo -> Artéria Aorta -> Órgãos/Tecidos -> Veias Cavas -> Átrio Direito.
• Válvulas Cardíacas: Tricúspide (direita) e Mitral/Bicúspide (esquerda); Semilunares (Aórtica e Pulmonar).

2. SISTEMA RESPIRATÓRIO:
• Porção Condutora: Fossas nasais, Faringe, Laringe, Traqueia, Brônquios e Bronquíolos.
• Porção Respiratória: Bronquíolos respiratórios e Alvéolos (local da hematose por difusão passiva).

3. SISTEMA NERVOSO:
• SNC: Encéfalo e Medula Espinhal. | SNP: 12 pares de nervos cranianos e 31 espinhais.
• Simpático (Luta/Fuga - Adrenalina) vs Parassimpático (Repouso/Digestão - Acetilcolina/Nervo Vago).

4. SISTEMA RENAL E DIGESTÓRIO:
• Néfron: Unidade funcional renal (Filtração, Reabsorção e Secreção).
• TGI: Boca -> Esôfago -> Estômago -> Intestino Delgado (Duodeno, Jejuno, Íleo) -> Intestino Grosso (Ceco, Cólon, Reto).""",
        "flashcards": [
            ("Qual o trajeto da pequena circulação (pulmonar)?", "Ventrículo Direito -> Artérias Pulmonares -> Pulmões -> Veias Pulmonares -> Átrio Esquerdo."),
            ("Quais são as válvulas atrioventriculares do coração?", "Tricúspide (lado direito) e Mitral/Bicúspide (lado esquerdo)."),
            ("Onde ocorre a hematose (troca gasosa)?", "Nos alvéolos pulmonares por difusão passiva."),
            ("Qual é a unidade funcional do rim responsável pela filtração?", "O Néfron.")
        ]
    },
    "citologia_histologia": {
        "titulo": "🔬 Citologia e Histologia Humana",
        "resumo": """🔬 RESUMO TÉCNICO COMPLETO: CITOLOGIA E HISTOLOGIA HUMANA

1. CITOLOGIA (BIOLOGIA CELULAR):
• Membrana Plasmática: Mosaico fluido, transporte passivo (sem ATP) e ativo (Bomba Na+/K+ ATPase - 3 Na+ saem, 2 K+ entram).
• Organelas: RER (proteínas de exportação), REL (lipídeos e desintoxicação), Golgi (secreção e empacotamento), Lisossomos (digestão celular), Mitocôndrias (respiração aeróbica).

2. HISTOLOGIA HUMANA:
• Tecido Epitelial: Avascular (nutrido pelo tecido conjuntivo via lâmina basal).
• Tecido Conjuntivo: Vascularizado. Células: Fibroblastos, Macrófagos e Plasmócitos (produção de anticorpos).
• Tecido Nervoso: Neurônios e Glia (Oligodendrócitos formam bainha de mielina no SNC; Células de Schwann no SNP).""",
        "flashcards": [
            ("Qual organela é responsável pela síntese de lipídeos e desintoxicação celular?", "Retículo Endoplasmático Liso (REL)."),
            ("Qual a função da Bomba de Na+/K+ ATPase?", "Transporte ativo que expulsa 3 Na+ e coloca 2 K+ na célula com gasto de ATP."),
            ("Qual célula do tecido conjuntivo produz anticorpos?", "Plasmócitos (derivados dos linfócitos B)."),
            ("Quais células produzem a Bainha de Mielina no SNC e SNP?", "Oligodendrócitos no SNC e Células de Schwann no SNP.")
        ]
    },
    "bioquimica": {
        "titulo": "🧪 Bioquímica Humana e Clínica",
        "resumo": """🧪 RESUMO TÉCNICO COMPLETO: BIOQUÍMICA HUMANA

1. TAMPÕES BIOLÓGICOS:
• pH sanguíneo normal: 7,35 a 7,45. Principal tampão: Bicarbonato / Ácido Carbônico (HCO3- / H2CO3).

2. METABOLISMO DE CARBOIDRATOS E LIPÍDEOS:
• Glicogenogênese (Insulina) vs Glicogenólise (Glucagon e Adrenalina).
• Lipoproteínas: LDL (colesterol para tecidos) e HDL (transporte reverso de colesterol ao fígado).

3. BIOENERGÉTICA:
• Glicólise (Citoplasma), Ciclo de Krebs (Matriz Mitocondrial) e Cadeia Respiratória (Cristas Mitocondriais com O2 como aceptor final de elétrons).""",
        "flashcards": [
            ("Qual é o principal sistema tampão químico do plasma sanguíneo?", "Sistema Tampão Bicarbonato (HCO3- / H2CO3)."),
            ("Qual a função da lipoproteína HDL no organismo?", "Realiza o transporte reverso do colesterol, removendo o excesso dos vasos e levando ao fígado."),
            ("Onde ocorrem a Glicólise e o Ciclo de Krebs?", "Glicólise no Citoplasma; Ciclo de Krebs na Matriz Mitocondrial.")
        ]
    },
    "saude_coletiva": {
        "titulo": "🏛️ Saúde Coletiva e Legislação do SUS",
        "resumo": """🏛️ RESUMO TÉCNICO COMPLETO: SAÚDE COLETIVA E SUS

1. PRINCIPIOS DO SUS (LEI 8.080/1990):
• Doutrinários: Universalidade, Equidade e Integralidade.
• Organizativos: Descentralização, Regionalização, Hierarquização e Participação Social (Lei 8.142/1990).

2. PNAB E IMUNIZAÇÃO (PNI):
• Estratégia Saúde da Família (ESF) como porta de entrada.
• Vacinas ao nascer: BCG (Intradérmica no braço direito) e Hepatite B.
• Rede de Frio: Armazenamento mantido entre +2°C e +8°C.""",
        "flashcards": [
            ("Quais são os 3 princípios doutrinários do SUS?", "Universalidade, Equidade e Integralidade."),
            ("Quais vacinas o recém-nascido deve receber ao nascer?", "BCG (dose única) e Hepatite B (primeira dose)."),
            ("Qual a temperatura da Rede de Frio para conservação de vacinas?", "Entre +2°C e +8°C (ideal em +5°C).")
        ]
    },
    "fundamentos_enfermagem": {
        "titulo": "🩺 Fundamentos de Enfermagem & SAE",
        "resumo": """🩺 FUNDAMENTOS DE ENFERMAGEM E SISTEMATIZAÇÃO DA ASSISTÊNCIA (SAE)

1. PROCESSO DE ENFERMAGEM (RESOLUÇÃO COFEN 736/2024):
• 5 Etapas: 1. Avaliação; 2. Diagnóstico de Enfermagem; 3. Planejamento; 4. Implementação; 5. Evolução.

2. SINAIS VITAIS (SSVV):
• PA Normal: <= 120/80 mmHg.
• FC Eucárdico: 60-100 bpm | FR Eupneico: 12-20 irpm.
• Temperatura: Afebril (36,1°C - 37,2°C) | Febril (>= 37,8°C).""",
        "flashcards": [
            ("Quais são as 5 etapas do Processo de Enfermagem segundo o COFEN?", "1. Avaliação; 2. Diagnóstico; 3. Planejamento; 4. Implementação; 5. Evolução."),
            ("Qual a referência de FC normal em adultos em repouso?", "60 a 100 bpm.")
        ]
    },
    "farmacologia": {
        "titulo": "💊 Farmacologia Aplicada",
        "resumo": """💊 FARMACOLOGIA E ADMINISTRAÇÃO DE MEDICAMENTOS

1. FARMACOCINÉTICA: Absorção, Distribuição, Metabolização (Fígado) e Excreção (Rins/Bile).
2. VIAS E ÂNGULOS DE APLICAÇÃO:
• Intramuscular (IM): 90° (Ventroglútea, Dorsoglútea, Deltoide, Vasto Lateral).
• Subcutânea (SC): 45° ou 90°.
• Intradérmica (ID): 10° a 15° (Pápula).""",
        "flashcards": [
            ("O que é Farmacocinética?", "Estudo do caminho do fármaco no organismo: Absorção, Distribuição, Metabolização e Excreção."),
            ("Qual o ângulo de aplicação das vias IM, SC e ID?", "IM: 90°; SC: 45° ou 90°; ID: 10° a 15°.")
        ]
    },
    "urgencia_emergencia": {
        "titulo": "🚨 Urgência e Emergência (AHA & PHTLS)",
        "resumo": """🚨 SUPORTE BÁSICO E AVANÇADO DE VIDA

1. RCP EM ADULTOS (AHA):
• Frequência: 100 a 120 compressões/minuto. Profundidade: 5 a 6 cm.
• Sem via aérea avançada: 30:2. Com IOT: Compressões contínuas + 1 ventilação a cada 6 segundos.

2. PROTOCOLO XABCDE DO TRAUMA:
• X: Hemorragia Exsanguinante | A: Vias aéreas e Coluna Cervical | B: Ventilação | C: Circulação | D: Neurologia | E: Exposição.""",
        "flashcards": [
            ("Qual a frequência e profundidade das compressões na RCP em adultos?", "100 a 120 compressões por minuto e profundidade de 5 a 6 cm."),
            ("Quais são os ritmos chocáveis no DEA?", "Fibrilação Ventricular (FV) e Taquicardia Ventricular sem Pulso (TVSP).")
        ]
    },
    "materno_infantil": {
        "titulo": "👶 Enfermagem Materno-Infantil e Pediatria",
        "resumo": """👶 SAÚDE DA MULHER E PEDIATRIA

1. OBSTETRÍCIA: Eclampsia (Pré-eclampsia + Convulsões) -> Tratamento com Sulfato de Magnésio.
2. PEDIATRIA: Escala de Apgar (1º e 5º min) e Teste do Pezinho (coleta ideal do 3º ao 5º dia de vida).""",
        "flashcards": [
            ("Qual medicamento trata a crise convulsiva na Eclampsia?", "Sulfato de Magnésio."),
            ("Quando deve ser feito o Teste do Pezinho?", "Entre o 3º e o 5º dia de vida do bebê.")
        ]
    }
}

# BANCO BASE DE QUESTÕES ENFERMAGEM / BIOMÉDICAS
QUESTOES_BASE = [
    {
        "pergunta": "(Anatomia) Qual o trajeto correto do sangue na Pequena Circulação (Pulmonar)?",
        "opcoes": ["Ventrículo Esquerdo -> Aorta -> Corpo", "Ventrículo Direito -> Artéria Pulmonar -> Pulmões -> Veias Pulmonares -> Átrio Esquerdo", "Átrio Direito -> Veias Cavas -> Pulmões", "Ventrículo Direito -> Veias Pulmonares -> Aorta"],
        "correta": 1,
        "explicacao": "A pequena circulação leva sangue venoso do Ventrículo Direito aos pulmões via Artéria Pulmonar e retorna oxigenado ao Átrio Esquerdo."
    },
    {
        "pergunta": "(Citologia) Qual organela é responsável pelo empacotamento, modificação pós-traducional e secreção de proteínas?",
        "opcoes": ["Lisossomo", "Complexo de Golgi", "Peroxissomo", "Retículo Endoplasmático Liso"],
        "correta": 1,
        "explicacao": "O Complexo de Golgi modifica, empacota e direciona as proteínas produzidas no RER."
    },
    {
        "pergunta": "(Histologia) Qual das alternativas apresenta uma característica do Tecido Epitelial?",
        "opcoes": ["Abundante vascularização direta.", "Grande quantidade de matriz extracelular.", "É avascular, nutrido por difusão do tecido conjuntivo.", "Presença marcante de osteoclastos."],
        "correta": 2,
        "explicacao": "O tecido epitelial é avascular e recebe nutrientes por difusão do tecido conjuntivo subjacente."
    },
    {
        "pergunta": "(Bioquímica) Paciente com hiperventilação apresenta pH = 7,52 e pCO2 = 28 mmHg. Qual o distúrbio ácido-básico?",
        "opcoes": ["Acidose Metabólica", "Alcalose Respiratória", "Acidose Respiratória", "Alcalose Metabólica"],
        "correta": 1,
        "explicacao": "pH alto (> 7,45) indica alcalose e pCO2 baixa (< 35 mmHg) confirma origem respiratória."
    },
    {
        "pergunta": "(Saúde Coletiva) Qual princípio do SUS determina tratar desigualmente os desiguais para garantir igualdade de oportunidade?",
        "opcoes": ["Universalidade", "Equidade", "Integralidade", "Descentralização"],
        "correta": 1,
        "explicacao": "A Equidade prioriza ações onde as necessidades e vulnerabilidades são maiores."
    },
    {
        "pergunta": "(Urgência) Na RCP em adultos com via aérea avançada (IOT), qual a frequência de ventilações?",
        "opcoes": ["30 compressões para 2 ventilações.", "1 ventilação a cada 6 segundos com compressões contínuas.", "15 compressões para 2 ventilações.", "2 ventilações a cada 10 segundos."],
        "correta": 1,
        "explicacao": "Com IOT, as compressões são ininterruptas e faz-se 1 ventilação a cada 6 segundos."
    },
    {
        "pergunta": "(Farmacologia) Qual é o ângulo correto para aplicação por via Intradérmica (ID)?",
        "opcoes": ["90°", "45°", "10° a 15°", "30° a 40°"],
        "correta": 2,
        "explicacao": "A via ID é aplicada em ângulo raso de 10° a 15° para formar pápula."
    },
    {
        "pergunta": "(Fundamentos) Qual a frequência respiratória considerada eupneica (normal) em adultos?",
        "opcoes": ["8 a 12 irpm", "12 a 20 irpm", "22 a 28 irpm", "30 a 40 irpm"],
        "correta": 1,
        "explicacao": "A frequência respiratória normal no adulto em repouso varia entre 12 e 20 irpm."
    },
    {
        "pergunta": "(Materno-Infantil) Qual a droga de primeira escolha para tratamento e prevenção de convulsões na Eclampsia?",
        "opcoes": ["Diazepam", "Sulfato de Magnésio", "Hydralazina", "Fenitoína"],
        "correta": 1,
        "explicacao": "O Sulfato de Magnésio é o tratamento padrão-ouro para prevenções de convulsões na pré-eclampsia/eclampsia."
    },
    {
        "pergunta": "(Saúde Coletiva) Qual vacina administrada ao nascer previne formas graves de tuberculose (miliar e meningite)?",
        "opcoes": ["Hepatite B", "BCG", "Pentavalente", "VOP"],
        "correta": 1,
        "explicacao": "A vacina BCG é dada em dose única ao nascer por via intradérmica para prevenção da tuberculose grave."
    }
]

# GERADOR AUTOMÁTICO EXPANSOR PARA 250 QUESTÕES
QUESTOES_PROVA = []
for i in range(250):
    base_q = QUESTOES_BASE[i % len(QUESTOES_BASE)]
    questao_copia = base_q.copy()
    num_questao = i + 1
    
    # Personalização da questão no banco expandido
    if i >= len(QUESTOES_BASE):
        questao_copia["pergunta"] = f"[{num_questao}] " + base_q["pergunta"]
    else:
        questao_copia["pergunta"] = base_q["pergunta"]
        
    QUESTOES_PROVA.append(questao_copia)