# Day 3 · Session 2 — Storage, Resources & the Azure CLI

**10:45 – 12:45 (2 hours)**

Now you create real things in the cloud. First by clicking in the portal, then by typing
one command that does the same job.

Everything goes inside **your own resource group**.

---

## 1. Words you need

| Word | What it means |
|---|---|
| **Storage account** | Your own space in Azure for holding files. Cheap, and it never switches off. |
| **Container** | A folder inside the storage account. |
| **Blob** | One file inside a container — a CSV, an image, anything. |
| **Region** | Which data centre in the world holds your data. Pick one close to you. |
| **Azure CLI** | Commands that do the same thing as clicking. Every one starts with `az`. |
| **Cloud Shell** | A terminal inside the Azure portal. Nothing to install. |

---

## 2. Lab 2A — Create a storage account (25 min)

1. In the portal search bar, type **`Storage accounts`** and press Enter
2. Click **+ Create**
3. Fill in the form:

   | Field | What to put |
   |---|---|
   | Subscription | Leave as it is |
   | **Resource group** | **YOUR group** — `rg-student-yourname` |
   | **Storage account name** | `stabebe2026` — lowercase letters and numbers only, 3–24 characters |
   | **Region** | The same one all week, e.g. **(Europe) North Europe** |
   | Performance | **Standard** |
   | Redundancy | **LRS (Locally-redundant storage)** — the cheapest |

4. Click **Review + create**
5. Click **Create**
6. Wait for **"Your deployment is complete"**, then click **Go to resource**

> **Name rejected?** Storage account names must be unique across the *entire world*.
> Add numbers until the green tick appears.

> **Wrong resource group?** You will get an error saying you do not have permission.
> That is Contributor working correctly — you can only build inside your own group.

---

## 3. Lab 2B — Upload your dataset (20 min)

1. Inside your storage account, click **Containers** in the left menu
2. Click **+ Container**
3. Name: **`data`**. Public access level: **Private**. Click **Create**
4. Click into the `data` container
5. Click **Upload**
6. Choose **`soldiers_fitness.csv`** from this folder
7. Click **Upload**

Click the file name to see its details. **Your data is now in the cloud** — the same file
from Day 1, except now any Azure service can reach it.

---

## 4. Lab 2C — Open Cloud Shell (15 min)

Cloud Shell is a terminal that runs inside the Azure portal. You do not install anything.

1. Click the **`>_`** icon at the top of the portal
2. Choose **Bash** (not PowerShell)
3. If it asks about storage, click **Create storage** — this happens once, ever
4. Wait for the black terminal to appear

Now type these, one at a time, pressing Enter after each:

```bash
# Who am I signed in as?
az account show --output table

# Which resource groups can I see?
az group list --output table

# What is inside my resource group?
az resource list --resource-group rg-student-yourname --output table
```

### Why bother with commands?

Clicking through 30 screens cannot be repeated, shared, or saved. One command can.
Real teams script everything they do more than once.

---

## 5. Lab 2D — Do it again with commands (25 min)

Everything you clicked in Labs 2A and 2B, in four commands.

Open **`create_resources.sh`** in this folder, change the two names at the top, then run
the lines **one at a time** in Cloud Shell so you can see what each does.

```bash
# 1. Your own names - change these
RG="rg-student-abebe"
STORAGE="stabebe2026cli"

# 2. Create the storage account
az storage account create \
    --name $STORAGE \
    --resource-group $RG \
    --location northeurope \
    --sku Standard_LRS

# 3. Create a container inside it
az storage container create \
    --name data \
    --account-name $STORAGE \
    --auth-mode login

# 4. Upload the file
az storage blob upload \
    --account-name $STORAGE \
    --container-name data \
    --name soldiers_fitness.csv \
    --file soldiers_fitness.csv \
    --auth-mode login
```

> To get the CSV into Cloud Shell, use the **upload button** (`{}` icon with an arrow)
> at the top of the Cloud Shell window.

Check it worked:

```bash
az storage blob list \
    --account-name $STORAGE \
    --container-name data \
    --auth-mode login \
    --output table
```

Then refresh the portal — the second storage account is there too.

---

## 6. Optional — read the data from Python

If you want to see how an application would use this data, run **`read_from_storage.py`**
in Cloud Shell:

```bash
pip install azure-storage-blob azure-identity pandas
python read_from_storage.py
```

Edit the two names at the top of the file first.

---

## 7. Files in this folder

| File | What it is |
|---|---|
| `README.md` | This guide |
| `soldiers_fitness.csv` | The dataset to upload |
| `create_resources.sh` | All the commands from Lab 2D, with comments |
| `read_from_storage.py` | Reads the CSV back out of Blob Storage using Python |
| `cleanup.sh` | Deletes what you created, if you want to start again |

---

## 8. Checklist

- [ ] I created a storage account inside **my own** resource group
- [ ] I created a container called `data`
- [ ] I uploaded `soldiers_fitness.csv` and can see it in the portal
- [ ] I opened Cloud Shell and ran `az account show`
- [ ] I created a second storage account using only commands
- [ ] I understand that storage costs almost nothing and can stay

**Nothing from this session needs to be switched off.** Storage is cheap and we use it
again after lunch.

---

## 9. If something goes wrong

**"The storage account name is already taken"**
Names are global. Add more numbers.

**"You do not have permission to perform action ... on scope ..."**
You picked the wrong resource group. Choose yours.

**Cloud Shell asks to create storage every time**
It only needs to succeed once. If it keeps asking, tell the trainer — it may need a
resource group you cannot create.

**`az: command not found` in Cloud Shell**
That should never happen — Cloud Shell has the CLI built in. If you are in a normal
terminal on your laptop instead, install it from
<https://learn.microsoft.com/cli/azure/install-azure-cli> or just use Cloud Shell.

**`AuthorizationPermissionMismatch` when uploading a blob**
Add `--auth-mode login` to the command (it is already in the script). If it still fails,
you may need the **Storage Blob Data Contributor** role — ask the trainer.

**The upload button in Cloud Shell does nothing**
Try a different browser, or upload the file through the portal instead (Lab 2B).

---

**Next:** [Session 3 — Azure Machine Learning](../Session3/README.md)
