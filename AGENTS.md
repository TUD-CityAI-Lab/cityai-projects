# CityAI Lab website maintenance agents

Maintain https://www.cityai-lab.nl/ from this Jekyll repository. Use British English, concise accessible academic prose, and the existing Bootstrap layout. Preserve supplied names and verified research claims.

## Agent roles

- **Highlights agent:** read `.agents/skills/cityai-highlights/SKILL.md` when adding or updating landing-page news about papers, graduations or lab events.
- **MSc projects agent:** read `.agents/skills/cityai-msc-projects/SKILL.md` when adding, editing, removing or changing the status of MSc opportunities/projects, or maintaining their student profiles and active Team membership.
- For an MSc graduation, use both skills: publish the highlight, move the project to Finished projects, and remove the student's active MSc Team card in one coordinated change.

These are specialist roles and reusable instructions; they do not create background processes or scheduled agents. Select the relevant role from the user's task. Read the named skill directly if repository skill discovery is unavailable.

## Repository map

- `index.html`: Highlights and The Team, including Master students.
- `master-projects/index.md`: Current opportunities, Ongoing projects, Finished projects; `include_relative` lines determine membership and order.
- `master-projects/_opportunity-*.md` and `_project-*.md`: HTML fragments, without page frontmatter.
- `master-projects/avatars/`: student portraits; `person.webp` is an existing neutral fallback.
- `assets/images/highlights/`: preferred new highlight image location.
- `master-projects/images/`: preferred new topic-image location; create when needed.
- `_layouts/`, `_includes/`, `assets/`: shared site presentation. Follow existing classes rather than redesigning them for content tasks.
- `Gemfile` and `Gemfile.lock`: Jekyll dependencies; use Bundler.

“Persona” means the student's real name, portrait and project/contact card, with a linked Team card. Do not invent a biography or create a separate profile page unless requested.

## Task and publishing contract

For a requested content-maintenance task, the owner authorises synchronising the latest repository, making the scoped edits, committing and pushing to the live publishing branch without a separate routine approval. Honour an explicit draft-only/no-push request. This standing contract does not instruct agents to publish merely because they are reviewing or editing agent instructions.

Read `.agents/website-publishing.md` for every maintenance task. It defines synchronisation, concurrent-agent handling, validation, publishing and live verification. Both agents edit `index.html`: coordinate changes and publication; do not run simultaneous mutations in one checkout.

Ask only for missing facts that affect identity, project status or factual accuracy. Prepare everything independent of those facts while waiting. A missing portrait can use the existing neutral fallback; a missing event image can use an authentic thesis cover or suitable factual alternative described in the skill. Never manufacture a person's face, defence photograph, publisher logo or journal masthead.

Finish with the changed content/status, commit identifier, deployment result and relevant live links. Distinguish pushed changes from verified live changes.
