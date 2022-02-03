from classes.cpc import ContaPoupanca
from classes.ccc import ContaCorrente

cp = ContaPoupanca(9999, 2222, 0 )

cp.detalhe()
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(1)

print('# '*10)

cc = ContaCorrente(agencia=9999,conta=2222,saldo=0,limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)

