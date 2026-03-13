# Topic Wiki Factory

[Korean](README.md)

An AI-agent template that helps you produce a first draft of a beginner-friendly wiki, one that reads more like a short book than a loose pile of notes, in about 30 minutes.

> "What is this?" -> "Why does it matter?" -> "What should I learn first?" -> "How do I use it?"
> in that order, so even a complete beginner can follow the wiki.

For beginner-focused topics, it aims to generate a hub-style starter wiki where `index.md` acts like a home page with the big picture, a 5-minute summary, reading order, rule summaries, and external study resources.

## What This Template Produces

- a hub-style home page that tells a new reader where to begin
- beginner-first docs that explain why a topic matters before the details
- a living learning wiki with `sources.md`, update watch points, and optional SVG explainers

Good fits:
- `Harness` -> a Harness CI/CD wiki
- `Chess` -> a beginner-friendly chess learning wiki
- `n8n` -> an n8n automation wiki

![Example output preview](assets/readme-preview.svg)

## See an example

[examples/README.md](examples/README.md) shows the generated output first.
It currently includes three lightweight examples: `examples/chess-intro/`, `examples/codex-101/`, and `examples/hitl-intro/`.

`examples/chess-intro/` shows:

- a hub-style home page
- a beginner-first starter guide
- SVG explainers for castling, en passant, and promotion
- a `sources.md` file that works as both a resource hub and an update watch list

`examples/hitl-intro/` shows a concept-focused wiki about human approval checkpoints, automation boundaries, and approval UX.

## Getting Started

The least-confusing recommended path looks like this:

1. Run `wiki-initializer` to define the topic and output path.
2. Run `wiki-orchestrator` to drive research, writing, and review.
3. Use `wiki-updater`, `wiki-auditor`, and `wiki-publisher` when needed.

Right now, the smoothest runtime is `Claude Code`.
`Cursor`, `Codex`, and `GPT` are also supported, but currently through a best-effort paste-the-prompt workflow.

Important: this repository does not yet include a one-command runner such as `./wiki create ...`.
Today, the core value is "state-based orchestration + prompts + sample outputs", not a fully automated CLI.

### Option 1. Start from the GitHub template

1. Click `Use this template` on GitHub.
2. Clone your new repository locally.
3. Run the workflow below in Claude Code or your preferred AI runtime.

### Option 2. Clone directly

```bash
git clone https://github.com/techtaek77/topic-wiki-factory my-wiki
cd my-wiki
```

### 1. Initialize

If you use Claude Code:

```text
@wiki-initializer
```

If you use Cursor / Codex / other runtimes:
- Open `prompts/wiki-initializer.md` and paste it into your AI tool.

The initializer asks 11 setup questions for topic definition, exclusions, seed materials, and output path, then creates `wiki-config.yaml`, `wiki-state.json`, and `{output_path}/wiki-memory.md`.

### 2. Generate the wiki

```text
@wiki-orchestrator
```

The orchestrator reads `wiki-state.json` and decides what to do next.
If the process stops halfway through, rerunning it will skip documents that are already done.
The default execution model is sequential automation, not parallel writer execution.
At the moment, the orchestrator is closer to a resumable controller than a one-pass runner that goes from init to done in a single command.

If you want the fastest near-automatic flow, set both flags to `false` in `wiki-config.yaml`.

```yaml
hitl:
  confirm_scope_after_research: false
  confirm_ia_before_writing: false
```

The default manual flow with `hitl` confirmations enabled looks like this:

1. `wiki-initializer`
2. `wiki-researcher`
3. `wiki-orchestrator` -> scope confirmation
4. `wiki-orchestrator` -> IA confirmation
5. Repeat `wiki-writer {slug}`
6. `wiki-reviewer`

## Output Principles

- knowledge wikis: a hub-style starter wiki where readers can quickly find the next step
- tool wikis: a practical docs hub with quick start and changelog support
- special-rule / exception / spatial docs: visual-first explanations instead of text-only walls
- `sources.md`: not just a citation scratchpad, but a resource hub plus required learning axes plus update watch points

## Keeping the wiki alive

This project works better as a living wiki than a one-shot generation script.
People get rusty when they stop learning, and wikis do the same when they stop updating.

Recommended maintenance loop:

1. Run `wiki-researcher` when official references or recommended resources may have changed.
2. Run `wiki-updater {slug} "{change summary}"` when a document needs a content refresh.
3. Run `wiki-gap-finder` to detect missing learning paths or missing documents.
4. Run `wiki-auditor` to inspect links, hub pages, and resource quality.
5. Run `wiki-orchestrator` to schedule the next writing pass.

For knowledge wikis, the default maintenance loop assumes a beginner hub guide such as `basics` plus a continuously maintained `sources.md` with learning resources and update watch points.
For board layouts, rule exceptions, or state-change-heavy topics, visual assets such as SVG diagrams should be maintained alongside the text.

### 3. Publish after review

After changing `publish.enabled: true` in `wiki-config.yaml`, run:

```text
@wiki-publish-preflight
@wiki-publisher
```

`wiki-publish-preflight` checks missing `repo_url`, whether a `.wiki.git` target needs `Home.md`, and whether internal files are excluded correctly.

### Quick verification

Before opening a PR, you can run the acceptance harness:

```bash
python3 scripts/orchestrator_harness.py
```

It covers 12 orchestrator scenarios.
This script is an acceptance checker for state-transition rules, not a full pipeline runner that generates a wiki end to end.

## Handling ambiguous topic names

Some topics, like `Harness`, may refer to a product name or a general concept.
The researcher compares possible meanings first, then the follow-up confirmation depends on your `hitl` settings.

1. The researcher compares possible meanings.
2. If `hitl.confirm_scope_after_research=true`, the orchestrator asks for human confirmation after research.
3. If `hitl.confirm_ia_before_writing=true`, the IA is confirmed once more before writing starts.
4. If either flag is `false`, that confirmation step auto-advances instead.

That helps prevent the classic "I meant execution harness, why did I get CI/CD docs?" moment.

## Repository structure

```text
/
├── .claude/agents/       <- Claude Code agents
├── assets/               <- static assets for README
├── examples/             <- lightweight sample wiki snapshots
├── prompts/              <- prompts for other runtimes
├── specs/                <- phased design proposals
├── templates/            <- document templates and schema examples
├── CONTRIBUTING.md
├── LICENSE
├── CODE_OF_CONDUCT.md
├── README.md
├── README.en.md
├── plan.md
├── spec.md
├── wiki-config.yaml
└── wiki-state.json
```

The root `wiki-config.yaml` and `wiki-state.json` are intentionally blank starter files.
Validation artifacts are not committed. Only curated example outputs under `examples/` are checked in; real generated files such as `docs/`, `sources.md`, and `wiki-memory.md` are created under your chosen `output_path` after the first run.

```yaml
output_path: "./output/harness"        # standalone folder
output_path: "03.Resources/하네스"     # inside an Obsidian vault
output_path: "../my-chess-wiki/docs"   # inside another repository
```

## Runtime usage

| Runtime | How to use |
|---------|------------|
| Claude Code | run `@wiki-initializer` -> repeat `@wiki-orchestrator`. Current primary path |
| Cursor | open `prompts/wiki-*.md` and paste them directly into the Agent/Chat input. Current best-effort path |
| Codex / GPT | open `prompts/wiki-*.md` and paste them into your AI. Current best-effort path |

## Advanced: Agent list

You do not need to memorize all of these to get started.
For a first run, `wiki-initializer`, `wiki-orchestrator`, and optionally `wiki-publisher` are usually enough.

| Agent | Role | When to run |
|------|------|-------------|
| `wiki-initializer` | setup wizard | once at the beginning |
| `wiki-orchestrator` | workflow controller | repeatedly during the flow |
| `wiki-researcher` | source collection | called by the orchestrator |
| `wiki-writer` | document writer | called by the orchestrator |
| `wiki-reviewer` | quality review | called by the orchestrator |
| `wiki-publish-preflight` | pre-publish check | right before publishing |
| `wiki-publisher` | GitHub publishing | once after completion |
| `wiki-updater` | impact analysis for changes | when content changes |
| `wiki-auditor` | structural audit | periodically |
| `wiki-freshness` | freshness check | tool wikis only |
| `wiki-gap-finder` | missing-topic detection | periodically |

## Known Limitations

- It does not fully automate fact verification. A human review is still required.
- It does not yet ship with a one-command runner or a fully automatic end-to-end pipeline.
- The first version is designed around GitHub Markdown publishing.
- It does not guarantee a perfect IA for every topic automatically.
- Multilingual translation, CMS features, and permission systems are outside the current scope.
- Knowledge-focused topics may have weaker official sources, so research quality can vary more.

## Contributing

Check [CONTRIBUTING.md](CONTRIBUTING.md) before opening a PR.
If you change prompts, keep `.claude/agents/` and `prompts/` in sync.

## References

- `EXPERIMENTS.md` -> notes on main / validation / narrative / agent-simplify experiments
- `WRITING-STYLE.md` -> readable, memorable writing rules for docs and samples
- `HYBRID-WRITING-STYLE.md` -> a blend of blog voice and wiki structure
- `DIAGRAM-GUIDELINES.md` -> rules for when to use flowcharts, graphs, and SVG explainers
- `templates/` -> document structure and schema examples
- `spec.md` -> design spec
- `specs/parallel-writer-spec.md` -> parallel writer extension proposal (Phase 2, not implemented yet)
- `tests/README.md` -> orchestrator acceptance harness
- `plan.md` -> development plan
