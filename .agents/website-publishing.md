# Shared maintenance and publishing workflow

## Synchronise and coordinate

Run from the Git repository root. Check `git status --short`, current branch and `git remote -v`. The expected origin is `https://github.com/TUD-CityAI-Lab/cityai-projects.git`; do not silently change it.

With a clean `main` checkout, run `git pull --ff-only origin main` before editing. With unrelated uncommitted changes or another active agent, use an isolated checkout/worktree based on fetched `origin/main`, or coordinate exclusive use of the checkout. Do not stash, discard, stage or publish another person's changes. Never reset the checkout to make a pull work. A dirty checkout containing only this task's interrupted edits can be resumed after inspecting them and remote changes.

Before each edit, check whether the requested item already exists. Update the existing item rather than duplicating it. Keep project IDs and published anchors stable.

## Content and images

Use facts supplied by the owner or verified primary sources. Do not invent results, supervisors, student details, honours, dates or acceptance/publication status. Match event dates rather than today's date. Resolve incomplete dates with the owner when necessary.

Prefer owner-supplied images, existing relevant repository assets, or primary-source images whose reuse is appropriate. Record the source/credit in the task report or an adjacent HTML comment; display attribution when required. Save new images in the repository rather than hotlinking. Use descriptive filenames and alt text. Inspect the image; retain a readable journal heading or thesis title when cropping. Resize large assets to practical display dimensions (usually at most 1600 px wide); use WebP/JPEG for photos and PNG for text/screenshots, typically below 500 KB unless readability requires more.

For generic project illustrations, an available image-generation skill can help. Follow its instructions if used, and describe the image as an illustration. Never generate a student portrait, purported defence photo or fabricated journal heading. A neutral existing avatar is acceptable when no real portrait is available.

For paper highlights, extract the image from the published PDF's first page, including its original journal banner/logos, full paper title and all authors. Preserve the PDF's recognisable journal design and typography. An HTML article-heading screenshot or masthead-only image does not meet the owner's requirements. Display the saved crop at its natural ratio. Follow the highlights skill for PDF rendering, crop selection and owner-supplied PDF-crop fallback details.

Use `relative_url` for local image paths and site links. Escape HTML text and attributes. For external links opened in a new tab, include `rel="noopener noreferrer"`.

## Validate

1. Review the scoped diff and run `git diff --check`. Confirm referenced files exist with exact filename case, project includes resolve, and anchors are unique and match Team links.
2. Run `bundle check`, then `bundle exec jekyll build --destination /tmp/<unique-task-directory>` using a directory created with `mktemp -d`. If dependencies are missing, install from the lockfile into a local/temporary Bundler path without changing dependencies. Check Node.js is available for the autoprefixer/ExecJS runtime when needed. Do not commit generated files or Bundler configuration.
3. Inspect rendered `/` and `/master-projects/` at desktop and narrow/mobile widths using a local preview when browser tools are available. Check the changed image loads, text reads well, and Team links land on the correct project. For MSc changes, verify the requested state and corresponding active Team membership together. Count actual rendered cards, ignoring commented-out examples.
4. If a build or relevant validation fails, repair the scoped cause before publishing. If tools/dependencies cannot be obtained, report the specific limitation and leave the prepared change unpublished rather than claiming validation.

## Publish and verify

GitHub Pages settings verified on 1 October 2026: legacy Pages build, branch `main`, source `/`, custom domain `www.cityai-lab.nl`. `_config.yml` and `CNAME` belong to this configuration. The current workflow in `.github/workflows/` updates publications; it is not a deployment workflow. Recheck Pages settings with `gh api repos/TUD-CityAI-Lab/cityai-projects/pages` if available; do not create a new deployment workflow or change hosting for ordinary maintenance.

Stage explicit task files and inspect the staged diff. Commit with a descriptive message. Immediately before pushing, fetch origin and integrate updated `origin/main` into the task branch/checkout. For clean task-only commits, rebase onto it, resolving content conflicts with the latest version and retaining both agents' intended entries. Rebuild after integration if site source changed. Push the task commit(s) as a normal fast-forward update to `origin/main` (for example `git push origin HEAD:main`). Never force-push. If main is protected, create a PR when authorised by the task, report that publication awaits merging, and do not bypass protection.

If a concurrent update rejects the push, fetch, reconcile, validate and retry, at most twice. If conflicts cannot be resolved from the supplied facts, preserve the work and report the blocker.

Check the Pages build for the pushed revision using the repository Pages build API or its Pages deployment run. Use bounded polling with progress updates; allow about five minutes, then report pending rather than waiting indefinitely. Fetch the live changed pages and verify the actual new text, status, portrait/topic image and anchors. A successful Git push or HTTP 200 alone does not prove the intended revision is live. Report failures, pending builds and cached older content accurately, with the commit and live links.
