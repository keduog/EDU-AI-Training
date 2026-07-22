#!/usr/bin/env bash
#
# Day 3 - Session 1  |  STUDENT SCRIPT
# ====================================
# Run this in Azure Cloud Shell to prove your access is working.
#
# HOW TO RUN
#   1. Go to https://portal.azure.com and sign in
#   2. Switch directory to UNIVERSITY OF GONDAR
#   3. Click the >_ icon at the top, choose Bash
#   4. Paste these commands one at a time

echo "=== 1. Who am I signed in as? ==="
az account show --query "{user:user.name, subscription:name, tenant:tenantId}" -o table

echo ""
echo "=== 2. Which resource groups can I see? ==="
az group list --output table

echo ""
echo "=== 3. What role do I have? ==="
MY_ID=$(az ad signed-in-user show --query id -o tsv)
az role assignment list --assignee "$MY_ID" \
    --query "[].{role:roleDefinitionName, scope:scope}" -o table

echo ""
echo "=== 4. Can I actually create something? (test) ==="
echo "Replace rg-student-yourname below with YOUR group, then run it:"
echo ""
echo "  az storage account check-name --name teststorage12345"
echo ""
echo "If step 2 shows your resource group and step 3 says Contributor,"
echo "your access is working correctly."
