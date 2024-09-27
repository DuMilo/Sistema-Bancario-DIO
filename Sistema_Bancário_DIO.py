from time import sleep;

# Para uso geral:
saldo = 0;

# Para o def retirar_valor:
limite = 500;
quant_saques = 0;
LIMITE_SAQUE = 3;

# Para o extrato:
extrato = "";

def exibir_menu():
  print("""\n== Banco do Brasil ==
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair""");

def depositar_valor(valor):
  global saldo;
  global extrato;
  if valor > 0:
    saldo += valor;
    extrato += (f"Depósito: R${valor:.2f}\n");
    print(f"Após o depósito de {valor:.2f}, sua conta tem saldo de {saldo:.2f}.");
    sleep(3);
  else:
    print("Valor Inválido. Tente Novamente!");
    sleep(3);

def retirar_valor(valor):
  global saldo;
  global limite;
  global quant_saques;
  global LIMITE_SAQUE;
  global extrato;

  acima_saldo = valor > saldo;
  acima_limite = valor > limite;
  acima_saques = quant_saques >= LIMITE_SAQUE;

  if acima_saldo:
    print("Valor Inválido! Valor acima do saldo na conta.");
    sleep(3);
  elif acima_limite:
    print("Valor Inválido! Valor acima do limite de saldo.");
    sleep(3);
  elif acima_saques:
    print("Valor Inválido! Número de saques diários já foi alcançado.");
    sleep(3);
  elif valor > 0:
    saldo -= valor;
    print(f"Após o saque de {valor:.2f}, sua conta tem saldo de {saldo:.2f}.");
    quant_saques += 1;
    extrato += (f"Saque: R${valor:.2f}\n");
    sleep(3);
  else:
    print("Valor inserido é inválido. Tente novamente!");
    sleep(3);

def mostrar_extrato():
  global saldo;
  print("\n== EXTRATO ==");
  print("Sem movimentações." if not extrato else extrato);
  print(f"\nSaldo: R$ {saldo:.2f}");
  print("=" * 13);
  sleep(3);

while True:
  exibir_menu();
  opcao = (input("\n>> "));

  if opcao == '1':
    valor = float(input("Quanto você deseja depositar à conta?\n>> "));
    depositar_valor(valor);
  elif opcao == '2':
    valor = float(input("Quanto de saldo você deseja retirar da conta?\n>> "));
    retirar_valor(valor);
  elif opcao == '3':
    mostrar_extrato();
  elif opcao == '4':
    print("Fechando programa... Até logo!");
    sleep(3);
    break;
  else: 
    print("Caractere Inválido! Fechando programa...");
    sleep(3);
    break;