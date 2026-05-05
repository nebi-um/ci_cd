def validar_fasta(filepath):
    """
    Valida se um ficheiro está no formato FASTA correto.
    
    Regras FASTA:
    - Linhas de cabeçalho começam com '>'
    - Sequências só podem ter letras (A, T, C, G, N, etc.)
    - Pelo menos uma sequência
    
    Returns:
        dict com 'valido' (bool) e 'erros' (list)
    """
    erros = []
    num_sequencias = 0
    tem_cabecalho = False
    linha_numero = 0
    
    try:
        with open(filepath, 'r') as f:
            for linha in f:
                linha_numero += 1
                linha = linha.strip()
                
                # Ignorar linhas vazias
                if not linha:
                    continue
                
                # Linha de cabeçalho
                if linha.startswith('>'):
                    if not linha[1:].strip():
                        erros.append(f"Linha {linha_numero}: Cabeçalho vazio")
                    tem_cabecalho = True
                    num_sequencias += 1
                
                # Linha de sequência
                else:
                    if not tem_cabecalho:
                        erros.append(f"Linha {linha_numero}: Sequência sem cabeçalho")
                    
                    # Validar caracteres (letras apenas)
                    if not linha.isalpha():
                        erros.append(f"Linha {linha_numero}: Caracteres inválidos na sequência")
        
        # Verificar se tem pelo menos uma sequência
        if num_sequencias == 0:
            erros.append("Ficheiro não contém nenhuma sequência FASTA")
        
    except FileNotFoundError:
        erros.append(f"Ficheiro não encontrado: {filepath}")
    except Exception as e:
        erros.append(f"Erro ao ler ficheiro: {str(e)}")
    
    return {
        'valido': len(erros) == 0,
        'erros': erros,
        'num_sequencias': num_sequencias
    }


def contar_gc_content(sequencia):
    """Calcula percentagem de GC numa sequência"""
    sequencia = sequencia.upper()
    total = len(sequencia)
    if total == 0:
        return 0.0
    gc = sequencia.count('G') + sequencia.count('C')
    return (gc / total) * 100