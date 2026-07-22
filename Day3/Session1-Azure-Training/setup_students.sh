#!/usr/bin/env bash
#
# Day 3 - Session 1  |  TRAINER SETUP SCRIPT
# ==========================================
# For each student in students.txt this script will:
#   0. (once) register the resource providers the class needs
#   1. invite them as a guest user in the tenant
#   2. create a resource group just for them
#   3. give them Contributor on THAT RESOURCE GROUP ONLY
#
# The scope in step 3 is the important part. Contributor on the SUBSCRIPTION
# would let every student delete everyone else's work - including yours.
#
# HOW TO RUN
#   1. Open https://portal.azure.com  (signed in as the subscription owner)
#   2. Click the >_ icon at the top (Cloud Shell), choose Bash
#   3. Upload this file and students.txt (the upload button in Cloud Shell)
#   4. Run:  bash setup_students.sh
#
# YOU NEED: Owner or User Access Administrator on the subscription,
#           and permission to invite guests in Entra ID.

set -e   # stop immediately if anything fails

# ---------------------------------------------------------------
# SETTINGS - change these to match your class
# ---------------------------------------------------------------
LOCATION="northeurope"          # data centre region
RG_PREFIX="rg-student"          # groups will be rg-student-abebe, etc.
STUDENT_FILE="students.txt"
REDIRECT_URL="https://portal.azure.com"

# ---------------------------------------------------------------
# Confirm the subscription before touching anything
# ---------------------------------------------------------------
echo "=============================================="
az account show --query "{subscription:name, id:id, tenant:tenantId}" -o table
echo "=============================================="
read -p "Is this the correct subscription? (yes/no) " confirm
if [ "$confirm" != "yes" ]; then
  echo "Stopped. Use: az account set --subscription \"NAME\""
  exit 1
fi

SUBSCRIPTION_ID=$(az account show --query id -o tsv)

# ---------------------------------------------------------------
# STEP 0 - Register resource providers (once per subscription)
#
# Students with Contributor on a resource group CANNOT do this
# themselves - it is a subscription-level action. If a provider is
# not registered, creating the ML workspace in Session 3 fails with
# "MissingSubscriptionRegistration" for the whole class.
#
# Running this again when already registered is harmless.
# ---------------------------------------------------------------
echo ""
echo "=============================================="
echo " STEP 0: registering resource providers"
echo "=============================================="
for NS in Microsoft.MachineLearningServices \
          Microsoft.Storage \
          Microsoft.KeyVault \
          Microsoft.CognitiveServices \
          Microsoft.Insights \
          Microsoft.ContainerRegistry ; do
  echo "  registering $NS ..."
  az provider register --namespace "$NS" --output none || echo "    (already registered or not permitted)"
done
echo "  Registration runs in the background and takes a few minutes."

# ---------------------------------------------------------------
# Loop through every student
# ---------------------------------------------------------------
while IFS=, read -r EMAIL NAME; do

  [[ -z "$EMAIL" || "$EMAIL" == \#* ]] && continue     # skip blanks and comments

  EMAIL=$(echo "$EMAIL" | xargs)   # trim spaces
  NAME=$(echo "$NAME" | xargs)
  RG="${RG_PREFIX}-${NAME}"

  echo ""
  echo "----------------------------------------------"
  echo "STUDENT: $NAME  <$EMAIL>"
  echo "----------------------------------------------"

  # --- 1. Invite as a guest user ------------------------------
  echo "  [1/3] Inviting as guest user..."
  EXISTING=$(az ad user list --filter "mail eq '$EMAIL'" --query "[0].id" -o tsv 2>/dev/null || true)

  if [ -n "$EXISTING" ]; then
    echo "        already in the directory, skipping invite"
    USER_ID="$EXISTING"
  else
    USER_ID=$(az rest --method POST \
      --url "https://graph.microsoft.com/v1.0/invitations" \
      --headers "Content-Type=application/json" \
      --body "{
        \"invitedUserEmailAddress\": \"$EMAIL\",
        \"invitedUserDisplayName\": \"$NAME\",
        \"inviteRedirectUrl\": \"$REDIRECT_URL\",
        \"sendInvitationMessage\": true
      }" --query "invitedUser.id" -o tsv)
    echo "        invitation email sent"
  fi

  # --- 2. Create their resource group --------------------------
  echo "  [2/3] Creating resource group $RG..."
  az group create --name "$RG" --location "$LOCATION" \
      --tags course=EDU-AI-Training day=3 student="$NAME" \
      --output none
  echo "        done"

  # --- 3. Contributor on that RESOURCE GROUP only --------------
  #     Note the --scope: it ends with /resourceGroups/$RG
  #     Never assign at /subscriptions/$SUBSCRIPTION_ID alone.
  echo "  [3/3] Assigning Contributor (resource group scope only)..."
  az role assignment create \
      --assignee-object-id "$USER_ID" \
      --assignee-principal-type User \
      --role "Contributor" \
      --scope "/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RG" \
      --output none
  echo "        done"

done < "$STUDENT_FILE"

echo ""
echo "=============================================="
echo " ALL STUDENTS SET UP"
echo "=============================================="
az group list --query "[?tags.course=='EDU-AI-Training'].{name:name, location:location}" -o table

echo ""
echo "NEXT STEPS:"
echo "  1. Send the email in pre_class_email.md (2 days before)"
echo "  2. Set a budget alert: Cost Management > Budgets > + Add"
echo "  3. The evening before class, run:  bash verify_setup.sh"
echo "     to see who has not accepted their invitation yet"
echo ""
echo "REMINDER FOR THE DAY: tell students to SWITCH DIRECTORY in the"
echo "portal to UNIVERSITY OF GONDAR, or they will see nothing at all."
