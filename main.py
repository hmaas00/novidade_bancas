import fgv_strategy as fgv

conferir = ['https://conhecimento.fgv.br/concursos/concursocgu21',
            'https://conhecimento.fgv.br/concursos/tcu21',
            'https://conhecimento.fgv.br/concursos/tjdft22']

for p in conferir:
    
    m = fgv.ultima_mensagem(p)

    print(f'de {p.split("/")[-1]}:\n{m}\n')

