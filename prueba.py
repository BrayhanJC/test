def resultado(tanqueX, litrosDisponibles):

	print('El tanque {}, tiene {} Litros'.format(tanqueX, litrosDisponibles))


def llenarTanques():

	#tanques
	tanqueA = 10
	tanqueB = 25
	tanqueC = 30
	tanqueD = 53

	#tuberias
	tuberiaTanqueAB = 1
	tuberiaTanqueAC = 4
	tuberiaTanqueCD = 8

	#llenado
	llenarA = 0 
	llenarB = 0 
	llenarC = 0 
	llenarD = 0

	litros = 4

	tiempo = 30

	litrosDisponibles = 0

	for x in range(1,tiempo+1):
	
		if x == 1:

			litrosDisponibles = litrosDisponibles + 4
			llenarA = litrosDisponibles

		if x > 1:

			if llenarB < tanqueB:

				if (llenarB + tuberiaTanqueAB) < tanqueB:

					llenarB = llenarB + tuberiaTanqueAB
					llenarA = llenarA - tuberiaTanqueAB

				else:
					diferencia = tanqueB - llenarB

					llenarB = llenarB + diferencia
					llenarA = llenarA - diferencia

			else:
				print('El tanque B esta totalmente lleno')

			if llenarC < tanqueC:

				if llenarA < tuberiaTanqueAC:

					aux = llenarA
				else:
					aux = tuberiaTanqueAC

				if x > 2:
								
					if (llenarC + aux) < tanqueC:

						llenarC = llenarC + aux
						llenarA = llenarA - aux

					else:
						if llenarB < tanqueB:
							llenarC = llenarC + tuberiaTanqueAC
							llenarA = llenarA - tuberiaTanqueAC
						else:
							diferencia = tanqueC - llenarC
							llenarC = llenarC + diferencia
							llenarA = llenarA - diferencia



				if x >= 1:
					llenarA = llenarA - aux

			else:
				print('El tanque C esta totalmente lleno')


			if x > 2:

				if llenarD < tanqueD:

					if llenarC < tuberiaTanqueCD:

						aux = llenarC
					else:
						aux = tuberiaTanqueCD

					if (llenarD + aux) < tanqueD:

						llenarD = llenarD + aux
						llenarC = llenarC - aux
					else:
						diferencia = tanqueD - llenarD
						llenarD = llenarD + diferencia
						llenarC = llenarC - diferencia	

				else:
					print('El tanque D esta totalmente lleno')


			llenarA = 4

	resultado("Tanque A ", llenarA)
	resultado("Tanque B", llenarB)
	resultado("Tanque C", llenarC)
	resultado("Tanque D", llenarD)

if __name__ == '__main__':

	llenarTanques()
