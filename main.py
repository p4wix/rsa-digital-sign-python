from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
from Crypto.PublicKey import RSA
import utils

# odczyt z pliku
rate, data = wavfile.read('sound/sample.wav') # reading wave file.
print("Na starcie: ", data, data.dtype)

# zamiana z int16 na uint8
data = data.astype(np.uint8)
print("Po zmianie na uint8: ", data, data.dtype)
print("Entropia: ", utils.calcEntropy(data))

# funkcja która generuje n bajty
lastIndex = 0
def generateBytes(tab, n):
	global lastIndex
	x = tab[lastIndex]
	for i in range(lastIndex + 1, n):
		x += tab[i]
	lastIndex += n
	return x.astype(np.uint8)

def callback(n):
	return generateBytes(data, n);

# generowanie klucza prywtnego do odczytu
key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

# generowanie klucza publicznego do kodowania
public_key = key.publickey().export_key()
file_out = open("receiver.pem", "wb")
file_out.write(public_key)
file_out.close()