#!/usr/bin/env bash
#
# Day 3 - Session 1  |  TRAINER PRE-FLIGHT CHECK
# ==============================================
# Run this the EVENING BEFORE the class.
#
# For every student in students.txt it reports:
#   - are they in the directory yet?
#   - have they ACCEPTED the invitation?
#   - does their resource group exist?
#   - do they have the Contributor role on it?
#
# HOW TO RUN
#   bash verify_setup.sh

RG_PREFIX="rg-student"
STUDENT_FILE="students.txt"

SUBSCRIPTION_ID=$(az account show --query id -o tsv)

echo "=================================================================="
echo " PRE-FLIGHT CHECK  -  subscription $(az account show --query name -o tsv)"
echo "=================================================================="
printf "%-32s %-10s %-10s %-8s\n" "STUDENT" "INVITED" "ACCEPTED" "ROLE"
echo "------------------------------------------------------------------"

READY=0
NOT_READY=0

while IFS=, read -r EMAIL NAME; do
  [[ -z "$EMAIL" || "$EMAIL" == \#* ]] && continue
  EMAIL=$(echo "$EMAIL" | xargs)
  NAME=$(echo "$NAME" | xargs)
  RG="${RG_PREFIX}-${NAME}"

  # Guest users are stored with the original address in otherMails / mail
  USER_JSON=$(az ad user list --filter "mail eq '$EMAIL'" \
                --query "[0].{id:id, state:externalUserState}" -o json 2>/dev/null)

  USER_ID=$(echo "$USER_JSON" | grep -o '"id": *"[^"]*"' | cut -d'"' -f4)
  STATE=$(echo "$USER_JSON" | grep -o '"state": *"[^"]*"' | cut -d'"' -f4)

  if [ -z "$USER_ID" ]; then
    INVITED="NO"; ACCEPTED="-"; ROLE="-"
  else
    INVITED="yes"
    # externalUserState: PendingAcceptance = not yet clicked; Accepted = done
    if [ "$STATE" == "PendingAcceptance" ]; then
      ACCEPTED="PENDING"
    else
      ACCEPTED="yes"
    fi

    HAS_ROLE=$(az role assignment list \
        --assignee "$USER_ID" \
        --scope "/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RG" \
        --query "[?roleDefinitionName=='Contributor'] | length(@)" -o tsv 2>/dev/null)

    if [ "$HAS_ROLE" == "0" ] || [ -z "$HAS_ROLE" ]; then ROLE="MISSING"; else ROLE="yes"; fi
  fi

  printf "%-32s %-10s %-10s %-8s\n" "$NAME <${EMAIL:0:18}>" "$INVITED" "$ACCEPTED" "$ROLE"

  if [ "$ACCEPTED" == "yes" ] && [ "$ROLE" == "yes" ]; then
    READY=$((READY+1))
  else
    NOT_READY=$((NOT_READY+1))
  fi

done < "$STUDENT_FILE"

echo "------------------------------------------------------------------"
echo " READY: $READY     NEEDS ATTENTION: $NOT_READY"
echo "=================================================================="
echo ""
echo "WHAT TO DO:"
echo "  INVITED = NO       -> rerun setup_students.sh for that person"
echo "  ACCEPTED = PENDING -> they have not clicked the email yet."
echo "                        Entra ID > Users > [them] > Resend invitation"
echo "                        Remind them to check Spam/Junk."
echo "  ROLE = MISSING     -> rerun setup_students.sh, or assign Contributor"
echo "                        on their RESOURCE GROUP (not the subscription)"
echo ""
echo "Students with ACCEPTED = PENDING can still be fixed on the morning,"
echo "but chase them tonight - it saves 30 minutes of class time."
