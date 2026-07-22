# Tonight's checklist — 8 trainees, class tomorrow

Emails confirmed. About 25 minutes of clicking. Work straight down this page.

## Your 8 trainees

| # | Name | Email | Resource group |
|---|---|---|---|
| 1 | Gizachew | `gizachewarega1@gmail.com` | `rg-student-gizachew` |
| 2 | Haile | `haileyeehate1221@gmail.com` | `rg-student-haile` |
| 3 | Abebayehu | `abebayehu333@gmail.com` | `rg-student-abebayehu` |
| 4 | Amanuel | `shunkeman@gmail.com` | `rg-student-amanuel` |
| 5 | Asaye | `asayee36@gmail.com` | `rg-student-asaye` |
| 6 | Muhammed | `amaan7634@gmail.com` | `rg-student-muhammed` |
| 7 | Biruk | `birukgirma47@gmail.com` | `rg-student-biruk` |
| 8 | Adem | `ademendris752@gmail.com` | `rg-student-adem` |

---

## ① Register resource providers (3 min)

**Do this first.** Without it, everybody's Session 3 fails tomorrow afternoon.

Portal → search **Subscriptions** → **Azure subscription 1** → **Resource providers**
(left menu) → search each name → click it → **Register**.

- [ ] Microsoft.MachineLearningServices
- [ ] Microsoft.CognitiveServices
- [ ] Microsoft.Storage
- [ ] Microsoft.KeyVault
- [ ] Microsoft.Insights
- [ ] Microsoft.ContainerRegistry

Already says **Registered**? Skip it.

---

## ② Invite the 8 people (8 min)

**https://entra.microsoft.com** → **Entra ID** → **Users** → **New user** →
**Invite external user**

Paste the email, type the name, **Review + invite**. Repeat.

- [ ] `gizachewarega1@gmail.com` — Gizachew
- [ ] `haileyeehate1221@gmail.com` — Haile
- [ ] `abebayehu333@gmail.com` — Abebayehu
- [ ] `shunkeman@gmail.com` — Amanuel
- [ ] `asayee36@gmail.com` — Asaye
- [ ] `amaan7634@gmail.com` — Muhammed
- [ ] `birukgirma47@gmail.com` — Biruk
- [ ] `ademendris752@gmail.com` — Adem

---

## ③ Create the 8 resource groups (5 min)

Portal → **Resource groups** → **+ Create**.
Region: **North Europe** for all of them.

- [ ] `rg-student-gizachew`
- [ ] `rg-student-haile`
- [ ] `rg-student-abebayehu`
- [ ] `rg-student-amanuel`
- [ ] `rg-student-asaye`
- [ ] `rg-student-muhammed`
- [ ] `rg-student-biruk`
- [ ] `rg-student-adem`

---

## ④ Give each person Contributor on THEIR group (8 min)

For each row: **open that resource group** → **Access control (IAM)** → **+ Add** →
**Add role assignment** → **Contributor** → **Next** → **Select members** → paste their
email → select them → **Select** → **Review + assign**

> ⚠️ **CHECK THE PAGE TITLE BEFORE YOU CLICK ADD.**
> It must read *rg-student-... | Access control (IAM)* — **not** *Azure subscription 1*.
> At subscription level every trainee could delete everyone else's work, including yours.

- [ ] `rg-student-gizachew` ← `gizachewarega1@gmail.com`
- [ ] `rg-student-haile` ← `haileyeehate1221@gmail.com`
- [ ] `rg-student-abebayehu` ← `abebayehu333@gmail.com`
- [ ] `rg-student-amanuel` ← `shunkeman@gmail.com`
- [ ] `rg-student-asaye` ← `asayee36@gmail.com`
- [ ] `rg-student-muhammed` ← `amaan7634@gmail.com`
- [ ] `rg-student-biruk` ← `birukgirma47@gmail.com`
- [ ] `rg-student-adem` ← `ademendris752@gmail.com`

---

## ⑤ Message the group (2 min)

Copy and send:

> Tomorrow we work on Microsoft Azure.
>
> You will receive an email from **Microsoft Invitations**. Please accept it tonight or
> first thing tomorrow morning.
>
> **Please check your Spam / Junk folder** — it usually lands there.
>
> If your Gmail address does not already have a Microsoft account, the link will help
> you create one. It takes a minute and costs nothing. **No credit card is needed.**
>
> After accepting: go to portal.azure.com, sign in, and check that the top-right corner
> says UNIVERSITY OF GONDAR. That is all — you are ready.

---

## ⑥ Tomorrow morning — quick check (2 min)

Portal → **Entra ID** → **Users**. All 8 should be listed.

Status still **PendingAcceptance**? Click the name → **Resend invitation**.
Then pair that person with a classmate and start the class. Do not wait.

---

## Notes for tomorrow

**All 8 are Gmail.** Most will need to create a Microsoft account during redemption —
the link handles it, about a minute. Better they hit that at home tonight than in your
classroom.

**Expected cost for the day:** roughly **$5–10** for 8 people. The only real risk is a
compute instance left running after everyone leaves — hence the joint shutdown at 16:20.

**You still teach the access lesson.** During Session 1, put the projector up and invite
one spare address of your own live: create a group, assign Contributor, show the email
arriving. They watch the real mechanism instead of eight people hunting through spam.

**If someone cannot get in at all:** pair them with a classmate on one machine. Fix it
at the break. Nobody sits idle.
