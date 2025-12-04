# AI Workflow Kit

A CLI toolkit for setting up AI-assisted development workflows across repositories.

## Features

- **Claude Code Commands**: Prime context, parallel experiments
- **Experiment Framework**: Docker-based A/B testing for different approaches
- **Spec-kit Integration**: Optional spec-driven development setup

## Prerequisites

- Python 3.11+
- [uv package manager](https://docs.astral.sh/uv/getting-started/installation/)
- Docker (for experiments)
- [spec-kit](https://github.com/github/spec-kit) (optional)

## Installation

There are two ways to use this toolkit:

### Option 1: Install Globally (Recommended)

Install the `workflow` command on your system so you can use it in any repo:

```bash
uv tool install ai-workflow-kit --from git+https://github.com/timjmitchell/ai-workflow-kit.git
```

This adds `workflow` to your PATH. You only run this **once**, then use `workflow` anywhere.

### Option 2: Run Without Installing

Use `uvx` to run the tool directly without permanent installation:

```bash
uvx --from git+https://github.com/timjmitchell/ai-workflow-kit.git workflow init .
```

This downloads, runs, and caches the tool. Good for trying it out or occasional use.

## Usage

### Initialize a Repository

Once installed, use `workflow init` to set up any repo with AI workflow tools:

```bash
# Navigate to your project
cd /path/to/your/project

# Full setup (commands + experiments + spec-kit)
workflow init .

# Or specify a path
workflow init /path/to/repo
```

This copies the following into your project:
- `.claude/commands/` - Claude Code slash commands
- `experiments/template/` - Docker experiment framework

#### Options

```bash
# Skip spec-kit integration
workflow init . --no-speckit

# Skip experiments framework
workflow init . --no-experiments

# Overwrite existing files
workflow init . --force
```

### What Gets Added

After running `workflow init`, your project will have:

**Claude Code Commands** (`.claude/commands/`):
- `/prime` - Prime Claude with context about your codebase
- `/prep-parallel-experiments <name> <count>` - Set up parallel Docker experiments
- `/execute-parallel-experiments <name>` - Run experiments and compare results

**Spec-kit Commands** (if enabled):
- `/speckit.constitution` - Establish project principles
- `/speckit.specify` - Create requirements
- `/speckit.plan` - Technical architecture
- `/speckit.tasks` - Generate task list
- `/speckit.implement` - Execute implementation

**Experiments Framework** (`experiments/`):
- `template/` - Base Docker setup to copy for each experiment

### Other CLI Commands

```bash
# See what templates are available
workflow list-templates

# Check version
workflow version
```

## Upgrading

When you want to get the latest version:

```bash
uv tool install ai-workflow-kit --force --from git+https://github.com/timjmitchell/ai-workflow-kit.git
```

The `--force` flag overwrites the existing installation.

**Note**: Upgrading only updates the `workflow` CLI tool itself. Projects you've already initialized keep their copied files - you'd need to re-run `workflow init . --force` to update them.

## Hybrid Workflow

Combine spec-kit's structured thinking with empirical validation:

```
/speckit.constitution     → Project principles
/speckit.specify          → Requirements (what/why)
/speckit.clarify          → Resolve ambiguities
/speckit.plan             → Architecture options
        ↓
/prep-parallel-experiments  → Test different approaches
/execute-parallel-experiments → Compare results, pick winner
        ↓
/speckit.tasks            → Generate tasks using validated approach
/speckit.implement        → Build with confidence
```

## Customization

After init, customize the templates for your project:

1. **Edit `.claude/commands/prime.md`** - Add your project's key files
2. **Edit `experiments/template/run.py`** - Your experiment logic
3. **Edit `experiments/template/requirements.txt`** - Experiment dependencies
4. **Edit `experiments/template/docker-compose.yml`** - Container configuration
