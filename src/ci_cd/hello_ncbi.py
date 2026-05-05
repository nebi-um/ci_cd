import requests

def obter_pmids(query):
    """Chama API do NCBI e retorna lista de PMIDs"""
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        'db': 'pubmed',
        'term': query,
        'retmode': 'json'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['esearchresult']['idlist']

def processar_artigos(query):
    """Função que queremos testar"""
    pmids = obter_pmids(query)
    # Processamento dos PMIDs
    total = len(pmids)
    return f"Encontrados {total} artigos sobre {query}"