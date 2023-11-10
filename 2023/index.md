---
layout: 2023/event
title: WEPGCOMP 2023
main_page: true

logo: assets/images/logo-ic.png
event_initials: WEPGCOMP 2023
event_name: Workshop de Estudantes de Pós-Graduação em Ciência da Computação do PGCOMP-UFBA
date_and_place: '23 e 24 de novembro de 2023'
banner_image: assets/images/ssa03_Elevador.JPG
kickoff: { year: 2023, month: 11, day: 23, hour: 8, minute: 30 }

about1: O Workshop de Estudantes de Pós-Graduação em Ciência da Computação – WEPGCOMP – é um evento anual organizado pelo Programa de Pós Graduação em Ciência da Computação (PGCOMP) da Universidade Federal da Bahia (UFBA).
about2: 'O objetivo do evento é apresentar as pesquisas em andamento realizadas pelos alunos de doutorado (a partir do segundo ano), bem como propiciar um ambiente de troca de conhecimento e congregação para toda a comunidade.'

schedule_preamble: 'O evento conta com <b>N_TALKS apresentações</b>, divididas em <b>N_SESSIONS sessões</b> ao longo de <b>N_DAYS dias</b>.<br>Os <b>slides</b> estarão disponíveis na <a style="font-weight: bold; color: #ff6600;" href="https://zenodo.org/communities/wepgcomp-ic-ufba/">comunidade do PGCOMP no Zenodo</a>.'
schedule_legend: '
<span class="legend-item"><span class="square cvis"></span>Computação Visual</span>
<span class="legend-item"><span class="square es"></span>Engenharia de Software</span>
<span class="legend-item"><span class="square icot"></span>Inteligência Computacional e</span> <span class="legend-item">Otimização</span>
<span class="legend-item"><span class="square ihcedu"></span>Interação Humano-Computador</span> <span class="legend-item">e Informática e Educação</span>
<span class="legend-item"><span class="square rc"></span>Redes de Computadores</span>
<span class="legend-item"><span class="square scmisc"></span>Sistemas Computacionais</span>
<span class="legend-item"><span class="square sd"></span>Sistemas Distribuídos</span>
<span class="legend-item"><span class="square sibw"></span>Sistemas de Informação,</span> <span class="legend-item">Banco de Dados e Web</span>
'

latitude: -13.000013
longitude: -38.507598
building: Pavilhão de Aulas da<br>Federação II (PAF II), UFBA
address: Tv. Barão de Jeremoabo - Ondina,<br>Salvador - BA, 40170-115

staff:
  'Comissão organizadora':
    - Robespierre Pita
    - Christina von Flach
    - Rodrigo Rocha
  'Apoio a TI e transmissão':
    - Bianco Oliveira
    - Hugo Chaves
    - Jessé Ferreira
  'Apoio às sessões':
    - Hugo Chaves
  'Comunicação':
    - Ivan do Carmo Machado
  'Apoio administrativo':
    - Kleber Batista
    - Silvana Barros


program:
  days:
  - name: Dia 1
    date: 23 / 11 / 2023
    slots: [
      '9:00', # Opening
      '9:30', '9:50', '10:10', # Session 1
      '10:30', # coffee break
      '10:40', '11:10', '11:30', '11:50', # Session 2
      '12:10', # lunch break
      '13:30', # keynote
      '14:35', '14:55', # Session 3
      '15:15', # coffee break
      '15:30', '15:50', '16:10', '16:30', # Session 4
    ]
    rooms:
    - name: Sala A
    - name: Sala B
  - name: Dia 2
    date: 24 / 11 / 2023
    slots: [
      '9:30', '9:50', '10:10', # Session 1
      '10:30', # coffee break
      '10:40', '11:10', '11:30', '11:50', # Session 2
      '12:10', # lunch break
    ]
    roomless: {}
    rooms:
    - name: Sala A
    - name: Sala B
  breaks:
    'Dia 1, 9:00': { title: 'Abertura (Sala A)' }
    'Dia 1, 10:30': { title: 'Intervalo' }
    'Dia 1, 12:10': { title: 'Pausa para almoço' }
    'Dia 1, 13:30': { title: 'Palestra' }
    'Dia 1, 15:15': { title: 'Intervalo' }
    'Dia 2, 10:30': { title: 'Intervalo' }
  talks:
    'Dia 1, Sala A, 9:30': { presenter: 'Elisangela Oliveira Carneiro', title: 'Sistemas de Reputação baseados em Blockchain para ambientes IoT', advisor: 'Fabíola Gonçalves Pereira Greve', topic_abbr: 'sd', topic: 'SC: Sistemas Distribuídos (SD)', }
    'Dia 1, Sala A, 9:50': { presenter: 'Francisco Renato Cavalcante Araújo', title: 'Serviços Diferenciados em Redes Centradas na Informação', advisor: 'Leobino Nascimento Sampaio', topic_abbr: 'rc', topic: 'SC: Redes de Computadores (RC)', }
    'Dia 1, Sala A, 10:10': { presenter: 'Eonassis oliveira santos ', title: 'Restauração redes óticas EON em casos de desastres com falhas em cascata', advisor: 'Gustavo Bittencourt Figueiredo', topic_abbr: 'rc', topic: 'SC: Redes de Computadores (RC)', }
    'Dia 1, Sala B, 9:30': { presenter: 'Paulo Roberto Silva Chagas Júnior', }
    'Dia 1, Sala B, 9:50': { presenter: 'Mirlei Moura da Silva', title: 'Numerical and Time Series Distance', advisor: 'ROBESPIERRE DANTAS DA ROCHA PITA', topic_abbr: 'icot', topic: 'CA: Inteligência Computacional e Otimização (ICOT)', }
    'Dia 1, Sala B, 10:10': { presenter: 'Rafaela Souza Alcântara', title: 'Redução de artefatos metálicos em tomografias computadorizadas para área odontológica', advisor: 'ANTONIO LOPES APOLINARIO JUNIOR', topic_abbr: 'cvis', topic: 'CA: Computação Visual (CVIS)', }
    'Dia 1, Sala A, 10:40': { presenter: 'Tadeu Nogueira Costa de Andrade', title: 'Ferramentas de Estatísticas e de Inteligência Computacional para Análise do WCET em Arquiteturas Multi-core', advisor: 'George Marconi de Araujo Lima', coadvisor: 'Veronica Maria Cadena Lima', topic_abbr: 'scmisc', topic: 'SC: Sistemas Embarcados e de Tempo Real (SETR)', }
    'Dia 1, Sala A, 11:10': { presenter: 'Elivelton Oliveira Rangel', title: 'MODELAGEM COMPUTACIONAL DE ESPAÇOS URBANOS UTILIZANDO DADOS GEO-ESPACIAIS PARA SUPORTE À SISTEMAS DE GERENCIAMENTO DE  EMERGÊNCIAS', advisor: 'Maycon Leone Maciel Peixoto', coadvisor: 'Daniel Gouveia Costa', topic_abbr: 'scmisc', topic: 'CA: Sistemas de Informação, Banco de Dados e Web (SIBW)', }
    'Dia 1, Sala A, 11:30': { presenter: 'Antonio Cleber de Sousa Araujo', }
    'Dia 1, Sala A, 11:50': { presenter: 'Adriana Viriato Ribeiro', title: 'Enabling Plug-n-Play Security for Ambient Assisted-Living Applications', advisor: 'Leobino Nascimento Sampaio', topic_abbr: 'rc', topic: 'SC: Redes de Computadores (RC)', }
    'Dia 1, Sala B, 10:40': { presenter: 'Mariese Conceição Alves dos Santos', title: 'Offloading de Dados Veiculares na Edge Computing Através de Heterogêneas Redes ', advisor: 'Maycon Leone Maciel Peixoto', topic_abbr: 'icot', topic: 'CA: Inteligência Computacional e Otimização (ICOT)', }
    'Dia 1, Sala B, 11:10': { presenter: 'Edeyson Andrade Gomes', title: 'Uma abordagem baseada em ontologia para auxiliar a aplicação de princípios curriculares orientados a competências em recursos educacionais abertos.', advisor: 'Laís do Nascimento Salvador', topic_abbr: 'ihcedu', topic: 'CA: Interação Humano-Computador (IHC) e Informática e Educação (IEDU)', }
    'Dia 1, Sala B, 11:30': { presenter: 'Claudio Junior Nascimento da Silva', title: 'Sistemas de IoT Tolerante a Falhas com uso de IA e Blockchain', advisor: 'CASSIO VINICIUS SERAFIM PRAZERES', topic_abbr: 'sd', topic: 'IOT, IA, Blockchain e Tolerância a Falhas', }

    'Dia 1, Sala A, 14:35': { presenter: 'Ernando Passos Batista Junior', title: 'Solution based on deep neural networks to improve communication of reactive OpenFlow/SDN networks in Fog of Things data streams.', advisor: 'Cássio Prazeres', coadvisor: 'Gustavo Bittencourt', topic_abbr: 'sibw', topic: 'CA: Sistemas de Informação, Banco de Dados e Web (SIBW)', }
    'Dia 1, Sala A, 14:55': { presenter: 'Bruno Souza Cabral', title: 'Comparison of Generative and Sequence Labeling Methods for Portuguese Open Information Extraction', advisor: ' DANIELA BARREIRO CLARO ', coadvisor: 'Marlo Vieira dos Santos e Souza', topic_abbr: 'icot', topic: 'CA: Inteligência Computacional e Otimização (ICOT)', }
    'Dia 1, Sala B, 14:35': { presenter: 'Guilherme Braga Araújo', title: 'Explorando características de redes de dados nomeados para oferecer serviços na borda das redes para aplicações distribuídas por meio de redes veiculares.', advisor: 'Leobino Nascimento Sampaio', topic_abbr: 'rc', topic: 'SC: Redes de Computadores (RC)', }
    'Dia 1, Sala B, 15:05': { presenter: 'Antonio Mateus de Sousa', title: 'A NDN como proposta de aquitetura para a Internet do futuro baseada na Confiança', advisor: 'Leobino Nascimento Sampaio', topic_abbr: 'rc', topic: 'SC: Redes de Computadores (RC)', }
    'Dia 1, Sala A, 15:30': { presenter: 'George Pacheco Pinto', title: 'FoT-PDS: Towards Data Privacy in a Fog of Things', advisor: 'Cássio Serafim Prazeres', topic: 'CA: Internet das Coisas', }
    'Dia 1, Sala A, 15:50': { presenter: 'Felipe Gustavo de Souza Gomes', }
    'Dia 1, Sala A, 16:10': { presenter: 'Maria Clara Pestana Sartori', title: 'United for Humanity: Developing a Collaborative Model for Crowd Engagement in Crisis Recovery Campaigns', advisor: 'Vaninha Vieira', topic_abbr: 'sibw', topic: 'CA: Sistemas de Informação, Banco de Dados e Web (SIBW)', }
    'Dia 1, Sala A, 16:30': { presenter: 'Diego Corrêa da Silva', title: '{Exploiting Calibration Settings toward Fairness in Recommender Systems', advisor: 'Frederico Araújo Durão', topic_abbr: 'sibw', topic: 'CA: Sistemas de Informação, Banco de Dados e Web (SIBW)', }
    'Dia 1, Sala B, 15:30': { presenter: 'Nilton Flávio Sousa Seixas', title: 'A methodology for Data-Driven Decision Making  to improve 6G fronthaul systems.', advisor: 'Gustavo Figueiredo', topic_abbr: 'rc', topic: 'SC: Redes de Computadores (RC)', }
    'Dia 1, Sala B, 15:50': { presenter: 'Andre Luiz Romano Madureira', title: 'Otimizando Comunicações NDN em redes MANET', advisor: 'Leobino Nascimento Sampaio', topic_abbr: 'rc', topic: 'SC: Redes de Computadores (RC)', }
    'Dia 1, Sala B, 16:10': { presenter: 'JHONATAN MACHADO NASCIMENTO', }

    'Dia 2, Sala A, 9:30': { presenter: 'ANTONIO CARLOS MARCELINO DE PAULA', }
    'Dia 2, Sala A, 9:50': { presenter: 'Beatriz Silva de Santana', title: 'Exploring Psychological Safety in Software Engineering: Insights from Stack Exchange', advisor: 'MANOEL GOMES DE MENDONCA NETO', topic_abbr: 'es', topic: 'ESS: Engenharia de Software Experimental', }
    'Dia 2, Sala A, 10:10': { presenter: 'Carlos Frederico Jansen Muakad', title: 'Mapeamento de sites de pergunta e resposta: uma abordagem comparativa entre os principais sites existentes a luz da engenharia de software', advisor: 'Manoel Mendonça Neto', coadvisor: 'Glauco Carneiro', topic_abbr: 'es', topic: 'ESS: Engenharia de Software Experimental', }
    'Dia 2, Sala A, 10:40': { presenter: 'Cleberton Carvalho Soares', title: 'Modelo de maturidade em proteção de dados para adequação dos sistemas de software à Lei Geral de Proteção de Dados (LGPD)', advisor: 'Rita Suzana Pitangueira Maciel', topic_abbr: 'es', topic: 'ESS: Proteção de dados pessoais', }
    'Dia 2, Sala A, 11:10': { presenter: 'Glaucya Carreiro Boechat', title: 'Uma Investigação sobre Análise de Sentimentos e Categorização de Issues Reabertas do GitHub', advisor: 'Manoel Gomes de Mendonça Neto', coadvisor: 'Ivan do Carmo Machado', topic_abbr: 'es', topic: 'ESS: Medição, Mineração e Visualização de Software', }
    'Dia 2, Sala A, 11:30': { presenter: 'LIDIANY CERQUEIRA SANTOS', }
    'Dia 2, Sala A, 11:50': { presenter: 'Mayka de Souza Lima', title: 'A CONCEPTUAL FRAMEWORK FOR THE DESIGN OF VIRTUAL LEARNING ENVIRONMENTS', advisor: 'Rita Suzana Pintagueira Maciel', topic_abbr: 'es', topic: 'ESS: Educação em Engenharia de Software.', }
---

