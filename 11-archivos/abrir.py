manejador=open('registro')
for line in manejador:
	line=line.strip()
	print(line)
manejador.close()
