# Cadeia de String
frase = 'Teste de python'
print(frase)
print(frase[:10:3])  # Inicia no 0, vai até o 10 e pula de 3 em 3
print(len(frase))  # Length - comprimento da frase
print(frase.count('e', 0, 13))  # Count - conta a quant. de carac.
print(frase.find('de'))  # Find - procura
print("python" in frase)  # outro tipo de procura
print(frase.replace('python', 'Python'))  # substitiu
# frase.upper() e frase.lower() - Transforma em Maiusc. ou Minúscula
print(frase.capitalize())  # Coloca maiúscula a primeira letra da frase
print(frase.title())  # Coloca em maiúscula a primeira letra de cada palavra
# frase.strip() - Remove todos os espaços inúteis (inicio e fim)
# frase.rstrip() - Remove os espaços inúteis na direita (fim)
# frase.lstrip() - Remove os espaços esquerda (inicio)
print(frase.split())  # Divide a frase nos espaços
print('''Third generation FPSO (SBM's Cidade de Maricá);
Triphasic test Separator vessels operation;
Gas treatment (dehydration and CO2 separation) operations;
Gas compressors operations;
Multiphase pumps operations;
HPU systems operations;
PIG’s Launching and receiving;
Utility plants operation;
Fire pumps and fire systems detections operation;
Pressure and leaking testing of the entire process plant;
Assisted in the issuing and control of PTW;
Supply and control of chemicals;\n''')  # 3 aspas para inserir textos grandes !
