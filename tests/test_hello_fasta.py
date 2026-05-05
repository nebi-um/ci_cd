import unittest
import os
import tempfile
from src.ci_cd.hello_fasta import validar_fasta, contar_gc_content


class TestFastaValidator(unittest.TestCase):
    
    def setUp(self):
        """Criar ficheiros temporários para testes"""
        self.temp_dir = tempfile.mkdtemp()
    
    def criar_fasta_temporario(self, conteudo, nome="test.fasta"):
        """Helper para criar ficheiro FASTA temporário"""
        filepath = os.path.join(self.temp_dir, nome)
        with open(filepath, 'w') as f:
            f.write(conteudo)
        return filepath
    
    def test_fasta_valido(self):
        """Testa ficheiro FASTA válido"""
        conteudo = """>seq1 descrição
                    ATCGATCG
                    GCTAGCTA
                    >seq2
                    AAATTTGGGCCC
                    """
        filepath = self.criar_fasta_temporario(conteudo)
        resultado = validar_fasta(filepath)
        
        self.assertTrue(resultado['valido'])
        self.assertEqual(len(resultado['erros']), 0)
        self.assertEqual(resultado['num_sequencias'], 2)
    
    def test_fasta_sem_cabecalho(self):
        """Testa sequência sem cabeçalho (inválido)"""
        conteudo = "ATCGATCG\nGCTAGCTA"
        filepath = self.criar_fasta_temporario(conteudo)
        resultado = validar_fasta(filepath)
        
        self.assertFalse(resultado['valido'])
        self.assertGreater(len(resultado['erros']), 0)
    
    def test_fasta_caracteres_invalidos(self):
        """Testa sequência com números (inválido)"""
        conteudo = """>seq1
                    ATCG123ATCG
                    """
        filepath = self.criar_fasta_temporario(conteudo)
        resultado = validar_fasta(filepath)
        
        self.assertFalse(resultado['valido'])
        self.assertIn('Caracteres inválidos', resultado['erros'][0])
    
    def test_fasta_vazio(self):
        """Testa ficheiro vazio"""
        filepath = self.criar_fasta_temporario("")
        resultado = validar_fasta(filepath)
        
        self.assertFalse(resultado['valido'])
        self.assertIn('não contém nenhuma sequência', resultado['erros'][0])
    
    def test_fasta_cabecalho_vazio(self):
        """Testa cabeçalho sem descrição"""
        conteudo = """>
                    ATCGATCG
                    """
        filepath = self.criar_fasta_temporario(conteudo)
        resultado = validar_fasta(filepath)
        
        self.assertFalse(resultado['valido'])
        self.assertIn('Cabeçalho vazio', resultado['erros'][0])
    
    def test_ficheiro_nao_existe(self):
        """Testa ficheiro que não existe"""
        resultado = validar_fasta('/caminho/inexistente.fasta')
        
        self.assertFalse(resultado['valido'])
        self.assertIn('não encontrado', resultado['erros'][0])
    
    def test_gc_content(self):
        """Testa cálculo de GC content"""
        self.assertAlmostEqual(contar_gc_content("ATCG"), 50.0)
        self.assertAlmostEqual(contar_gc_content("AAAA"), 0.0)
        self.assertAlmostEqual(contar_gc_content("GGCC"), 100.0)
        self.assertEqual(contar_gc_content(""), 0.0)
    
    def test_gc_content_case_insensitive(self):
        """Testa GC content com letras minúsculas"""
        self.assertAlmostEqual(contar_gc_content("atcg"), 50.0)
        self.assertAlmostEqual(contar_gc_content("AtCg"), 50.0)


if __name__ == '__main__':
    unittest.main()