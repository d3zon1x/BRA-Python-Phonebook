
# 🔧 How to Work with Our Project on GitHub

Welcome! 

Here's a step-by-step guide to help you work with our shared project using GitHub. 
Even if you're new to coding, this will walk you through everything.

## Pure git instructions
### 1. 🍴 Fork the Main Repository
* **What:** Make your own copy of the project.
* **Why:** So you can safely make changes without breaking the original code.
* **How:**  
1. Go to the main project page on GitHub.  
2. Click the `Fork` button in the top-right corner.  
3. GitHub will create a copy in your account.


### 2. ©️ Clone Your Fork to Your Computer
* **What:** Download your GitHub project copy to your computer.
* **Why:** So you can edit the code using your own tools.
* **How:**  
1. On your fork page, click the `Code` button.  
2. Copy the link that ends with `.git`.  
3. Open a terminal or Git Bash.  
4. Type: `git clone YOUR_LINK_HERE`  
5. Press Enter.



## 3. 🌳 Go to the Right Branch `PYnnn`
* **What:** Switch to the correct version of the project.
* **Why:** All students work in the `PYnnn` branch.
* **How:**  
1. In terminal, go to the folder:  
   `cd YOUR_PROJECT_FOLDER`  
2. Type:  
   `git checkout PYnnn`


### 4. 🔶 Create a New Branch for Your Work
* **What:** Create your own branch to work on.
* **Why:** Keeps your changes organized and separate.
* **How:**  
1. Type:  
   `git checkout -b yourname-task`  
   Example: `git checkout -b anna-levels`


### 5. 📝 Make Your Changes
* **What:** Edit or add files to complete your task.
* **Why:** This is where you actually work on the code.
* **How:**  
- Use any editor like VS Code, Roblox Studio, or Notepad++  
- Make small, clear changes


### 6. 💾 Save and Commit Your Changes
* **What:** Tell Git to remember your changes.
* **Why:** So your progress is saved with a message.
* **How:**  
1. Type:  
   `git add .`
   - Make sure that you don't commit cache files: 
     `git status`
2. Then:  
   `git commit -m "What you did"`  
   Example: `git commit -m "Added player jump animation"`


### 7. 📌 Push Your Branch to GitHub
* **What:** Send your work to GitHub.
* **Why:** So the teacher can see your changes.
* **How:**  
1. Type:  
   `git push origin yourname-task`


### 8. 🙋‍♂️ Make a Pull Request (PR)
* **What:** Ask to add your changes into the main project.
* **Why:** So your code can be reviewed and approved.
* **How:**  
1. Go to your fork on GitHub.  
2. Click `Compare & pull request`.  
3. Make sure:  
   - **Base repository** = teacher’s repo  
   - **Base branch** = `PYnnn`
   - **Head repository** = your repo  
   - **Compare branch** = your branch  
4. Click `Create pull request`.  
5. Write what you did and click `Submit`.


### 9. 🔄 Keep Your Fork Updated
* **What:** Get the latest changes from the teacher’s project.
* **Why:** To avoid conflicts and stay up to date.
* **How (do this regularly):**  
1. Add teacher's repo as a remote (do once):  
   `git remote add upstream https://github.com/TEACHER_USERNAME/REPO_NAME.git`  
2. Get updates:  
   `git fetch upstream`  
3. Switch to `PYnnn`:  
   `git checkout PYnnn`  
4. Merge changes:  
   `git merge upstream/PYnnn`  
5. Push to your fork:  
   `git push origin PYnnn`


### 10. Repeat Steps 4–8 for Every Task
**Always:**  
- Create a new branch  
- Work  
- Commit  
- Push  
- Make a pull request

---

### 🙈 Using .gitignore

* **What:** A `.gitignore` file tells Git which files or folders it should **not** track.
* **Why:** Some files should stay on your computer and never be uploaded to GitHub, for example:
- Secret passwords or API keys
- Temporary files from editors (like `.idea` from PyCharm)
- Build or output files
- Log files, caches, or auto-generated content

#### 📄 How to Create or Edit .gitignore

1. In the root of your project folder, create a file named:  
   `.gitignore`

2. Add file and folder patterns to ignore. For example:

   - Ignore Python cache and compiled files:  
     `__pycache__/`  
     `*.pyc`  

   - Ignore PyCharm project files:  
     `.idea/`  

   - Ignore secret environment files:  
     `.env`  

   - Ignore Roblox Studio autosaves:  
     `*.rbxl.autosave`  

#### 🔄 When Does .gitignore Work?

- It only works **for files that are not already tracked** by Git.
- If a file is already committed, adding it to `.gitignore` won’t remove it from Git history.

#### 🧹 How to Stop Tracking a File You Already Added

If you added a file by mistake and want Git to forget it but keep it on your computer:

1. Untrack the file:  
   `git rm --cached filename`  

   Example:  
   `git rm --cached .env`  

2. Commit the change:  
   `git commit -m "Removed tracked file .env"`  

Now Git will ignore it if it’s listed in `.gitignore`.


#### 💡 Pro Tips

- Use `*.ext` to ignore all files with a given extension.
- Use `foldername/` to ignore a folder and all its contents.
- Use `!important.txt` to *not* ignore a specific file inside an ignored folder.

📌 Always include a correct `.gitignore` in your repository. It helps keep your commits clean and avoids uploading sensitive or useless files.

---

### ✅ Troubleshooting Git/GitHub

- ❗ **I accidentally committed to the wrong branch**  
  Don’t panic. You can:  
      1. 📋 Copy your changed files somewhere safe outside the project folder.  
      2. 🔀 Switch to the correct branch with `git checkout correct-branch`.  
      3. 📂 Paste the files back.  
      4. 💾 Add, commit, and push your changes again.


- ⚠️ **Git says there are conflicts when I merge or pull**  
  This means your copy and the main project changed the same lines. To fix:  
      1. 🔍 Read the conflicting files carefully; conflict sections are marked with `<<<<<<` and `>>>>>>`.  
      2. 🤔 Decide which changes to keep or how to combine them.  
      3. ✍️ Edit the file to remove conflict markers and make the code correct.  
      4. 💾 Save the file.  
      5. ➕ Run `git add FILENAME` for each fixed file.  
      6. ✅ Finish merge with `git commit`.  
      7. ❓ If unsure, ask the teacher before proceeding.


- 🚫 **My pull request can’t be merged automatically**  
  This usually means your branch is out of date. To fix:  
      1. 🔄 Update your fork with the latest changes from the main repo (see “Keep Your Fork Updated” step).  
      2. 🔀 Merge those updates into your branch:  
     `git checkout your-branch`  
      3. ⚔️ Fix any conflicts (see above).  
      4. 🚀 Push the updated branch: `git push origin your-branch`.  
      5. 🔄 The pull request should update automatically.


- ❌ **I forgot to add some files before committing**  
  You can add them now:  
      1. ➕ Use `git add missing-file`.  
      2. 📝 Then commit with `git commit --amend` to add them to the last commit.  
      3. ⚠️ Push with `git push --force origin your-branch` (careful: force push overwrites the remote history).


- 🗑️ **I accidentally added the wrong files before committing**  
  Sometimes you do `git add .` and it includes files you didn’t want. 
  No problem. To unstage (remove from the commit list) before committing:  
        1. 🧹 See what’s staged:  
           `git status`  
        2. 🚫 Unstage a file (remove it from the next commit, but keep the file):  
           `git restore --staged filename`  
           `git restore --staged secret_config.txt`  
        3. ✅ Now commit only the files you want:  
           `git commit -m "Added correct files only"`
   
  🔒 This does not delete the file from your computer — just tells Git not to include it in the commit.


- 🔙 **I made a mistake and wanted to undo my last commit**  
  If you haven’t pushed yet:  
  - ↩️ Run `git reset HEAD~1` to undo the last commit but keep your changes.  
  If you already pushed, ask the teacher before trying to undo history.


- 🤷‍♂️ **I’m stuck or don’t understand git error messages**  
  Copy the error message and ask Google/AI/classmates/the teacher for help. Don’t guess blindly.

---

## 🛠️ Working with GitHub in PyCharm

PyCharm can help you work with Git and GitHub more easily using its built-in tools.

### 1. 🔄 Clone the Repository in PyCharm
* **What:** Download the project to your computer directly from PyCharm.
* **Why:** You don’t need to use the terminal if you prefer a graphical interface.
* **How:**  
1. Open PyCharm.  
2. Click `Get from Version Control` on the welcome screen (or use `VCS > Get from Version Control` if a project is open).  
3. Paste the URL of your forked repository (ends with `.git`).  
4. Choose a folder to save the project and click `Clone`.


### 2. 🔀 Switch to the PYnnn Branch
* **What:** Make sure you are working on the correct project branch.
* **Why:** All group work happens in branch `PYnnn`.
* **How:**  
1. At the bottom-right corner of PyCharm, click the branch name.  
2. Select `PYnnn` from the list.  
3. If you don’t see it, click `Remote Branches` and check out `origin/PYnnn`.

### 3. ➕ Create a New Branch for Your Work
* **What:** Make a separate branch to keep your changes organized.
* **Why:** Avoid mixing your work with others and keep code clean.
* **How:**  
1. Click the branch name again.  
2. Choose `New Branch`.  
3. Enter your branch name like `yourname-task` (example: `anna-levels`).  
4. Click `Create`.

### 4. 💻 Make and Save Changes
* **What:** Edit files in PyCharm using its editor.
* **Why:** PyCharm provides helpful code completion and error checking.
* **How:**  
- Open files and start editing.  
- Save your work (Ctrl+S or File > Save All).


### 5. ✅ Commit Your Changes
* **What:** Tell Git to record your changes with a message.
* **Why:** Keeps track of your progress and what you changed.
* **How:**  
1. Open the `Git` tool window (View > Tool Windows > Git).  
2. Click the `Commit` button.  
3. Write a clear commit message (e.g., “Added player jump animation”).  
4. Check the files you want to commit.  
5. Click `Commit` or `Commit and Push` to send changes directly to GitHub.


### 6. 🚀 Push Your Branch to GitHub
* **What:** Upload your commits so others can see your work.
* **Why:** Necessary for creating pull requests.
* **How:**  
- If you didn’t push during commit, click `Git > Push` or click the ↑ arrow in the Git window.  
- Confirm the branch and push.


### 7. 🔄 Pull Changes from Upstream
* **What:** Update your local project with the latest changes from the main repository.
* **Why:** Prevents conflicts and keeps your code current.
* **How:**  
1. Add upstream remote once (in terminal or PyCharm terminal):  
   `git remote add upstream https://github.com/TEACHER_USERNAME/REPO_NAME.git`  
2. To fetch and merge updates:  
   - Use terminal:  
     `git fetch upstream`  
     `git checkout PYnnn`  
     `git merge upstream/PYnnn`  
   - Or use PyCharm’s VCS > Git > Fetch and Merge.


### 8. 🔀 Make a Pull Request on GitHub from PyCharm
After pushing your branch, go to GitHub to create a Pull Request as explained in the main instructions.
Or, you can create a pull request (PR) directly from PyCharm — if it’s correctly set up.

#### ✅ Requirements

- You are using **PyCharm Professional** (free for students/teachers)  
  OR the **Community Edition** with GitHub connected
- You already **pushed your branch to GitHub**
- You connected your GitHub account in PyCharm (`File > Settings > Version Control > GitHub`)

#### 📌 Steps to Create a Pull Request

1. Make sure your branch is pushed:  
   Go to `VCS > Git > Push`  
   or click the ↑ icon in the top-right corner

2. Open the Git Log:  
   Go to `View > Tool Windows > Git`  
   Click the `Log` tab to see your commits

3. Right-click your latest commit  
   Choose `Create Pull Request` (only available if properly configured)

4. Fill in the pull request form:  
   - **Target branch** → PY133  
   - **Source branch** → your branch  
   - **Base repo** → teacher’s repo  
   - **Head repo** → your fork  
   - Add title and description  
   - Click `Submit`

#### 🧭 If You Don’t See “Create Pull Request” Option

That’s common in the Community Edition. Do this instead:

1. Push your branch in PyCharm  
2. Go to your repository on GitHub in your browser  
3. Click `Compare & pull request` (GitHub usually suggests it)  
4. Make sure base = PY133 and head = your branch  
5. Write your description and click `Create pull request`

#### 💡 Tips

- PR = asking to merge your changes into the main project
- You only create PRs **after pushing your branch**
- If anything is unclear, ask the teacher before submitting

---

Happy coding! 💻  



