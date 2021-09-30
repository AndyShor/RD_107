This folder contains scripts to calculate input data for thermophysical properties.

* ethylene_combustion.py - uses Cantera to predict RP-1+LOX combustion product composition
* janaf_data_reader.py - uses JANAF data for major combustion products stored in /data
to return molecular weight and polynomial fit of Cp(T) based on given composition.
Several relevant compositions available in the script to chose from

To run cantera simulations use a separate environment

```console
foo@bar:~$ cd /this_repo/src
foo@bar:~$ conda env create -f cantera_env.yaml
foo@bar:~$ conda activate ct-env
```
