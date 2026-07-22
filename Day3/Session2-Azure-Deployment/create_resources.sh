#!/usr/bin/env bash
#
# Day 3 - Session 2  |  STUDENT SCRIPT
# ====================================
# Everything you clicked in Lab 2A and 2B, done with commands.
#
# DO NOT run this file all at once the first time.
# Read it, then paste the commands ONE AT A TIME into Cloud Shell,
# so you can see what each one does.
#
# HOW TO RUN
#   1. https://portal.azure.com  ->  switch directory to University of Gondar
#   2. Click the >_ icon at the top, choose Bash
#   3. Upload this file and soldiers_fitness.csv using the upload button
#   4. Change the two names below, then run the commands

# ---------------------------------------------------------------
# CHANGE THESE TWO LINES
# ---------------------------------------------------------------
RG="rg-student-abebe"            # <-- your resource group
STORAGE="stabebe2026cli"         # <-- lowercase + numbers only, must be unique worldwide
LOCATION="northeurope"           # <-- keep the same region all day

# ---------------------------------------------------------------
# 0. Check you are in the right place
# ---------------------------------------------------------------
az account show --output table
az group show --name $RG --output table

# ---------------------------------------------------------------
# 1. Create the storage account
#    --sku Standard_LRS is the cheapest option
# ---------------------------------------------------------------
az storage account create \
    --name $STORAGE \
    --resource-group $RG \
    --location $LOCATION \
    --sku Standard_LRS \
    --output table

# ---------------------------------------------------------------
# 2. Create a container (a folder) inside it
# ---------------------------------------------------------------
az storage container create \
    --name data \
    --account-name $STORAGE \
    --auth-mode login \
    --output table

# ---------------------------------------------------------------
# 3. Upload the CSV file
# ---------------------------------------------------------------
az storage blob upload \
    --account-name $STORAGE \
    --container-name data \
    --name soldiers_fitness.csv \
    --file soldiers_fitness.csv \
    --auth-mode login \
    --output table

# ---------------------------------------------------------------
# 4. Check it is really there
# ---------------------------------------------------------------
az storage blob list \
    --account-name $STORAGE \
    --container-name data \
    --auth-mode login \
    --output table

echo ""
echo "Done. Refresh the Azure portal and look inside your storage account."
