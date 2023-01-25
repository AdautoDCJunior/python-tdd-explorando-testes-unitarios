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

  def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
    entrada = 100000
    entrada_nome = 'Adauto Yamato'
    esperado = 90000

    funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada)
    funcionario_teste.decrescimo_salario()
    resultado = funcionario_teste.salario

    assert resultado == esperado