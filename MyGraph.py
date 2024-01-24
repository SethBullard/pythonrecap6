import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()

print("Hello World!")

#Create a virtual environment
#Step 1 - create the environemnt
#MAC: python3 -m venv
#Step 2 - Activate the VE
#MAC: source myvenv/bin/activate
#Step 3: Install third party library or module
#in this case: pip3 install matplotlib(or whatever library it is)