This folder is a case folder used for mid altitude case (30 kPa ambient pressure).
For launch from ground replace boundary and initial conditions related to ambient pressure from 30kPa to 100 kPa.
Default boundary conditions are in folder /0/default
Copy files, edit values i p file
then run usual 
$setFields
$rhoCentralFoam

For running on AWS use attached shell script (modify names) that will copy the data to an s3 bucket and terminate your spot instance.
