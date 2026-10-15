TEST BRANCH NOTE: this branch (feat/2026-10-15/version-1) is a self-contained
test build and deliberately carries `css/`, `js/` and `htrab/` because the
verse-study changes are not in a tagged template release yet. On `main` the
shell rule below still applies. Do not merge this branch into `main` as it is.

This repo is the shell for one book: `index.html` (a loader), `questions.json`,
`images/`, `media/` and `book-structure/`. All quiz code is loaded from a
tagged copy of https://github.com/eckko/recall-quiz-site-template on
jsDelivr. Do not add `css/`, `js/`, `htrab/`, `themes/` or `vendor/` here.
Never point `index.html` at a branch; use an exact tag
(`python3 tools/set_template_tag.py TAG`). For the code, tools, tests and
AI notes (AGENTS.md, ai-context/), see the template repo.
