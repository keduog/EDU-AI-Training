#!/usr/bin/env bash
#
# Day 3 - Session 2  |  Undo what you created, if you want to start again.
#
# WARNING: this deletes data. There is no undo.

RG="rg-student-abebe"          # <-- your resource group
STORAGE="stabebe2026cli"       # <-- the storage account to delete

echo "About to DELETE storage account: $STORAGE"
read -p "Type yes to continue: " confirm
[ "$confirm" != "yes" ] && { echo "Cancelled."; exit 0; }

az storage account delete --name $STORAGE --resource-group $RG --yes
echo "Deleted."

# To delete EVERYTHING in your resource group at once (much more drastic):
#   az group delete --name $RG --yes --no-wait
