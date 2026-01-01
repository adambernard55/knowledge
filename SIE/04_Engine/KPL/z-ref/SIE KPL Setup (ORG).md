# Obsidian to GitHub to WordPress Workflow Setup

## Prerequisites ✅
- Obsidian installed with Git plugin
- GitHub Desktop installed
- GitHub account active
- WordPress site with custom post type configured

## Step 1: Connect GitHub - Multi-Repository Setup

### 1.1 Create Repositories for Each Publishing Folder

1. **In GitHub (web interface):**
   - Create separate repositories for each subfolder you want to publish
   - Example structure:
     - `my-blog-posts` (for /Blog folder)
     - `my-tutorials` (for /Tutorials folder)
     - `my-notes-public` (for /Public Notes folder)

2. **Repository Settings:**
   - Make repositories public or private as needed
   - Initialize with README (optional)
   - Choose appropriate license if public

### 1.2 Clone Repositories Locally

1. **Open GitHub Desktop**
2. **For each repository:**
   - Click "Clone a repository from the Internet"
   - Select your repository
   - Choose a local path **outside** your Obsidian vault initially
   - Example paths:
     - `C:\Git-Repos\my-blog-posts`
     - `C:\Git-Repos\my-tutorials`

### 1.3 Set Up Obsidian Vault Folder Connections

**Option A: Symbolic Links (Recommended)**
1. **Create symbolic links** from your Obsidian subfolders to the Git repositories:
   ```cmd
   mklink /D "C:\Path\To\Obsidian\Vault\Blog" "C:\Git-Repos\my-blog-posts"
   mklink /D "C:\Path\To\Obsidian\Vault\Tutorials" "C:\Git-Repos\my-tutorials"
   ```

**Option B: Separate Git Initialization**
1. **Navigate to each Obsidian subfolder** you want to publish
2. **Initialize Git in each subfolder:**
   ```bash
   cd "C:\Path\To\Obsidian\Vault\Blog"
   git init
   git remote add origin https://github.com/yourusername/my-blog-posts.git
   ```

### 1.4 Configure Obsidian Git Plugin for Multi-Repo

1. **Open Obsidian Settings → Community Plugins → Git**
2. **Key Settings:**
   - **Vault backup interval**: Set to 0 (disable auto-backup for main vault)
   - **Auto pull interval**: Set to 0 
   - **Disable push**: Enable (we'll handle this per folder)

3. **For each publishing folder, create a separate Git configuration:**
   - Use the Git plugin's folder-specific settings if available
   - Or use command palette for manual commits per folder


> [!## Fix the "Git Not Ready" Issue First:

You need to initialize Git in your Obsidian vault root before the plugin settings will appear.

### Quick Setup:

1. **Find your Obsidian vault folder path:**
    
    - In Obsidian: Settings → About → Vault path
    - Copy this path
2. **Open Terminal/Command Prompt as Administrator:**
    
    - Windows: `Win + R`, type `cmd`, press `Ctrl + Shift + Enter`
    - Mac: Applications → Utilities → Terminal
3. **Navigate to your vault and initialize Git:**
    
    ```bash
    cd "C:\Your\Obsidian\Vault\Path"
    git init
    git config user.name "Your Name"
    git config user.email "your.email@example.com"
    ```
    
4. **Create initial commit:**
    
    ```bash
    echo "# My Obsidian Vault" > README.md
    git add README.md
    git commit -m "Initial setup"
    ```
    
5. **Restart Obsidian**
    

## After This Setup:

- The **"Git Not Ready"** message should disappear
- You'll see all the Git plugin settings I mentioned earlier
- You can then configure the automatic backup settings as planned in your [SIE Knowledge Pipeline Setup](obsidian://open?file=SIE%2F04_Knowledge%2FSIE%20Knowledge%20Pipeline%20Setup.md)] Title
> Contents

---

### 1.5 Test the Connection

1. **Create a test file** in one of your publishing folders
2. **In GitHub Desktop:**
   - Switch to the appropriate repository
   - You should see the new file in "Changes"
   - Add a commit message
   - Commit and push

3. **Verify on GitHub** that the file appears in the web interface

## Next Steps Preview

- Step 2: Configure WordPress Integration
- Step 3: Set up Automated Publishing Triggers
- Step 4: Configure Content Formatting and Metadata
- Step 5: Test Complete Workflow

---

**Notes for Documentation:**
- Record your specific folder paths and repository names
- Save GitHub repository URLs for easy reference
- Document any custom naming conventions you're using




