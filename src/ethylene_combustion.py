import cantera as ct
import numpy as np

gas1 = ct.Solution('gri30.yaml')
gas1.TP = 3500, 5850000
gas1.X = 'C2H4:1, O2:2.19'
gas1.equilibrate('TP')
print(gas1())