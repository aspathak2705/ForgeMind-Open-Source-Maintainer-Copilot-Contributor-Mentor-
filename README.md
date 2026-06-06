# ForgeMind

ForgeMind is a CLI-first AI maintainer copilot for Python repositories. It scans code, builds a local repository index, surfaces dependency relationships, triages issues, and uses a Nemotron-backed reasoning layer for higher-level maintainer and contributor guidance.

## Problem

Large repositories are hard to understand quickly. New contributors need a reliable way to find relevant files, reason about impact, and identify good starting points. Maintainers need a fast way to inspect repository health, hotspots, and issue context without stitching together multiple tools.

ForgeMind reduces that friction by combining:

- repository indexing and symbol search
- dependency graph analysis
- issue triage and recommendation workflows
- maintainer health summaries
- local memory and reflection storage for agent learning
- optional Nemotron-powered reasoning via OpenRouter

## Architecture

ForgeMind is organized into four layers:

1. CLI layer - `main.py` wires Typer commands into user-facing workflows.
2. Command layer - `commands/` contains the executable CLI actions.
3. Core intelligence layer - `core/` contains parsing, search, graph, issue, mentor, reporting, and LLM orchestration logic.
4. Persistence and integrations - `storage/` and `integrations/` provide SQLite storage, memory, and GitHub sync helpers.

### Data flow

```text
Python source files
  -> FileScanner + PythonParser
  -> SQLite `files` table
  -> RepositoryService / RepositorySearch
  -> ranking, graph, triage, maintainer analysis
  -> optional Nemotron reasoning
```

### Storage model

The local SQLite database stores:

- indexed repository files in `files`
- agent memory in `agent_memory`
- reflections in `reflections`
- synced GitHub issues in `github_issues`
- GitHub pull requests, labels, and contributors in dedicated tables

By default, the database lives at `~/.forgemind/forgemind.db`, unless `FORGEMIND_DB_PATH` is set.

## Agents

ForgeMind currently includes three primary agent workflows:

### Repository Agent

Located in `agents/repository_agent/repository_agent.py`, this agent:

- searches repository context by keyword
- enriches matching files with importance and impact data
- exposes file importance, difficulty, and dependency impact

It powers repository explanation and file discovery flows.

### Issue Agent

Located in `agents/issue_agent/issue_agent.py`, this agent:

- classifies issue text as bug, feature, question, or unknown
- extracts repository-linked keywords from the issue text
- ranks related files and classes
- estimates plausibility, verification level, severity, and confidence
- generates reproduction steps and recommendations
- records both memory and reflections

This is the core of the `triage` command.

### Maintainer Agent

Located in `agents/maintainer_agent/maintainer_agent.py`, this agent:

- computes repository health metrics
- finds hotspot files by dependency impact
- generates a maintainer report
- stores memory and reflections for later review

This is the backbone of the `maintain` command.

### Mentor workflow

The repository also contains mentorship-oriented building blocks under `agents/mentor_agent/` and `core/mentor/`:

- onboarding analysis
- beginner-friendly file ranking
- learning path generation
- difficulty estimation

These pieces are present in the codebase, but a dedicated `mentor` CLI command is not currently wired into `main.py`.

## Nemotron Integration

ForgeMind uses an OpenRouter-hosted Nemotron model through `core/llm/nemotron_provider.py`.

### Provider

- `NemotronProvider` wraps the OpenAI client with `base_url="https://openrouter.ai/api/v1"`
- the model is set to `nvidia/nemotron-3-super-120b-a12b:free`
- reasoning is enabled through the `extra_body` payload

### Prompt orchestration

`core/llm/prompt_builder.py` defines prompt templates for:

- issue analysis
- contributor mentorship
- maintainer reporting

`core/llm/agent_reasoner.py` connects those prompts to the provider.

### Required environment variable

```env
OPENROUTER_API_KEY=your_openrouter_key
```

If the key is missing, Nemotron-backed commands may fail or fall back to generic text in some workflows.

## Commands

The CLI entry point is `forgemind`, defined in `main.py`.

### Available commands

- `forgemind` - show the dashboard
- `forgemind help` - show the command dashboard
- `forgemind index <path>` - scan a repository and store Python file metadata
- `forgemind summary` - intended to print a repository overview, but the current implementation calls a missing `RepositoryService.get_summary()` method
- `forgemind graph` - print a dependency graph from indexed imports
- `forgemind ask <query>` - search for files, classes, functions, and imports matching a symbol
- `forgemind explain <topic>` - show enriched repository context for a topic
- `forgemind triage [issue]` - analyze issue text and generate an assessment
- `forgemind maintain` - generate repository health and hotspot summaries
- `forgemind memory` - print stored agent memory records
- `forgemind reflections` - print stored reflections
- `forgemind doctor` - check Nemotron, memory, and reflection availability

### Present in code, not yet wired

- `commands/sync.py` implements GitHub issue sync, but it is not registered in `main.py`
- `agents/mentor_agent/mentor_agent.py` and related mentor modules are implemented, but no CLI command currently exposes them
- the dashboard text mentions `mentor`, but no `mentor` command is currently registered

## Repository Layout

```text
ForgeMind/
|-- main.py
|-- commands/
|-- core/
|-- agents/
|-- storage/
|-- integrations/
|-- forge_mind_cli/
|-- pyproject.toml
`-- README.md
```

### Core modules

- `core/indexer.py` - scans Python files and writes parsed metadata to SQLite
- `core/parser/` - AST-based Python parser and file scanner
- `core/search/` - repository search and result ranking
- `core/graph/` - dependency graph construction
- `core/issue/` - issue classification, severity, plausibility, confidence, and recommendations
- `core/mentor/` - onboarding and learning path helpers
- `core/reporting/` - plain-text report formatting
- `core/llm/` - provider abstraction and Nemotron integration
- `core/reflection/` - persistent reflections

### Storage and integrations

- `storage/sqlite/` - SQLite database bootstrap and GitHub repository tables
- `storage/memory/` - agent memory service and persistence
- `integrations/github/` - GitHub API client and sync helpers

## Setup

### Requirements

- Python 3.11 or newer
- a working OpenRouter API key for Nemotron-backed features
- optional GitHub token for API sync workflows

### Environment variables

```env
OPENROUTER_API_KEY=your_openrouter_key
GITHUB_TOKEN=your_github_token
FORGEMIND_DB_PATH=C:\Users\you\.forgemind\forgemind.db
```

`GITHUB_TOKEN` is only needed for GitHub sync helpers. `FORGEMIND_DB_PATH` is optional and overrides the default SQLite location.

### Install

```bash
pip install -e .
```

If your environment does not already include the runtime packages imported by the code, install them as well:

```bash
pip install typer pydantic rich python-dotenv openai requests nltk
```

NLTK also needs its data packages:

```bash
python -m nltk.downloader stopwords punkt wordnet omw-1.4
```

### Run

```bash
forgemind
```

Or run a specific command:

```bash
forgemind index .
forgemind explain auth
forgemind triage "App crashes on startup"
forgemind maintain
```

## How it Works

### Indexing

`forgemind index <path>` scans Python files, parses imports/classes/functions with `ast`, and stores structured metadata in SQLite.

### Search and context

`forgemind ask <query>` and `forgemind explain <topic>` query indexed repository metadata to surface relevant files, classes, functions, and imports.

### Dependency analysis

The graph layer matches imported module names against indexed file stems and builds a simple dependency graph for downstream impact analysis.

### Issue triage

The issue pipeline:

1. classifies the issue text
2. extracts keywords
3. finds matching repository context
4. estimates plausibility and confidence
5. derives severity, reproduction steps, and a recommendation
6. stores memory and reflection records

### Maintainer analysis

The maintainer workflow:

1. measures file, class, function, and import counts
2. finds the most impacted files
3. generates an LLM-backed summary when Nemotron is available
4. formats the result as a maintainer report

## Limitations

- The indexer currently targets Python files only.
- The dependency graph is stem-based and may miss imports that do not map cleanly to file names.
- Some modules are present as building blocks but are not exposed as CLI commands yet.
- `summary` is currently incomplete because `RepositoryService.get_summary()` is not implemented.
- The package metadata in `pyproject.toml` should be kept in sync with runtime imports.

## Future Work

- expose the mentor workflow as a first-class CLI command
- wire `commands/sync.py` into the CLI for GitHub sync
- broaden parsing beyond Python-only repositories
- improve dependency resolution for package/module aliases
- add tests for indexing, search, triage, and graph generation
- formalize dependency declarations in `pyproject.toml`
- add richer output formats for reports and recommendations

## Project Goal

ForgeMind aims to help maintainers and contributors move from raw repository code to actionable understanding as quickly as possible.
