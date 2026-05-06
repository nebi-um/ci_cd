from unittest.mock import patch
from unittest import TestCase
from src.ci_cd.hello_ncbi import processar_artigos

class TestNCBI(TestCase):
    @patch('src.ci_cd.hello_ncbi.obter_pmids')
    def test_processar_artigos(self, mock_obter):
        mock_obter.return_value = ['12345678', '87654321', '11111111']
        
        resultado = processar_artigos('cancer')
        
        assert resultado == "Encontrados 3 artigos sobre cancer"
        mock_obter.assert_called_once_with('cancer')