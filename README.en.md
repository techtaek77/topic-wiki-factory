# Topic Wiki Factory

[Korean](README.md)

An AI-agent template for generating a Feynman-structured learning wiki for any topic in about 30 minutes.

> "What is this?" -> "Why does it matter?" -> "What should I learn first?" -> "How do I use it?"
> in that order, so even a complete beginner can follow the wiki.

Examples:
- `Harness` -> a Harness CI/CD wiki
- `Chess` -> a beginner-friendly chess learning wiki
- `n8n` -> an n8n automation wiki

![Example output preview](assets/readme-preview.svg)

## See an example

If you want to see the generated output first, check `examples/chess-intro/`.
It includes lightweight examples such as `examples/chess-intro/` and `examples/codex-101/`, with the input config, the state file, and a sample output wiki.

## Getting Started

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

The initializer asks for the topic definition, exclusions, local seed materials, and output path, then creates `wiki-config.yaml` and `wiki-state.json`.

### 2. Generate the wiki

```text
@wiki-orchestrator
```

The orchestrator reads `wiki-state.json` and decides what to do next.
If the process stops halfway through, rerunning it will skip documents that are already done.
If both `hitl.confirm_scope_after_research` and `hitl.confirm_ia_before_writing` are `false`, it will move through those phases without asking for human confirmation.
The default execution model is still sequential automation, not parallel writer execution.

The default manual flow with `hitl` confirmations enabled looks like this:

1. `wiki-initializer`
2. `wiki-researcher`
3. `wiki-orchestrator` -> scope confirmation
4. `wiki-orchestrator` -> IA confirmation
5. Repeat `wiki-writer {slug}`
6. `wiki-reviewer`

### 3. Publish after review

After changing `publish.enabled: true` in `wiki-config.yaml`, run:

```text
@wiki-publish-preflight
@wiki-publisher
```

`wiki-publish-preflight` checks missing `repo_url`, whether a `.wiki.git` target needs `Home.md`, and whether internal files are excluded correctly.

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
Sample generated outputs are not committed as validation artifacts. Real generated files such as `docs/`, `sources.md`, and `wiki-memory.md` are created under your chosen `output_path` after the first run.

```yaml
output_path: "./output/harness"        # standalone folder
output_path: "03.Resources/하네스"     # inside an Obsidian vault
output_path: "../my-chess-wiki/docs"   # inside another repository
```

## Agent list

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

## Runtime usage

| Runtime | How to use |
|---------|------------|
| Claude Code | run `@wiki-initializer` -> repeat `@wiki-orchestrator` |
| Cursor | adapt files from `prompts/wiki-*.md` into `.cursor/rules/` |
| Codex / GPT | open `prompts/wiki-*.md` and paste them into your AI |

## Known Limitations

- It does not fully automate fact verification. A human review is still required.
- The first version is designed around GitHub Markdown publishing.
- It does not guarantee a perfect IA for every topic automatically.
- Multilingual translation, CMS features, and permission systems are outside the current scope.
- Knowledge-focused topics may have weaker official sources, so research quality can vary more.

## Contributing

Check [CONTRIBUTING.md](CONTRIBUTING.md) before opening a PR.
If you change prompts, keep `.claude/agents/` and `prompts/` in sync.

## References

- `templates/` -> document structure and schema examples
- `spec.md` -> design spec
- `parallel-writer-spec.md` -> parallel writer extension proposal
- `tests/README.md` -> orchestrator acceptance harness
- `plan.md` -> development plan
