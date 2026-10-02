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

- Paper: extract a crop from the published article PDF's first page. Preserve its original journal banner, publisher logo/cover art, typography, complete paper title and all authors. The HTML article page has different styling and must not be used as the image source. Read the PDF-header procedure below. Use an alternative research figure only if the owner requests it.
- Graduation: prefer the supplied defence photograph or thesis cover. If no defence photo is available, an authentic cover obtained from the thesis is suitable. Do not use a stock or generated person as the graduating student. If neither an authentic photo/cover nor a relevant supplied illustration is available, prepare the text and request the missing image/source before publishing the incomplete highlight.
- Other event: use a relevant authentic event image or supplied illustration.

Save the image locally and follow the shared image rules. Preview both columns and mobile stacking.

## Extract a paper header from the PDF

1. Follow the publisher page's **View PDF** link and obtain the published version of record. Verify its title, authors and journal against the requested paper. Do not use another paper's banner, a preprint without the journal design, or an HTML reconstruction.
2. Prefer downloading the PDF and rendering page 1 with Poppler at about 150–200 dpi. Inspect the page before selecting crop coordinates. Render the header region directly with `pdftoppm -f 1 -l 1 -singlefile -r 180 -x X -y Y -W WIDTH -H HEIGHT -png article.pdf header`, where coordinates are pixels at the chosen resolution. This preserves the original PDF artwork; do not reconstruct text or use image generation.
3. Include the full journal banner and logos, the complete title, and every author line, including relevant superscripts/ORCID icons. Stop just below the final author line; exclude affiliations, abstract, page footer and PDF viewer controls. Keep the original spacing between the banner, title and authors. Trim outside page margins without clipping logos or text. About 2.5:1 is a useful reference ratio, but the actual header content determines the crop.
4. A screenshot of the actual PDF viewer at a readable zoom is also acceptable when direct rendering is unavailable. If downloading is blocked but the owner supplied an authentic crop of this PDF, use it after checking the title, authors and banner; report that source accurately. If no PDF or suitable supplied PDF crop can be obtained, prepare the text and request the PDF/crop before publishing. Never fall back to the HTML heading.
5. Save a descriptive local PNG, normally 1000–1600 px wide when rendering from the PDF; preserve a supplied crop's resolution rather than enlarging it artificially. Inspect the final image at full size and at the site's display width. Display it at its natural ratio using `img-fluid`, without a CSS crop. Record the PDF DOI/source and whether it was rendered or owner-supplied in an adjacent HTML comment or task report. Use a new filename when replacing an HTML screenshot so cached assets do not mask the correction.

## Graduation handoff

For an MSc graduation, also read `../cityai-msc-projects/SKILL.md`. If the project is ongoing, move its existing include to Finished projects and remove the student's active MSc Team card as part of the same commit. If already finished, verify it rather than duplicating the transition. Retain the finished project/contact card and historical assets. Do not apply MSc Team removal rules to PhD graduations or other roles.

Validate, publish and verify using the shared workflow. Report the live highlight and any associated MSc transition.
