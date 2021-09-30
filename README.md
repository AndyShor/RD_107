# RD107 - legendary rocket engine
CFD case for simulation of RD107 rocket engine.
I wrote a long read article describing technical side of this simulation (here).
I also wrote another short article about my experience running this case on AWS.


Temperature distribution in the first 25 ms after ignition at the sea level
Enjoy propagating shock waves, colliding shock waves (Mach diamonds) and imagine the roar it creates.

![flow](/figures/T_ambient_p=100kPa.gif)

# Repo structure
This repository has the following structure

* data - thermodynamic data of jet engine combustion products, retrieved form JANAF [JANAF](https://janaf.nist.gov/) database and cleaned
* figures - containes images with the run results as well as nozzle drawing, and few other
* model - is the OpenFOAM case folder, can be run 'as is' (see below), configured for sea level launch, 'as is' will take ~24h on average laptop
* notebooks - contains some Jupyter notebooks used to create generate OpenFOAM geometry and gas settings from JANAF data
* src - auxiliary python code to keep notebooks more concise

# Run the model youself

Model case in the /model folder is ready to go, geometry is based on the original drawing of RD107 nozzle

![geom](/figures/RD107.jpg)

With proper OpeFOAM (tested on OpenFOAM v8 on Ubuntu 20.04 (AWS) and 18.04 (WSL) ) the case can be run by just
$blockMesh
$setFields
$rhoCentralFoam

Beware case takes long time to solve, temperature distribution below took 24h to solve.
Solved cases visualized with Paraview applying needed symmetries (select rd107.foam file)

# Modify the case

If you want to use the case as a startinng point use provided notebooks to change geometry.
If your case runs on other oxidizer-fuel pair than RP-1/LOX  (Methane/LOX, Hydrogen/LOX, N₂O₄/UDMH)
you can use provided notebooks, JANAF database and other references to calculate combustion product composition,
molecular mass, and heat capacity (and replace data in /model/constant/thermophysicalProperties)


