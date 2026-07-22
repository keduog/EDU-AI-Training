#!/usr/bin/env bash
#
# Day 3 - Session 4  |  END OF DAY CLEANUP
# ========================================
# Run this in Cloud Shell before you leave.
#
#   bash cleanup.sh

# ---------------------------------------------------------------
# CHANGE THESE
# ---------------------------------------------------------------
RG="rg-student-abebe"
WORKSPACE="ml-abebe"
COMPUTE="ci-abebe"

echo "=============================================="
echo " STEP 1: Stop the compute instance"
echo "=============================================="
az ml compute stop \
    --name "$COMPUTE" \
    --workspace-name "$WORKSPACE" \
    --resource-group "$RG" \
    2>/dev/null && echo "Stop requested." || echo "Could not stop it here - use ML Studio instead."

echo ""
echo "=============================================="
echo " STEP 2: What is still in your resource group?"
echo "=============================================="
az resource list --resource-group "$RG" \
    --query "[].{name:name, type:type}" -o table

echo ""
echo "=============================================="
echo " STEP 3: Compute status"
echo "=============================================="
az ml compute list \
    --workspace-name "$WORKSPACE" \
    --resource-group "$RG" \
    --query "[].{name:name, state:provisioning_state}" -o table 2>/dev/null \
    || echo "Check ML Studio -> Compute instead."

echo ""
echo "----------------------------------------------"
echo "KEEP: storage account, Language resource (nearly free)"
echo "STOP: compute instance (this is the one that bills)"
echo ""
echo "To delete EVERYTHING you made today - cannot be undone:"
echo "  az group delete --name $RG --yes --no-wait"
echo "----------------------------------------------"
