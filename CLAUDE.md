# Personal learning system

When the user says "I want to learn <Subject>":

- Detailed layout: `<Subject>/00_Roadmap.pdf`, `Notes/NN_Topic.pdf` (one per topic), `Programs/NN_Topic/…`, `<Subject>_Tracker.xlsx`.
  Each topic PDF: Definition, Diagram, Syntax, Example Program, Output, Tamil real-world example, Common Mistakes,
  Interview Questions (3-5), Practice Exercises (3). Topics are numbered in learning order, grouped Beginner → Intermediate → Advanced → Master.
- Programs must compile/run. For Angular, `python tools/build_subject.py angular` compiles every program (AOT, strict templates)
  in `tools/angular_harness`, runs them in headless Chromium and writes the real output into the PDFs.
- If the subject folder exists, add topics (append to the content list) and rebuild; the tracker keeps the learner's progress.
- Combined overview PDF per subject: `python tools/build_guides.py [Subject …]` → `<Subject>/<Subject>_Zero_to_Master.pdf`.
- Content lives in `tools/content/`. PDFs are rendered with Chromium (needs Noto Sans Tamil for correct Tamil shaping).
