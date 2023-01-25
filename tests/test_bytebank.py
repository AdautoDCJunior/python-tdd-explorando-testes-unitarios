from codigo.bytebank import Funcionario

class TestClass:
  def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
    # Given-Contexto
    entrada = '13/03/2000'
    esperado = 23

    # When-ação
    funcionario_teste = Funcionario('Teste', entrada, 1111)
    resultado = funcionario_teste.idade()

    # Then-desfecho
    assert resultado == esperado

  def test_quando_sobrenome_recebe_Adauto_Junior_deve_retornar_Junior(self):
    entrada = ' Adauto Junior '
    esperado = 'Junior'

    adauto = Funcionario(entrada, '11/11/2000', 1111)
    resultado = adauto.sobrenome()

    assert resultado == esperado