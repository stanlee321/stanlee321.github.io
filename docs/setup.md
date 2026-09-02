# Setup — publishing this site

How to get this repo onto GitHub Pages, and the deferred custom-domain steps.
Not built (`docs/` is excluded).

**All of this is Stanley's to execute.** The maintainer agent does not create
repos, change repo settings, commit, or push. It prepares; he presses the
buttons.

---

## 1. Current state

- Local repo: `stanlee321.github.io`, branch `main`, **zero commits**, no remote.
- No Jekyll build has ever been run locally (no local Jekyll, Docker down).
  Verification so far is structural only. The GitHub Pages build will be the
  first real build — expect to fix something on the first try.

---

## 2. First publish

### 2.1 The repository name matters

For a GitHub **user site** served at `https://stanlee321.github.io` with no path
prefix, the repository must be named exactly:

```
stanlee321.github.io
```

That exact name is what makes it a user site. A differently-named repo would be
a *project* site at `https://stanlee321.github.io/<repo>/`, which would require
setting `baseurl` in `_config.yml` — currently `baseurl: ""`, correct for a user
site. Do not rename without changing `baseurl` to match.

> Note: the existing `stanlee321/stanlee321` repo is a **different** repo — it is
> the GitHub *profile* repo, whose `README.md` renders on Stanley's profile
> page. It is not this site. See §5.

### 2.2 Commit and push

From the repo root, after reviewing the diff:

```bash
git add _config.yml _layouts _posts assets blog index.md publications.md projects.md 404.md robots.txt .gitignore CLAUDE.md docs scripts README.md
git status                     # read it before committing
git commit -m "Initial site"
git remote add origin git@github.com:stanlee321/stanlee321.github.io.git
git push -u origin main
```

If the repo does not exist yet, create it on github.com as **public**, named
`stanlee321.github.io`, with no README, no .gitignore, and no license
(the local repo already has what it needs).

### 2.3 Enable Pages

On github.com:

1. Go to the repo → **Settings** → **Pages** (left sidebar).
2. Under **Build and deployment** → **Source**, choose **Deploy from a branch**.
   *Not* "GitHub Actions" — this site is built by GitHub's native Jekyll and has
   no workflow.
3. Under **Branch**, choose **`main`** and folder **`/ (root)`**. Save.
4. Wait for the build. It usually takes one to two minutes for a first build.

For a user site named `stanlee321.github.io`, Pages is often enabled
automatically on first push, with the source already set to `main` / root. Check
the Pages settings anyway and confirm.

### 2.4 Confirm the build

- The **Settings → Pages** panel shows the live URL and the last deployment.
- The repo's **Actions** tab shows a `pages-build-deployment` run. Open it if
  the site does not appear — a kramdown or Liquid error shows up there with a
  file and line number.
- Then check by eye, and this is the part the linter cannot do:
  - the home page renders and the nav works;
  - **the math in the announcement post renders** (KaTeX from cdnjs) — this is
    the single most likely thing to be wrong on first load;
  - Figure 1 loads;
  - the results table scrolls rather than overflowing on a phone;
  - light and dark mode both look right;
  - `/feed.xml` and `/sitemap.xml` exist and are not empty;
  - a 404 (visit `/does-not-exist/`) renders the custom page.

### 2.5 Immediately after the first successful build

Replace `linkedin_url` in `_config.yml`. It is currently the literal string
`TODO-LINKEDIN-URL`, and `index.md` renders it as visible text on the home page.

---

## 3. Routine publishing

Every later change is just a commit to `main`; Pages rebuilds automatically.
There is nothing else to run. Before any push, run the review gate in
`../CLAUDE.md` §7.

---

## 4. Custom domain — salvatierra.io — DEFERRED

**Not being done now.** Written down so it is a ten-minute job when Stanley
wants it. Do not start it without his say-so.

### 4.1 Decide apex or subdomain

- **Apex** (`salvatierra.io`) — needs A / AAAA records. Nicer to say.
- **`www` subdomain** (`www.salvatierra.io`) — needs one CNAME. Slightly more
  robust, and the usual recommendation.

Both can be configured; one is primary and the other redirects.

### 4.2 DNS records at the registrar

**For the `www` subdomain**, one record:

| Type | Name | Value |
|---|---|---|
| CNAME | `www` | `stanlee321.github.io.` |

**For the apex**, four A records and four AAAA records pointing at GitHub Pages:

| Type | Name | Value |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| AAAA | `@` | `2606:50c0:8000::153` |
| AAAA | `@` | `2606:50c0:8001::153` |
| AAAA | `@` | `2606:50c0:8002::153` |
| AAAA | `@` | `2606:50c0:8003::153` |

> **Verify these IPs against GitHub's current documentation before entering
> them** — "Managing a custom domain for your GitHub Pages site". GitHub has
> changed the Pages IP set before, and a stale A record silently serves nothing.
> Treat the table above as a starting point, not as authority.

### 4.3 The CNAME file

Create a file named exactly `CNAME` (uppercase, no extension) at the repo root,
containing one line and nothing else:

```
salvatierra.io
```

(or `www.salvatierra.io` if the `www` form is primary).

Setting the custom domain through **Settings → Pages → Custom domain** creates
and commits this file for you, which is the less error-prone route. Do it there
rather than by hand.

### 4.4 Finish

1. Wait for DNS to propagate — minutes to a day. GitHub shows a "DNS check in
   progress" state in the Pages settings.
2. Once the check passes, tick **Enforce HTTPS** in Settings → Pages. It becomes
   available after GitHub provisions a certificate, which can take up to a day.
3. Update `url:` in `_config.yml` from `https://stanlee321.github.io` to the new
   domain. **This matters:** `url` feeds `jekyll-seo-tag` (canonical URLs,
   og:url), `jekyll-feed` (feed entry links), and `jekyll-sitemap`. Leaving it
   stale means correct-looking pages with wrong canonical links.
4. Update any absolute links that point at the old domain — including the
   `docs/social/` drafts, which carry the full post URL.
5. Append an entry to `log.md`.

### 4.5 Undoing it

Remove the custom domain in Settings → Pages, delete the `CNAME` file, revert
`url:` in `_config.yml`. The `github.io` URL keeps working the whole time.
