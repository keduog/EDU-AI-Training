# Session 2 — GitHub & Google Colab

**Day 1 · 10:45 – 12:45 · 2 hours**

This is the longest README of the day, and the most important. Everything you build
for the rest of the week gets stored using the skills on this page.

Work through it top to bottom. Do not skip ahead — each part depends on the one before it.

---

## Contents

1. [What you will end up with](#1-what-you-will-end-up-with)
2. [Creating your GitHub account](#2-creating-your-github-account)
3. [Verifying your account and joining the course organization (`keduog`)](#3-verifying-your-account-and-joining-the-course-organization-keduog)
4. [Navigating GitHub — what every button does](#4-navigating-github--what-every-button-does)
5. [Creating your own repository](#5-creating-your-own-repository)
6. [Committing a dataset in the browser](#6-committing-a-dataset-in-the-browser)
7. [Forking the course repository](#7-forking-the-course-repository)
8. [Installing Git and VS Code](#8-installing-git-and-vs-code)
9. [Cloning with the command line](#9-cloning-with-the-command-line)
10. [Opening the folder in VS Code with `code .`](#10-opening-the-folder-in-vs-code-with-code-)
11. [Commit and push from the command line](#11-commit-and-push-from-the-command-line)
12. [Commit and push from the VS Code interface](#12-commit-and-push-from-the-vs-code-interface)
13. [Branching and merging](#13-branching-and-merging)
14. [Pull requests — merging through GitHub](#14-pull-requests--merging-through-github)
15. [Running the code in Google Colab](#15-running-the-code-in-google-colab)
16. [Files in this folder](#16-files-in-this-folder)
17. [Git command cheat sheet](#17-git-command-cheat-sheet)
18. [Troubleshooting](#18-troubleshooting)
19. [Checklist before you leave](#19-checklist-before-you-leave)

---

## 1. What you will end up with

By 12:45 you will have:

- A GitHub account with a verified email address
- Membership of the course organization `keduog`
- Your own public repository, `my-first-ai-lab`
- A dataset committed inside it
- A fork of the course repository
- Git and VS Code installed and working on your machine
- Both repositories cloned to your computer
- At least one commit pushed from the command line and one from VS Code
- One branch created, merged, and deleted
- The Session 2 notebook running in Google Colab

---

## 2. Creating your GitHub account

**Skip this section if you already have a GitHub account** — jump to section 3.

1. Open a browser and go to **<https://github.com>**
2. Click **Sign up** (green button, top right)
3. Enter your **email address**. Use an address you can open right now — you must click a code that gets sent to it.
4. Create a **password**. GitHub requires at least 15 characters, or 8 characters with a number and a lowercase letter. Write it down somewhere safe.
5. Choose a **username**. This becomes part of every URL you own on GitHub, so choose carefully.

   **Recommended pattern:** `firstname-lastname-edu`

   | Good | Why |
   |------|-----|
   | `abebe-tesfaye-edu` | Readable, professional, obviously yours |
   | `sara-bekele-edu` | Same |

   | Avoid | Why |
   |-------|-----|
   | `xX_dark_coder_Xx` | You will put this on a CV one day |
   | `user12345` | Nobody, including your trainer, can tell who you are |

   If the username is taken, GitHub tells you immediately. Add a number or a middle initial.

6. Answer the "Are you a robot?" puzzle.
7. GitHub emails you an **8-digit launch code**. Open your email, copy the code, paste it in.
8. When asked about a plan, choose **Free**.

**Write your username here so you don't forget it:** `________________________`

You will type this username dozens of times this week.

---

## 3. Verifying your account and joining the course organization (`keduog`)

### 3a. Verify your email address

Your account is not fully usable until the email is verified. Most people complete this
during signup, but check anyway:

1. Click your **avatar** (top-right corner) → **Settings**
2. In the left menu, click **Emails**
3. Your address should show a green **Verified** label.
4. If it says *Unverified*, click **Resend verification email**, open your inbox, and click the link.

> **Why this matters:** unverified accounts cannot be added to organizations, cannot
> create pull requests in some repositories, and cannot use GitHub Pages. If verification
> is missing, everything later in this session will fail with confusing errors.

### 3b. Enable two-factor authentication (recommended)

1. **Settings** → **Password and authentication**
2. Click **Enable two-factor authentication**
3. Choose an authenticator app (Google Authenticator, Microsoft Authenticator, Authy) and scan the QR code
4. **Save your recovery codes somewhere safe.** If you lose your phone and your recovery codes, your account is unrecoverable.

### 3c. Join the course organization `keduog`

The course materials live in the GitHub organization **`keduog`**.

1. Send your GitHub username to your trainer (or type it in the class chat)
2. The trainer sends an invitation to your email
3. Open the email and click **Join @keduog**, or go directly to <https://github.com/keduog>
4. Once accepted, `keduog` appears under your avatar menu → **Your organizations**

To confirm your membership: go to <https://github.com/keduog> and check that you can see
the course repositories listed. If you get a 404 page, the invitation has not been accepted yet.

> Throughout this README, `keduog/ai-lab-day1` is used as the course repository name.
> If your trainer gives you a different name, substitute it everywhere.

---

## 4. Navigating GitHub — what every button does

Open <https://github.com/keduog/ai-lab-day1> and find each of these.

### The repository page

| What you see | What it does |
|---|---|
| **Code** tab | The files. This is the default view. |
| **Issues** tab | The to-do list / bug tracker for the project |
| **Pull requests** tab | Proposed changes waiting to be reviewed and merged |
| **Actions** tab | Automated jobs that run when code changes (used later in the week) |
| **Settings** tab | Repository options. Only visible if you own the repo. |

### Inside the Code tab

| What you see | What it does |
|---|---|
| Branch selector (says `main`) | Switches between parallel versions of the project |
| **Fork** button (top right) | Makes your own personal copy of somebody else's repository |
| **Star** button | Bookmarks the repo. Purely social — changes nothing. |
| **Watch** button | Sends you notifications when the repo changes |
| Green **`<> Code`** button | Gives you the URL used to download (clone) the repo |
| **Commits** counter (e.g. "42 commits") | Click it to see the full history of every change ever made |
| File list | Click any file to read it. GitHub renders `.md`, `.csv`, `.ipynb` and images nicely. |
| **README.md** shown below the files | GitHub automatically displays the README of every folder. That's why this file exists. |

### Your own profile

Click your avatar → **Your profile**. This page is your public portfolio.
By the end of the week it will show your repositories and a green contribution graph.
This is what your trainer opens to check your progress.

**Exercise (5 minutes):** find and click all of the following:
- the commit history of the course repo
- one individual commit, showing green (added) and red (removed) lines
- the `session2_github_colab/data/soldiers_fitness.csv` file, rendered as a table
- your own profile page

---

## 5. Creating your own repository

1. Click the **`+`** icon (top-right, beside your avatar) → **New repository**
2. Fill in:

   | Field | Value |
   |---|---|
   | Owner | your own username (not `keduog`) |
   | Repository name | `my-first-ai-lab` |
   | Description | `My Day 1 exercises for the AI Lab training.` |
   | Visibility | **Public** — so your trainer can see your work |
   | Add a README file | **ticked** |
   | .gitignore | `Python` |
   | License | leave as *None* for now |

3. Click **Create repository**

You are now looking at `https://github.com/YOUR-USERNAME/my-first-ai-lab`.

> **Why tick "Add a README file"?** A repository with no files is in a strange
> half-created state that is harder to clone. Starting with a README avoids that.

> **Why choose the Python .gitignore?** It tells Git to ignore junk files that Python
> creates (`__pycache__`, `.ipynb_checkpoints`) so they never get committed.

---

## 6. Committing a dataset in the browser

You can edit files on GitHub.com directly, without installing anything. This is the
fastest way to learn what a commit actually is.

1. In **your** `my-first-ai-lab` repository, click **Add file** → **Create new file**
2. In the filename box, type exactly:

   ```
   data/soldiers_fitness.csv
   ```

   The moment you type the `/`, GitHub creates a folder called `data`. That is how folders are made here.

3. Paste this into the large text area:

   ```csv
   id,age,pushups_per_min,run_5km_minutes,fitness_level
   1,22,45,24,high
   2,31,30,29,medium
   3,27,52,22,high
   4,38,18,35,low
   5,25,40,26,medium
   ```

4. Scroll down and click the green **Commit changes...** button
5. In the dialog:
   - **Commit message:** `Add fitness dataset`
   - Leave *Commit directly to the main branch* selected
   - Click **Commit changes**

6. Click the `data` folder, then the CSV file. GitHub displays it as a table.

**You have just made your first commit.** A commit is a saved snapshot plus a message
explaining why. Every AI project in the world — including the ones training models like
PaLM — is built from thousands of these.

### Writing good commit messages

| Good | Bad |
|---|---|
| `Add fitness dataset` | `stuff` |
| `Fix wrong column name in CSV` | `asdf` |
| `Add sentiment analysis notebook` | `update` |
| `Remove unused import` | `changes` |

Rule of thumb: finish the sentence *"If applied, this commit will …"*.

---

## 7. Forking the course repository

A **fork** is your own personal copy of somebody else's repository, stored under your
account. You can change your fork freely without affecting the original.

1. Go to <https://github.com/keduog/ai-lab-day1>
2. Click **Fork** (top right)
3. Owner: your username. Repository name: leave as `ai-lab-day1`. Click **Create fork**
4. You are redirected to `https://github.com/YOUR-USERNAME/ai-lab-day1`

Look under the repository title — it says *forked from keduog/ai-lab-day1*.

### Fork vs. clone — the difference students always mix up

| | Fork | Clone |
|---|---|---|
| Where does the copy live? | On GitHub, under your account | On your own computer |
| Do you need to install anything? | No | Yes — Git |
| Can you push changes back to it? | Yes, it's yours | Yes, to whichever repo you cloned |
| What is it for? | Contributing to a project you don't own | Working on files locally |

Normal order of operations: **fork first, then clone your fork.**

---

## 8. Installing Git and VS Code

### Git

| System | How |
|---|---|
| Windows | Download from <https://git-scm.com/downloads> and run the installer. **Accept every default** — the defaults install Git Bash, which you need. |
| macOS | Open Terminal, type `git --version`, press Enter. macOS offers to install the developer tools. Accept. |
| Linux (Ubuntu) | `sudo apt update && sudo apt install git` |

### VS Code

Download from <https://code.visualstudio.com> and run the installer.

**Windows users:** on the "Select Additional Tasks" screen, tick
**"Add to PATH"** — this is what makes the `code .` command work in section 10.

### Verify both installed

Open a terminal:
- **Windows:** press Start, type `Git Bash`, press Enter
- **macOS:** press Cmd+Space, type `Terminal`, press Enter
- **Linux:** press Ctrl+Alt+T

Type:

```bash
git --version
code --version
```

You should see version numbers, for example `git version 2.43.0`. If you see
*command not found*, see [Troubleshooting](#18-troubleshooting).

### Tell Git who you are (do this once, ever)

Git stamps your name and email onto every commit you make.

```bash
git config --global user.name "Abebe Tesfaye"
git config --global user.email "abebe@example.com"
```

Use **the same email address as your GitHub account**, otherwise your commits will not
be linked to your profile and your contribution graph stays empty.

Check it worked:

```bash
git config --global --list
```

---

## 9. Cloning with the command line

**Cloning** = downloading a full copy of a repository, including its entire history, onto your computer.

### Step 1 — get the URL

On **your fork** (`https://github.com/YOUR-USERNAME/ai-lab-day1`):

1. Click the green **`<> Code`** button
2. Make sure the **HTTPS** tab is selected (not SSH)
3. Click the copy icon

The URL looks like: `https://github.com/YOUR-USERNAME/ai-lab-day1.git`

### Step 2 — choose where it goes

In your terminal:

```bash
cd ~
mkdir ai-lab
cd ai-lab
pwd
```

| Command | What it does |
|---|---|
| `cd ~` | Go to your home folder |
| `mkdir ai-lab` | Make a new folder called `ai-lab` |
| `cd ai-lab` | Go into it |
| `pwd` | Print where you currently are |
| `ls` (`dir` on Windows CMD) | List the files here |

### Step 3 — clone

```bash
git clone https://github.com/YOUR-USERNAME/ai-lab-day1.git
```

Output looks like:

```
Cloning into 'ai-lab-day1'...
remote: Enumerating objects: 47, done.
Receiving objects: 100% (47/47), 12.31 KiB, done.
```

### Step 4 — go inside and look

```bash
cd ai-lab-day1
ls
git status
```

`git status` should say:

```
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

That message means: Git is tracking this folder, you are on the `main` branch, and you
have made no changes yet.

### Step 5 — clone your own repository too

```bash
cd ..
git clone https://github.com/YOUR-USERNAME/my-first-ai-lab.git
ls
```

You now have both projects side by side inside `~/ai-lab/`.

---

## 10. Opening the folder in VS Code with `code .`

From your terminal, inside the repository folder:

```bash
cd ~/ai-lab/my-first-ai-lab
code .
```

**Read that carefully — it is `code`, then a space, then a single dot.**

The dot means "the folder I am currently in". So `code .` means
*"open VS Code, with this folder as the project"*.

VS Code opens with:
- The **Explorer** panel on the left showing `README.md` and `data/`
- The branch name **`main`** in the blue bar at the bottom-left

That blue bar branch name is your proof that VS Code has recognised this as a Git repository.

### Useful variations

```bash
code .                  # open the current folder
code README.md          # open just one file
code ~/ai-lab           # open a folder by path
```

### If `code .` says "command not found"

- **Windows:** you missed the "Add to PATH" tick during install. Re-run the VS Code installer and tick it, then open a **new** terminal window.
- **macOS:** open VS Code, press `Cmd+Shift+P`, type `shell command`, and choose **"Shell Command: Install 'code' command in PATH"**. Then open a new terminal.

### VS Code terminal

You don't need to switch windows. Inside VS Code press:

```
Ctrl + `        (Control and the backtick key, above Tab)
```

A terminal opens at the bottom, already inside your project folder. Every `git` command
in this README can be typed there.

---

## 11. Commit and push from the command line

This is the core loop. Learn it once, use it forever.

### Step 1 — make a change

Inside `my-first-ai-lab`, create a file:

```bash
echo "# My notes from Day 1" > NOTES.md
```

Or just create and edit `NOTES.md` in VS Code and save it.

### Step 2 — see what changed

```bash
git status
```

```
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        NOTES.md
```

**Red** = Git can see the file but is not yet tracking it.

### Step 3 — stage the change

```bash
git add NOTES.md
```

Or stage everything that changed:

```bash
git add .
```

Run `git status` again — `NOTES.md` is now **green**, under *Changes to be committed*.

> **What is staging for?** It lets you choose which changes go into the next commit.
> You might have edited five files but only want to commit two of them.

### Step 4 — commit

```bash
git commit -m "Add personal notes file"
```

```
[main 3f1a9c2] Add personal notes file
 1 file changed, 1 insertion(+)
```

The commit is now saved **on your computer**. GitHub does not know about it yet.

### Step 5 — push

```bash
git push
```

The first time, Git asks you to sign in:

- A browser window opens → click **Authorize**, or
- The terminal asks for a username and password

> **Important:** if it asks for a *password*, your normal GitHub password will **not**
> work. You need a **Personal Access Token**. See [Troubleshooting](#18-troubleshooting).

After a successful push:

```
To https://github.com/YOUR-USERNAME/my-first-ai-lab.git
   a1b2c3d..3f1a9c2  main -> main
```

### Step 6 — verify

Refresh your repository page on GitHub. `NOTES.md` is there.

### The loop, summarised

```bash
git status      # what changed?
git add .       # stage everything
git commit -m "clear message"
git push        # upload to GitHub
```

And when someone else has changed the repo:

```bash
git pull        # download their changes first
```

> **Golden rule: `git pull` before you start work, `git push` when you finish.**

---

## 12. Commit and push from the VS Code interface

Everything in section 11, without typing commands.

1. Edit any file in VS Code and save it (`Ctrl+S`)
2. Click the **Source Control** icon in the left bar (branch symbol, third icon down). It shows a blue badge with the number of changed files.
3. Your changed files are listed under **Changes**
4. Hover over a file and click **`+`** to stage it (this is `git add`)
5. Type your commit message in the box at the top
6. Click **✓ Commit** (this is `git commit`)
7. Click **Sync Changes** (this is `git pull` followed by `git push`)

### Which should you use?

| | Command line | VS Code interface |
|---|---|---|
| Speed once learned | Faster | Slower |
| Easy to start with | Harder | Easier |
| Works everywhere (servers, cloud) | Yes | No |
| Shows you exactly what changed | With `git diff` | Click a file to see it side by side |

**Learn both.** Use the VS Code interface day to day; use the command line when you are
on a remote server or when something goes wrong.

---

## 13. Branching and merging

A **branch** is a parallel version of your project. You experiment on a branch; if it
works, you merge it into `main`; if it doesn't, you delete it and `main` was never touched.

### Create a branch and switch to it

```bash
git switch -c add-readme-section
```

(Older tutorials use `git checkout -b add-readme-section` — same thing.)

Check where you are:

```bash
git branch
```

```
  main
* add-readme-section
```

The `*` shows your current branch. VS Code's bottom-left bar also updates.

### Work on the branch

Edit `README.md` — add a line like `## About me`. Then:

```bash
git add .
git commit -m "Add About me section to README"
```

### Merge it back into main

```bash
git switch main          # go back to main
git merge add-readme-section
```

```
Updating a1b2c3d..7d8e9f0
Fast-forward
 README.md | 2 ++
```

**Fast-forward** means `main` had not changed while you were away, so Git simply moved
the pointer forward. This is the clean, common case.

### Push and tidy up

```bash
git push
git branch -d add-readme-section
```

### If a merge conflict happens

A conflict occurs when the same lines were changed in both branches. Git marks the file:

```
<<<<<<< HEAD
Text that is currently on main
=======
Text from your branch
>>>>>>> add-readme-section
```

To fix it:

1. Open the file in VS Code — it highlights conflicts and offers buttons:
   **Accept Current Change** / **Accept Incoming Change** / **Accept Both Changes**
2. Choose what the file should actually say, and delete all the `<<<<<<<`, `=======`, `>>>>>>>` marker lines
3. Save, then:

```bash
git add .
git commit -m "Resolve merge conflict in README"
git push
```

Conflicts are normal. They are not a sign you did something wrong.

---

## 14. Pull requests — merging through GitHub

On a real team you rarely merge into `main` yourself. You open a **pull request** so
someone reviews your work first.

### Try it on your own repository

```bash
git switch -c my-first-pull-request
echo "Learning pull requests." >> NOTES.md
git add .
git commit -m "Add note about pull requests"
git push -u origin my-first-pull-request
```

> `-u origin branch-name` is needed the **first** time you push a new branch. It tells
> Git where this branch lives on GitHub. After that, plain `git push` works.

Now on GitHub:

1. Open your repository — a yellow banner appears: *"my-first-pull-request had recent pushes"*
2. Click **Compare & pull request**
3. Give it a title and a short description explaining what you changed and why
4. Click **Create pull request**
5. Click the **Files changed** tab — this is what a reviewer sees: green additions, red deletions
6. Click **Merge pull request** → **Confirm merge**
7. Click **Delete branch** (the branch has served its purpose)

Back on your computer:

```bash
git switch main
git pull
```

Your merged change is now in your local `main`. **The cycle is complete.**

### Contributing back to the course repo

To submit work to `keduog/ai-lab-day1`, the flow is:

```
fork  →  clone your fork  →  branch  →  commit  →  push to your fork  →  pull request to keduog
```

When you open the pull request, check that the **base repository** is `keduog/ai-lab-day1`
and the **head repository** is your fork.

---

## 15. Running the code in Google Colab

You do not need Python installed to run the notebooks. Colab runs them on Google's
computers, for free.

### Method 1 — open a notebook straight from GitHub (recommended)

1. Go to <https://colab.research.google.com>
2. Sign in with a Google account
3. **File** → **Open notebook** → **GitHub** tab
4. Paste: `keduog/ai-lab-day1`
5. Click the search icon, then click `session2_github_colab/session2_starter.ipynb`

### Method 2 — the direct URL

Any GitHub notebook can be opened by putting this in front of its path:

```
https://colab.research.google.com/github/keduog/ai-lab-day1/blob/main/session2_github_colab/session2_starter.ipynb
```

### Running cells

| Action | How |
|---|---|
| Run one cell | Click it, press **Shift+Enter** |
| Run every cell | **Runtime** → **Run all** |
| Stop a running cell | Click the ■ stop button |
| Start completely fresh | **Runtime** → **Restart session** |

The first cell takes a few seconds while Colab connects you to a machine. That is normal.

### Getting a free GPU

**Runtime** → **Change runtime type** → **T4 GPU** → **Save**

The session restarts. Re-run your cells. To confirm you have a GPU, run:

```python
!nvidia-smi
```

This is the same idea that AWS and Azure sell at industrial scale (Days 2 and 3) —
you just used it for free.

### Saving your work back to GitHub

**File** → **Save a copy in GitHub**

- Repository: `YOUR-USERNAME/my-first-ai-lab`
- File path: `session2_starter.ipynb`
- Commit message: `Add Session 2 starter notebook`

Tick **"Include a link to Colab"** so you can reopen it in one click.

> **Warning:** Colab notebooks are **not** saved to GitHub automatically. If you close
> the tab without doing the step above, your work is gone. Save to GitHub at the end of
> every lab.

---

## 16. Files in this folder

| File | What it is | How to run it |
|---|---|---|
| `README.md` | This guide | Read it |
| `session2_starter.ipynb` | The main Session 2 notebook | Open in Colab (section 15) |
| `hello_colab.py` | Simplest possible script — checks your setup | `python hello_colab.py` |
| `explore_dataset.py` | Loads the CSV and prints summary statistics | `python explore_dataset.py` |
| `git_practice.sh` | The whole command-line workflow as one commented script | Read it; run commands one by one |
| `data/soldiers_fitness.csv` | The practice dataset (15 rows) | Loaded by the scripts above |

### Running the Python scripts locally

You need Python installed for these. If you don't have it yet, skip them —
the notebook does the same things in Colab.

```bash
cd ~/ai-lab/ai-lab-day1/session2_github_colab
pip install pandas
python hello_colab.py
python explore_dataset.py
```

---

## 17. Git command cheat sheet

### Setup — once per computer

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global --list
```

### Starting work

```bash
git clone <url>          # download a repository
cd <folder>              # go into it
code .                   # open it in VS Code
git pull                 # get the latest changes before you start
```

### The daily loop

```bash
git status               # what has changed?
git add .                # stage all changes
git add file.py          # or stage just one file
git commit -m "message"  # save a snapshot
git push                 # upload to GitHub
```

### Branches

```bash
git branch                       # list branches
git switch -c new-branch         # create and switch to a branch
git switch main                  # switch back to main
git merge new-branch             # merge a branch into the current one
git branch -d new-branch         # delete a merged branch
git push -u origin new-branch    # first push of a new branch
```

### Looking around

```bash
git log --oneline        # compact history
git log --oneline -5     # last 5 commits
git diff                 # what changed but isn't staged yet
git diff --staged        # what is staged and about to be committed
git remote -v            # which GitHub repo am I connected to?
```

### Undoing things

```bash
git restore file.py              # throw away changes to one file
git restore --staged file.py     # unstage a file (keep the changes)
git commit --amend -m "better"   # fix the last commit message (before pushing)
git revert <commit-hash>         # undo a commit by making a new one
```

> Avoid `git reset --hard` until you are confident. It permanently deletes work.

---

## 18. Troubleshooting

**`git: command not found`**
Git isn't installed, or your terminal was open before you installed it.
Close the terminal, open a new one, try again. If it persists, reinstall Git.

**`code: command not found`**
See section 10. On Windows, re-run the VS Code installer and tick *Add to PATH*.
On macOS, use `Cmd+Shift+P` → *Shell Command: Install 'code' command in PATH*.
Always open a **new** terminal afterwards.

**`Support for password authentication was removed`**
GitHub no longer accepts your account password on the command line. Use a token:

1. GitHub → avatar → **Settings** → **Developer settings** (very bottom of the left menu)
2. **Personal access tokens** → **Tokens (classic)** → **Generate new token (classic)**
3. Note: `AI Lab training`. Expiration: 90 days. Tick the **`repo`** scope.
4. **Generate token** and **copy it immediately** — you cannot see it again
5. When Git asks for a password, paste the **token** instead

**`fatal: repository not found`**
Usually a typo in the URL, or the repo is private and you're not a member.
Check your `keduog` membership (section 3c). Verify the URL with `git remote -v`.

**`Please tell me who you are`**
You skipped the `git config` step in section 8.

**`Updates were rejected because the remote contains work that you do not have`**
Someone pushed changes before you. Fix:

```bash
git pull
git push
```

**`Permission denied (publickey)`**
You cloned with an SSH URL but have no SSH key set up. Easiest fix — switch to HTTPS:

```bash
git remote set-url origin https://github.com/YOUR-USERNAME/my-first-ai-lab.git
```

**Colab: `FileNotFoundError` when loading the CSV**
Colab runs on Google's machine, not yours, so your local files don't exist there.
Load the CSV from its GitHub **raw** URL instead — the notebook shows how.

**Colab: my code disappeared**
You closed the tab without saving. Always use **File → Save a copy in GitHub**.

**VS Code doesn't show a branch name at the bottom**
You opened a plain folder, not a cloned repository. Make sure you ran `code .`
from inside the folder that `git clone` created.

---

## 19. Checklist before you leave

- [ ] GitHub account created and email shows **Verified**
- [ ] Two-factor authentication enabled (recommended)
- [ ] Member of the `keduog` organization
- [ ] I can find the Code, Issues, Pull requests and Settings tabs
- [ ] My repository `my-first-ai-lab` exists and is **Public**
- [ ] `data/soldiers_fitness.csv` is committed and displays as a table
- [ ] I forked `keduog/ai-lab-day1`
- [ ] `git --version` and `code --version` both work
- [ ] `git config --global user.name` and `user.email` are set
- [ ] I cloned a repository with `git clone`
- [ ] I opened it with `code .`
- [ ] I committed and pushed from the **command line**
- [ ] I committed and pushed from the **VS Code interface**
- [ ] I created a branch, merged it, and deleted it
- [ ] I opened and merged a pull request
- [ ] I ran `session2_starter.ipynb` in Colab and switched to a GPU runtime
- [ ] I saved the notebook back to my GitHub repository

---

**Next:** [Session 3 — Hugging Face](../session3_huggingface/README.md)
