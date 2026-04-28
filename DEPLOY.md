# Deployment Guide — mohcinemadkour.github.io

## One-Time GitHub Setup

### Step 1: Create the repository

Go to https://github.com/new and create a repo named exactly:

```
mohcinemadkour.github.io
```

(This special name triggers GitHub Pages automatically for your username.)

### Step 2: Enable GitHub Actions deployment

1. In the repo → **Settings** → **Pages**
2. Under **Source**, select **GitHub Actions**
3. Save

### Step 3: Push the site files

```bash
# Clone your new empty repo
git clone https://github.com/mohcinemadkour/mohcinemadkour.github.io.git
cd mohcinemadkour.github.io

# Copy all files from the zip into this directory
# (unzip the provided mohcine-website.zip here)

# Add your profile photo
cp /path/to/your/photo.jpg assets/img/prof_pic.jpg

# Add your CV PDF
cp /path/to/your/CV.pdf assets/pdf/Mohcine_Madkour_CV.pdf

# Commit and push
git add .
git commit -m "Initial site launch"
git push origin main
```

### Step 4: Watch the build

Go to **Actions** tab in your repo → you'll see the "Deploy Jekyll site to Pages" workflow run.
Build takes ~2–3 minutes. Your site will be live at:

```
https://mohcinemadkour.github.io
```

---

## Local Development

```bash
# Install Ruby (if not already installed)
# macOS: brew install ruby
# Ubuntu: sudo apt-get install ruby-full

# Install bundler
gem install bundler

# Install dependencies
cd mohcinemadkour.github.io
bundle install

# Serve locally with live reload
bundle exec jekyll serve --livereload

# Open http://localhost:4000
```

---

## Adding Your Profile Photo

Drop any photo named `prof_pic.jpg` into `assets/img/`:

```bash
cp ~/your-photo.jpg assets/img/prof_pic.jpg
git add assets/img/prof_pic.jpg
git commit -m "Add profile photo"
git push
```

---

## Quick Content Edits

| What to change    | Where                                          |
| ----------------- | ---------------------------------------------- |
| Bio text          | `_pages/about.md` (bottom section after `---`) |
| Social links      | `_data/socials.yml`                            |
| Google Scholar ID | `_data/socials.yml` → `scholar_userid`         |
| CV PDF link       | `_data/socials.yml` → `cv_pdf`                 |
| News items        | `_news/announcement_*.md`                      |
| CV data           | `_data/cv.yml`                                 |
| New project       | New file in `_projects/`                       |
| New blog post     | New file in `_posts/YYYY-MM-DD-title.md`       |
| New talk          | New file in `_talks/`                          |
| New teaching      | New file in `_teachings/`                      |

---

## Troubleshooting

**Build fails with gem errors:**

```bash
bundle update
git add Gemfile.lock
git commit -m "Update Gemfile.lock"
git push
```

**Page not found after deploy:**

- Check Settings → Pages → Source is set to "GitHub Actions" (not "Deploy from a branch")

**Profile image not showing:**

- Make sure the file is named exactly `prof_pic.jpg` in `assets/img/`
