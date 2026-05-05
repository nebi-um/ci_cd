from unittest.mock import patch
from unittest import TestCase  # Adicionar isto
from src.ci_cd.hello_ncbi import processar_artigos

class TestNCBI(TestCase):  # Adicionar classe
    @patch('src.ci_cd.hello_ncbi.obter_pmids')  # Corrigir path
    def test_processar_artigos(self, mock_obter):
        # Definir return value
        mock_obter.return_value = ['12345678', '87654321', '11111111']
        
        # Testar
        resultado = processar_artigos('cancer')
        
        # Verificar
        assert resultado == "Encontrados 3 artigos sobre cancer"
        mock_obter.assert_called_once_with('cancer')