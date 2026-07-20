# Session 4 — GitHub Copilot & Your Personal Website

**Day 1 · 15:30 – 16:30**

In this session you will describe a website in plain English, let AI write it, look at it
in your browser, and publish it on the internet.

---

## 1. What is GitHub Copilot?

**Copilot** is an AI assistant that lives inside VS Code and writes code for you.

- You describe what you want in **normal language** — English, no programming needed
- Copilot writes the code
- You read it, ask for changes, and accept it

It is free to start. Students and teachers get the paid version free at
<https://education.github.com>.

---

## 2. Install Copilot in VS Code

1. Open **VS Code**
2. Click the **Extensions** icon in the left bar (it looks like four squares)
3. Search for **GitHub Copilot**
4. Click **Install**
5. When it asks, click **Sign in with GitHub** — a browser opens, click **Authorize**,
   then go back to VS Code

**Check it worked:** the Copilot icon appears in the bottom-right corner with no red
warning mark.

### Open the chat

Press **`Ctrl + Alt + I`** (Mac: `Cmd + Alt + I`), or click the chat icon at the top.

At the top of the chat panel there is a dropdown. Choose **Agent**.
This is what lets Copilot create files for you.

---

## 3. Open your repository

Use the folder you cloned in Session 2.

In VS Code: **File → Open Folder…** → select your `EDU-AI-Training` folder.

Check the bottom-left corner shows **`main`**.

---

## 4. Write the prompt

Paste this into the Copilot chat. **Change the name and details to yours.**

```
Create a personal website in one file called index.html.
It is for <your name>, an instructor at Ethiopian Defense University.
Include a header with my name and title, an About Me section,
a Skills section listing Python, GitHub and AI, and a Contact section
with my email abebe@example.com.
Use a clean modern design with a dark blue color scheme.
Put all the CSS inside the same file. No JavaScript frameworks.
```

Press **Enter**. Copilot writes the file in front of you.

### Why this prompt works

| It says | Why that matters |
|---|---|
| "one file called index.html" | Copilot knows exactly what to create |
| "for Abebe Tesfaye, an instructor at…" | It knows who it is for |
| "About Me, Skills, Contact" | It knows what to put inside |
| "dark blue, CSS inside, no frameworks" | It knows the rules to follow |

Compare with a bad prompt: **`make me a website`** — Copilot has to guess everything,
and you will not like the result.

### Read it, then accept

Look at the code for a minute. Is your name correct? Are all the sections there?

Then click **Keep** or **Accept** so the file is saved.

### Ask for changes

Keep talking to it in the same chat:

```
Change the color scheme to dark green.
```
```
Add a section listing three projects.
```
```
Make it look good on a mobile phone.
```

Each message updates the file. This back-and-forth is normal — nobody gets it right in
one try.

---

## 5. See the website in your local browser

**Step 1.** In the VS Code Explorer (left panel), find **`index.html`**

**Step 2.** Right-click it

**Step 3.** Choose **Reveal in File Explorer** (Windows) or **Reveal in Finder** (Mac)

**Step 4.** A folder window opens with the file highlighted. **Double-click `index.html`**

**Step 5.** Your website opens in your browser. **This is your website, running on your
own computer.**

### Try changing something

1. Go back to VS Code
2. Change a heading, or ask Copilot to change a colour
3. Press **Ctrl + S** to save
4. Go to the browser and press **F5** to refresh
5. The change appears

This is how every web developer works: edit, save, refresh.

---

## 6. Push the website to GitHub

1. In VS Code, click the **Source Control** icon in the left bar
2. `index.html` appears under **Changes**
3. Type a message: `Add my personal website`
4. Click **✓ Commit** (if it asks to stage all changes, click **Yes**)
5. Click **Sync Changes**

Now open `https://github.com/YOUR-USERNAME/EDU-AI-Training` in your browser and refresh.

**`index.html` is there.**

---

## 7. Publish it on the internet

This makes your website a real, public web page that anyone can open.

1. In your repository on GitHub, click **Settings** (top of the page)
2. In the left menu, click **Pages**
3. Under *Source*, choose **Deploy from a branch**
4. Branch: **`main`** · Folder: **`/ (root)`**
5. Click **Save**
6. Wait about one minute, then refresh the page

Your website address appears at the top:

```
https://YOUR-USERNAME.github.io/EDU-AI-Training/
```

Open it on your phone. Send the link to a friend.

> If `index.html` is inside a folder (like `Day1/`), the address includes that folder:
> `https://YOUR-USERNAME.github.io/EDU-AI-Training/Day1/`
>
> To keep it simple, put `index.html` in the top level of the repository.

---

## What you just did

```
Plain English sentence
        |
   GitHub Copilot writes the code
        |
   You look at it in your browser
        |
   Commit and push to GitHub
        |
   A live website on the internet
```

All of it in one hour, without writing a single line of HTML yourself.

---

## If something goes wrong

**Copilot says "not signed in"**
Click the Copilot icon in the bottom bar and sign in again.

**Copilot only talks, it does not create the file**
You are in *Ask* mode. Change the dropdown at the top of the chat to **Agent**.

**"You have exceeded your free request limit"**
Work in pairs on one computer, and apply for the free student plan at
<https://education.github.com>.

**The website looks broken**
Tell Copilot exactly what is wrong: *"the sections overlap each other, fix the layout"*.

**GitHub Pages shows a 404**
- The file must be named exactly `index.html`, all lowercase
- Wait a full minute after saving the settings
- The repository must be **Public**

---

## Checklist

- [ ] Copilot is installed in VS Code and signed in
- [ ] The chat is in **Agent** mode
- [ ] I wrote a prompt and Copilot created `index.html`
- [ ] I asked for at least one change
- [ ] I opened the website in my own browser
- [ ] I committed and pushed it to GitHub
- [ ] I turned on GitHub Pages and my website is live
