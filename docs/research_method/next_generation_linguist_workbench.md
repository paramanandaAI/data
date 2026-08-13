# Next-Generation Linguistic Annotation Toolkit: KISS Design Blueprint & Planning Document

## 1. Executive Summary & Design Vision

Linguistic annotation for low-resource languages (e.g. Nepali, Newari, Maithili) requires balancing real-world industry deployability with strict academic and linguistic satisfaction. Desktop-first annotation tools fail because field linguists often annotate on the go via tablets or mobile viewports. 

This document defines the architectural blueprint for **KISS** (Keep It Simple, Scholar!) as a **web-first, mobile-view responsive annotation workbench** built natively in Python using **Gradio 6.0** and CSS.

---

## 2. In-Depth Analysis of the Gradio Ecosystem

We analyzed the Gradio ecosystem repository dumps (`awesome-demos`, `custom-components`, `trackio`, `trail-exp`) to extract production patterns:
- **`trail-exp` (Agent-Native SDK)**: Proves that pagination queues (`annotation-queue.md`) and state difference visualizers (`diff-reviewer.md`) are the most effective ways for human-in-the-loop validation of code-mixed or spelling-corrected datasets.
- **`trackio` (Local-First Logging)**: Reinforces our plain YAML sidecar strategy. Storing metadata (`photo.jpg.yml`) adjacent to images avoids locking database schemas and simplifies version control.
- **`custom-components`**: Demonstrates Svelte-based wrappers. However, to avoid Node/npm build toolchains on linguists' local systems, we prioritize **Core Gradio Components + Custom inline CSS + HTML5 Canvas scripts** to build advanced interactive widgets.

---

## 3. Resolving Missing Gradio Annotation Components

Standard Gradio lacks interactive annotation tools such as bounding-box drawers, token segment highlights, or transcript editors. We resolve these natively:

### A. Bounding Box & Region Annotation (HTML5 Canvas Overlay)
Instead of building a Svelte component, we can use `gr.Image(tool="sketch")` or render a custom image viewport inside a `gr.HTML` block containing a vanilla Javascript HTML5 Canvas overlay.
- The canvas script listens to click/drag coordinates on the client side.
- Coordinates are stringified into a JSON payload (e.g. `[{"x": 10, "y": 20, "w": 50, "h": 50}]`) and written to a hidden `gr.Textbox(visible=False)` component using standard DOM selector queries (`document.querySelector('textarea').value = ...`).
- Clicking "Save" triggers the textbox change event, syncing coordinates directly back to the Python backend.

### B. Segment & Token Highlight Selection
For grammatical annotation (such as marking detached postpositions or misspelled tokens):
- We render the text inside a `gr.HTML` wrapper.
- Tokens are wrapped in custom span elements: `<span class="k-token" onclick="toggleToken(this)">नेपाली</span>`.
- A small inline JS script toggles a selected class on click, serializing selected token indices into another hidden Gradio Textbox for instant sidecar sync.

---

## 4. Web-First Mobile View Architecture

The KISS user interface operates under a strict mobile-responsive responsive grid design:

```
+------------------------------------------+
| 💋 KISS Workspace [Total: 3/72 Annotated]  | <- Header (Brand + Overall Progress Bar)
+------------------------------------------+
|                                          |
|  [Image Viewer / HTML Text Viewport]     | <- Main Viewport (Autoscales to height)
|  - Large visual context                  |
|                                          |
+------------------------------------------+
|  [Linguistic Form Inputs]                | <- Inputs (Stacked below viewer on mobile)
|  - Language Code (Compulsory)            |
|  - Caption Box / Tags / Source           |
+------------------------------------------+
|  🏠 Home  |  🖼️ Library  |  ✏️ Annotate    | <- Sticky Bottom Nav Bar (Mobile Viewport)
+------------------------------------------+
```

### Mobile Layout Specifications
- **Navigation Toggle**: Switched via Gradio column visibility (`gr.update(visible=True)`). Layouts remain pre-loaded to ensure zero navigation latency.
- **Screen Header**: Every subview starts with `components.layout.brand_bar` displaying high-level counts.
- **Tap Targets**: All buttons, tags, and dropdown items have a minimum height of `44px` with `12px` of margin to prevent thumb-miss errors.
- **Accordions**: Auxiliary panels, such as the Ollama Vision Agent, are collapsed (`gr.Accordion(open=False)`) by default to prevent long vertical page scrolls.

---

## 5. Custom Agent Skills Structure

We define a streamlined, highly verbose set of customization skills inside `.agents/skills/gradio_repos/`:

1. [`gradio/SKILL.md`](file:///D:/noising_denoising/kiss/.agents/skills/gradio_repos/gradio/SKILL.md):
   - Gradio 6.0 Block constraints (CSS and Theme passed to `.launch()`).
   - Transitioning `gr.Box` usage to `gr.Group` or `gr.Column(variant="panel")`.
   - Local file paths rendering conventions using `gr.Image(type="filepath")` and `gr.Gallery`.
2. [`gradio-mobile-app/SKILL.md`](file:///D:/noising_denoising/kiss/.agents/skills/gradio_repos/gradio-mobile-app/SKILL.md):
   - CSS-driven Bottom Navbar media queries for screens under 900px.
   - Fluid columns wrapping with `min_width` parameters.
   - Touch targets and mobile form design principles.
3. [`annotation-canvas/SKILL.md`](file:///D:/noising_denoising/kiss/.agents/skills/gradio_repos/annotation-canvas/SKILL.md) [NEW]:
   - Client-side Javascript hooks for region highlight and coordinates serialization.
   - Exchanging values between custom HTML rendering and hidden Gradio form inputs.
4. [`sidecar-data-flow/SKILL.md`](file:///D:/noising_denoising/kiss/.agents/skills/gradio_repos/sidecar-data-flow/SKILL.md) [NEW]:
   - Storing localized YAML sidecars containing source text, targets, statuses, and evaluations.
   - Exporting multimodal dataset files (JSONL and structured ZIP).
5. [`nepali-nlp-validation/SKILL.md`](file:///D:/noising_denoising/kiss/.agents/skills/gradio_repos/nepali-nlp-validation/SKILL.md) [NEW]:
   - Heuristics for Devanagari script verification.
   - Custom checklists for matra/halanta dropping and Nepali postposition detacher validation.
