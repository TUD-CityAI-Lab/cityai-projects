---
name: cityai-highlights
description: Add or update CityAI Lab landing-page highlights about papers, graduations and lab events, with concise text, an authentic image and the repository publishing workflow.
---

# CityAI highlights agent

Read repository `AGENTS.md` and `.agents/website-publishing.md`. Follow their synchronisation and publication contract.

## Write the highlight

Use the supplied description, paper link/DOI or thesis link to identify the event, date, participants and correct publication status. Read primary sources when links are supplied. Check existing Highlights for the same paper/event before adding anything.

Write a descriptive heading and normally 60–120 words in British English. Lead with what happened, explain the research question and contribution in accessible terms, and link the paper/thesis when available. Use a warm but restrained tone for graduations. Mention honours only when supplied or verified. Do not call a preprint a published journal paper or claim open access without checking.

Place the complete new `.row.highlight-item` in `index.html` under Highlights, in descending event-date order. Follow this existing structure, substituting real facts:

```html
<div class="row highlight-item">
  <div class="col-md-8 highlight-text">
    <h3>Descriptive event heading</h3>
    <p><strong>Month YYYY</strong> – Concise announcement and research context.
      <a href="https://primary-source.example/paper">Read the paper</a>.</p>
  </div>
  <div class="col-md-4 highlight-image">
    <img src="{{ 'assets/images/highlights/descriptive-name.webp' | relative_url }}"
         class="img-fluid" alt="Accurate description of the image">
  </div>
</div>
```

Retain existing highlights unless removal is requested. Do not rewrite unrelated news or run the publication-list automation merely because a paper highlight is added.

## Choose an image

- Paper: use an authentic screenshot of the actual article on the publisher website that includes the journal name, full paper title and all authors. A masthead alone, or a screenshot of another paper in the same journal, is insufficient. Open the article, adjust browser zoom/viewport if needed to make the heading readable, and capture a tight crop covering the journal heading, complete title and complete author list. Exclude unrelated navigation, sidebars and the abstract. Choose the width-to-height ratio to fit these elements without cutting text; roughly 2:1 to 3:1 is often suitable, but complete readable content takes priority. Save a real cropped screenshot as a local PNG and display it at its natural ratio using `img-fluid`, without a CSS crop that hides the title/authors. Inspect the saved image and the rendered highlight at desktop and mobile widths. Never synthesise publisher branding, paper text or authors. If the publisher cannot be accessed, use an authentic first-page crop including journal, title and authors, or request the owner's screenshot; do not substitute another paper's heading. Use an alternative research figure only if the owner requests it.
- Graduation: prefer the supplied defence photograph or thesis cover. If no defence photo is available, an authentic cover obtained from the thesis is suitable. Do not use a stock or generated person as the graduating student. If neither an authentic photo/cover nor a relevant supplied illustration is available, prepare the text and request the missing image/source before publishing the incomplete highlight.
- Other event: use a relevant authentic event image or supplied illustration.

Save the image locally and follow the shared image rules. Preview both columns and mobile stacking.

## Graduation handoff

For an MSc graduation, also read `../cityai-msc-projects/SKILL.md`. If the project is ongoing, move its existing include to Finished projects and remove the student's active MSc Team card as part of the same commit. If already finished, verify it rather than duplicating the transition. Retain the finished project/contact card and historical assets. Do not apply MSc Team removal rules to PhD graduations or other roles.

Validate, publish and verify using the shared workflow. Report the live highlight and any associated MSc transition.
