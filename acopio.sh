#!/bin/bash

REGION="westeurope"
SIZE="Standard_A0"
GR="CCh4"
MV="h4eur"
IMAGEN="jetware-srl:postgresql:postgresql96-ubuntu-1604:1.0.170503"
USER="jorgeportubunt"
SUBSC="580f87c0-c5fa-45f2-85ef-1484a1631e94"

echo "login en Azure"

az login
az group create -l $REGION -n $GR --subscription $SUBSC

az vm image accept-terms --urn jetware-srl:postgresql:postgresql96-ubuntu-1604:1.0.170503 --subscription $SUBSC


az vm create --resource-group $GR --name $MV --image $IMAGEN --generate-ssh-keys --output json --verbose --size $SIZE --subscription $SUBSC
az vm open-port --resource-group $GR --name $MV --port 80 --subscription $SUBSC


