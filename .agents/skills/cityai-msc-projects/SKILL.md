---
name: cityai-msc-projects
description: Maintain CityAI Lab MSc opportunities and ongoing or finished projects, including concise descriptions, topic images, student profiles and synchronised active Team membership.
---

# CityAI MSc projects agent

Read repository `AGENTS.md` and `.agents/website-publishing.md`. Follow their synchronisation and publication contract.

## Determine the operation

Use the owner's description to identify the project, requested status and student where applicable. If a new description has no assigned student, treat it as a Current opportunity. Ask for the student's real name before publishing an ongoing project if it is missing. Do not infer completion from elapsed time or from the presence of an old file.

Project state is the section containing its `include_relative` in `master-projects/index.md`, not file frontmatter or a database. An active MSc project and its student Team membership must be changed together.

| Requested state/action | Project page | Landing-page Team |
| --- | --- | --- |
| New opportunity | `_opportunity-<slug>.md`, included under Current opportunities | No student card |
| New ongoing project | `_project-<slug>.md`, included under Ongoing projects, with student contact card | Add one linked active student card |
| Opportunity starts | Replace/remove opportunity include; add ongoing project include, preserving useful content and links | Add assigned student's card |
| Project finishes | Move the existing project include from Ongoing to Finished projects | Remove the corresponding active MSc card |
| Project removed | Remove its include from the requested section | Remove its card if no remaining ongoing project or separately confirmed active role requires it |
| Description edited | Edit the existing fragment; preserve anchor | Update linked name/portrait if requested |

Do not remove unrelated research interns, supervisors or other members. One student with multiple ongoing projects needs one Team card; retain it until their last ongoing project ends. If a completing student has another separately identified active lab role, remove the MSc-project membership but retain that confirmed role. Do not assume such a role exists.

## Project content and images

Inspect a nearby `_project-*.md` or `_opportunity-*.md` before editing. Reuse its HTML layout: `.row`, `.col-sm-8` for research text, `.col-sm-4` for `.card.contact-card`. Fragments have no Jekyll frontmatter. Give the heading a unique stable kebab-case `id`; use the same ID in the Team link.

Write a clear title and normally 80–150 words covering the problem, proposed approach/data and intended contribution. An opportunity should invite a student to investigate; an ongoing project should describe work in progress; a finished project should use completed tense only for verified work and findings. Add supervision/collaboration details only when provided or verified. Preserve verified thesis, code and detailed-description links. Do not invent a student's email address.

Each new project/opportunity needs a suitable topic image in addition to any student portrait. Prefer a supplied/reusable real image, meaningful research illustration or diagram. An image-generation skill, if available, may create a generic topic illustration; do not imply it depicts actual research data or results. Save it under `master-projects/images/<slug>.<ext>` and use an `.img-fluid` image with descriptive alt text in the text column, or another placement consistent with the existing layout. Follow the shared image rules. Existing edited projects need new imagery only when requested or when adding the requested missing image.

For an ongoing student, add a contact card in the project fragment using their real name and portrait under `master-projects/avatars/`. Use `master-projects/avatars/person.webp` if a portrait is unavailable; explicitly report the fallback. A project illustration cannot serve as the student's portrait. Reuse the same portrait for their Team card.

## Landing-page student card

Add one complete `.col` in the active Master students grid in `index.html`, outside HTML comments. Follow existing `.card.team-card`, `.card-img-top`, `.card-body`, `.card-title` and `.card-text` classes. Link the name with `.stretched-link` to `{{ 'master-projects/#stable-project-id' | relative_url }}` and use `Master student` as the role. Include accurate alt text on the portrait.

On completion, move the original include exactly once to Finished projects, near recent completions where the date is known. Preserve its anchor, contact card, portrait and historical links. Remove the whole corresponding active Team `.col`; do not merely hide it in a comment. Add a verified completion month/thesis link when available, but do not invent results. A graduation announcement is added only when graduation is requested or confirmed; then use `../cityai-highlights/SKILL.md` as well.

On removal, removing the include unpublishes the project. Keep the underlying fragment and assets by default as an archive. Delete them only when explicitly requested and after checking other references. Never remove a shared portrait or image still used by another project, Team member or highlight.

## Verify the linked state

Check the rendered project appears in exactly the intended section, its topic image and portrait load, and its anchor resolves. An ongoing student's active Team card must appear once and link correctly. A finished/removed project's former MSc card must be absent unless another confirmed active assignment requires membership. Ignore historical cards inside comments and preserve unrelated interns. Then follow the shared build, push and live-verification workflow for both pages.
