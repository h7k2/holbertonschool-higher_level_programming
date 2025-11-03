# Advanced HTML — Techium (Foundations v2.1 – Part 2)

Holberton project: **Advanced HTML** — build a fully structured static website **without CSS** for the fictional company **Techium**.

---

## Overview

Practice writing **clean, semantic HTML5**: correct document skeleton, accessible structure, headings hierarchy, lists, tables, media (images/video/audio), icons, links, and iframes. Some tasks explicitly allow invalid markup for learning purposes; otherwise, aim for **W3C‑valid** HTML.

---

## Learning Objectives

* Create the **HTML5 skeleton**: `<!DOCTYPE html>`, `<html lang="en" dir="ltr">`, `<head>`, `<body>`.
* Use **semantic tags**: `header`, `main`, `footer`, `nav`, `section`, `article`, `aside`, `h1`…`h6`.
* Follow the **headings hierarchy** and know when to use `div` vs `span`.
* Author **lists** (`ul`, `ol`, `dl`), **tables** with `scope` on `th`, and **quotes** (`q`, `blockquote`, `cite`).
* Embed **media**: `img` (with `alt` and dimensions), `video`/`audio` with `controls`, `loop`, `poster`/fallback text.
* Add **favicons** (`.ico` & `.png`) and an **iframe** (YouTube embed).
* Write HTML that is organized, readable, and accessible.

---

## Repository

* **GitHub repository:** `holbertonschool-web_front_end`
* **Directory:** `html_advanced`
* **Required file:** `README.md` (this file) at the root of `html_advanced/`

---

## File Set (summary)

You will progressively create these files:

```
0-index.html, 1-index.html, 2-index.html, 3-index.html,
5-index.html, 6-index.html, 7-index.html, 8-index.html,
9-index.html, 10-index.html, 11-styleguide.html, 12-index.html,
13-styleguide.html, 14-index.html, 15-index.html, 16-index.html,
17-index.html, 18-index.html, about.html, latest_news.html, contact.html,
20-index.html, 21-index.html, 22-index.html, 23-index.html, 24-index.html,
25-index.html, 26-styleguide.html, 27-index.html, 28-styleguide.html,
29-index.html, 30-styleguide.html, 31-index.html, 32-styleguide.html,
33-styleguide.html, 34-styleguide.html, 35-index.html, 36-index.html,
index.html (final), 38-styleguide.html, 39-styleguide.html, styleguide.html
```

> **Company name:** Techium

---

## Assets

* **Favicons:** generate via [https://realfavicongenerator.net/](https://realfavicongenerator.net/)

  * Place `favicon.ico` and `favicon.png` at the project root (siblings to your HTML files).
  * Link both in `<head>` with `rel`, `type`, and `href`.
* **Images (later tasks):** place under `images/` with required filenames from the task (e.g., `pic-work-01.jpg`, `pic-person-01.jpg`, etc.).
* **Logo:** `logo-black.png` (160×40) used in header and footer (task 35).

---

## Getting Started

1. Create `0-index.html` with the doctype and `<html lang="en" dir="ltr">`.
2. Add `<head>` and `<body>` (tasks 1–3 progressively add meta, title, description, viewport, and favicons).
3. Build out **Header / Main / Footer**, then sections and articles as specified.
4. Open files directly in your browser to preview.

---

## Validation (when required)

* Use the **W3C Markup Validator** to check files that must pass.
* Common pitfalls:

  * Missing `lang`/`dir` on `<html>`.
  * Incorrect heading order (`h1` before `h2`, etc.).
  * Missing `alt` on `<img>`.
  * Missing `scope` on table headers.

---

## Task Roadmap (high level)

* **0–3:** Base skeleton, head/body, meta/viewport/title/description, favicon; add header/main/footer.
* **4–6:** Add `aside`; create sections; create `article`s for Works/News/Testimonials.
* **7–10:** `nav`; add `h1`, `h2`, `h3` per section and article requirements.
* **11–13:** Start **styleguide** page; headings & paragraph examples.
* **14–16:** Add `span` logo text, wrap with `div`s, structure section content with `header` + content.
* **17–18:** Add comments for scanning; link the logo to `/` inside a wrapper `div`.
* **19–25:** Create extra pages; build nav links; social links; button-like links; list links; footer secondary nav.
* **26–28:** Styleguide lists; footer separator `<hr>` example.
* **29–31:** Testimonials as `blockquote` + `cite`; address in footer; news authors with `<small>`.
* **32–34:** Typography (address formatting, `pre`/`code`, highlighted text via `<mark>`); table with `scope`; `details/summary` examples.
* **35–37:** Replace text logo with image; add images to sections; replace social links with **SVG icons** in the final `index.html`.
* **38–40:** Add video, audio, and iframe examples to the styleguide.

---

## Accessibility & Semantics Tips

* Use **meaningful headings** and keep hierarchy consistent.
* Provide **descriptive `alt` text** (or empty `alt` for decorative images when the task says so).
* Use `<nav>` for navigation, `<section>` for major areas, `<article>` for self‑contained content, `<aside>` for complementary info.
* Use `<q>` for inline quotes and `<blockquote>` + `<cite>` for longer quotations.
* Use `th scope="col"`/`scope="row"` in tables.

---

## How to Run Locally

Open any HTML file in your browser (e.g., double‑click `index.html`). No server or build step required.

---

## Notes

* Some tasks state: **“W3C won’t pass / does not need to pass”** — ignore validator errors for those specific steps.
* Filenames must match **exactly**; the checker is strict.

---

## Author

Project by **Holberton School**. Implementation by **[Your Name]** for the **Techium** website exercises.
