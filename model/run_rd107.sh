#!/bin/sh
rhoCentralFoam | tee -a logfile
aws s3 cp --recursive /mnt/cfd/rd107 s3://my-cfd-case-bucket/rd107
sudo shutdown -h now