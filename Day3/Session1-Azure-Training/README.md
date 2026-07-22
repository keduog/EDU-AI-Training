# Day 3 · Session 1 — Azure Foundations & Getting Your Access

**09:00 – 10:30 (1.5 hours)**

Today you use a real Microsoft Azure subscription — the trainer's, belonging to the
University of Gondar. You do **not** need to create an Azure account, you do **not**
need a credit card, and there is no eligibility check.

You are invited as a **guest user** with your own email address.

---

## Part A — For students

### 1. What is Azure?

**Cloud computing** means renting somebody else's computers over the internet instead
of buying your own.

**Azure** is Microsoft's cloud — thousands of computers in data centres worldwide that
you can rent by the minute.

On Day 1 you used Google Colab: free and simple. Azure is what organisations use when
they need real control, real security, and real scale.

### 2. The four levels

```
TENANT                University of Gondar (uog.edu.et) — where user accounts live
  └─ SUBSCRIPTION     "Azure subscription 1" — where the bill goes (the trainer's)
       └─ RESOURCE GROUP    rg-student-abebe — YOUR folder
            └─ RESOURCES    storage account, ML workspace, AI service...
```

| Level | What it is | Who controls it |
|---|---|---|
| **Tenant** | The directory of people | The university |
| **Subscription** | The billing container | The trainer |
| **Resource group** | Your own folder | **You** |
| **Resource** | An actual thing you create | **You** |

**You work at the bottom two levels only.**

### 3. What is a guest user?

You keep your own email address — Gmail, Yahoo, Outlook, or your `uog.edu.et` address.
You are added to the university's directory as a **visitor**.

- You sign in with your own Microsoft account
- You get no new password to remember
- You can only see what you have been given access to
- **You need no credit card and no Azure subscription of your own**

> This has already been tested for this course. A personal Yahoo address was invited into
> the University of Gondar tenant and signed in successfully. Whatever email you use will
> work the same way.

### 4. What is the Contributor role?

**Contributor** is a set of permissions on **your resource group only**.

| You CAN | You CANNOT |
|---|---|
| Create resources | Give access to other people |
| Change and delete your own resources | Touch another student's resource group |
| Run notebooks, train models | Change billing or the subscription |
| Use AI services | See other students' work |

In one sentence: **guest = you can sign in. Contributor = you can build things, but only
in your own folder.**

---

### 5. Lab 1A — Accept your invitation (15 min)

The trainer sent your invitation before class. It is in your email.

1. Open your email inbox
2. Look for a message from **Microsoft Invitations** (`invites@microsoft.com`),
   subject like *"You're invited to the University of Gondar organization"*
3. Click **Accept invitation**
4. Sign in:
   - **If your email already has a Microsoft account** — enter your password
   - **If it does not** (common with Gmail and Yahoo) — Microsoft walks you through
     creating one for that same address. About a minute, and it costs nothing.
5. Read the permission request and click **Accept**
6. You land on a page confirming you have joined **University of Gondar**

> **No email?** Check **Spam** and **Junk** first — Microsoft invitations very often land
> there. If it is not there, tell the trainer; they resend it in one click.

---

### 6. Lab 1B — Sign in and find your resource group (20 min)

1. Go to **<https://portal.azure.com>**
2. Sign in with **the same email** you used to accept the invitation
3. Look at the **top-right corner**. It must say **UNIVERSITY OF GONDAR** under your name
4. If it does not: click your name → **Switch directory** → **UNIVERSITY OF GONDAR**
5. In the search bar at the top, type **`Resource groups`** and press Enter
6. You should see **`rg-student-yourname`**. Click it.

**This is your working area for the rest of the day.**

### The two mistakes almost everyone makes

**Mistake 1 — wrong directory.**
If the portal looks empty and says "no subscriptions found", you are signed in to your
*own* directory instead of the university's. Do step 4.

**Mistake 2 — wrong account.**
Many people have more than one Microsoft account — a work one and a personal one. The
browser may sign you in with the wrong one automatically. Check the email address in the
top-right corner. If it is wrong: sign out completely, or open a **private / incognito
window** and sign in again.

---

### 7. What costs money

| Costs money while running | Free or nearly free |
|---|---|
| **Compute instance** (Session 3) | Creating a resource group |
| Virtual machines | Browsing the Azure portal |
| Managed online endpoints | Azure AI Language free tier (F0) |
| Large amounts of stored data | Small CSV files in storage |
| **Anything left on overnight** | A **stopped** compute instance |

**The one rule for today:** if you switch on a compute instance, you switch it off before
you leave. We do this together at 16:20.

---

### 8. Checklist

- [ ] I accepted the invitation email
- [ ] I can sign in at portal.azure.com
- [ ] The top-right corner says **UNIVERSITY OF GONDAR**
- [ ] I can see my own resource group
- [ ] I can explain what Contributor lets me do
- [ ] I know which things cost money

---

### 9. If something goes wrong

| Problem | Fix |
|---|---|
| "You don't have any subscriptions" | Wrong directory. Profile → **Switch directory** → University of Gondar |
| Portal is empty, directory is correct | Your role has not been assigned yet. Tell the trainer. |
| Invitation link says expired | Ask the trainer to resend it |
| It signs me in as the wrong person | Sign out completely, or use a private/incognito window |
| I see the group but cannot create anything | Your role may be *Reader*. Ask the trainer to check IAM on your group. |
| I never received any email | Check Spam/Junk, then ask the trainer to resend |

---

## Part B — For the trainer

### Why guest access, and not individual student accounts

You may well be asked this. The short answer:

| Individual free accounts | Guest access to your subscription |
|---|---|
| Each student needs a **credit card** for identity verification | No card, from anybody |
| "Azure for Students" requires **full-time student status** — instructors are blocked | No eligibility check at all |
| Eligibility checks fail unpredictably on the day | Nothing to check |
| $100 credit that runs out | Your subscription, your budget |
| **You cannot see or help with anyone's work** | You see everything |
| **You cannot stop a compute instance somebody forgot** | You can stop anything |
| 30 accounts to create during class time | 15 minutes of setup beforehand |

Guest access is the standard way Microsoft intends organisations to share a subscription.
It is not a workaround.

---

### CRITICAL: assign the role on the RESOURCE GROUP, not the subscription

When you open **Access control (IAM)** it is very easy to be at the *subscription* level
by mistake. **Do not assign Contributor there.**

| Scope | What happens |
|---|---|
| Subscription | Every student can see, change and **delete everything** — other students' work and yours |
| **Resource group** ✅ | Each student can only touch their own folder |

Before clicking **Add role assignment**, check the page title. It must show the
**resource group name**, not "Azure subscription 1".

Navigate: **Resource groups → [the student's group] → Access control (IAM)**.

---

### Step 0 — Register the resource providers (once, before class)

This is the step people miss, and it breaks Session 3 for the whole class.

A student with Contributor on a *resource group* **cannot register resource providers** —
that is a subscription-level action. If a provider is not registered, creating an Azure ML
workspace fails with `MissingSubscriptionRegistration`.

Run this once in Cloud Shell:

```bash
az provider register --namespace Microsoft.MachineLearningServices
az provider register --namespace Microsoft.Storage
az provider register --namespace Microsoft.KeyVault
az provider register --namespace Microsoft.CognitiveServices
az provider register --namespace Microsoft.Insights
az provider register --namespace Microsoft.ContainerRegistry
```

Harmless if they are already registered. Registration takes a few minutes.

---

### Step 1 — Invite each student as a guest

1. Go to <https://entra.microsoft.com>
2. **Entra ID** → **Users** → **New user** → **Invite external user**
3. Enter the student's email address and display name
4. Add a short personal message so it does not look like spam
5. **Review + invite** → **Invite**

### Step 2 — Create one resource group per student

1. In <https://portal.azure.com>: search **Resource groups** → **+ Create**
2. Name: `rg-student-abebe`
3. Region: **North Europe** or **UAE North**
4. **Review + create** → **Create**

### Step 3 — Assign Contributor on that group

1. Open **the resource group** (not the subscription)
2. **Access control (IAM)** → **+ Add** → **Add role assignment**
3. **Role** tab → **Contributor** → **Next**
4. **Members** tab → **Select members** → type the student's email → select → **Select**
5. **Review + assign**

> **Known gotcha:** assigning a role through IAM does **not** reliably send the invitation
> email. Always invite through Entra ID first (Step 1). If a student says they got
> nothing: **Entra ID → Users → [student] → Resend invitation**.

### Do it all with one script instead

`setup_students.sh` does Steps 0–3 for the whole class. Edit `students.txt` first, then
run it in Cloud Shell:

```bash
bash setup_students.sh
```

### Step 4 — Set a budget alert

1. Search **Cost Management** → **Budgets** → **+ Add**
2. Scope: your subscription. Amount: whatever you are comfortable with
3. Alerts at 50%, 80% and 100% to your own email

This does not stop spending, but you will know immediately if something is left running.

### Step 5 — Verify everybody the evening before

```bash
bash verify_setup.sh
```

This lists every student, whether they have accepted their invitation, and whether their
role assignment exists — so you can chase the two or three who have not accepted yet.

---

### What today will cost you

Rough estimate for 30 students, at typical prices. Check your own region — prices vary
and change.

| Item | Estimate |
|---|---|
| Compute instances (30 × ~2 hours, smallest CPU size) | **~$15–25 total** |
| Blob storage (a few small CSV files) | Cents |
| Azure AI Language, free F0 tier | $0 |
| Resource groups, portal, Cloud Shell | $0 |
| **Expected total for the day** | **under $30** |

The risk is not the class — it is one compute instance left running for a week, which can
cost more than the whole day. That is why idle shutdown and the joint 16:20 cleanup matter.

---

### Pre-class communication

Send the email in **`pre_class_email.md`** two days before. It tells students an
invitation is coming, which address it will arrive at, and to check their spam folder.

Sending it early is the single biggest time-saver on the day.

---

### If a student has no invitation on the day

Do not spend more than two minutes on any one person:

1. **Resend** — Entra ID → Users → the student → Resend invitation (30 seconds)
2. **Check the address** — a typo is the most common cause
3. **Still nothing?** Pair them with a classmate on one machine, fix it at the break

Nobody sits idle. Pair work is normal in real teams anyway.

---

**Next:** [Session 2 — Storage & the Azure CLI](../Session2/README.md)
