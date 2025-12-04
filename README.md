# AI Workflow Kit

A CLI toolkit for setting up AI-assisted development workflows across repositories.

## Features

- **Claude Code Commands**: Prime context, parallel experiments
- **Experiment Framework**: Docker-based A/B testing for different approaches
- **Spec-kit Integration**: Optional spec-driven development setup

## Installation

```bash
# One-time install (recommended)
uv tool install ai-workflow-kit --from git+https://github.com/YOUR_USERNAME/ai-workflow-kit.git

# Or run without installing
uvx --from git+https://github.com/YOUR_USERNAME/ai-workflow-kit.git workflow init .
```

## Usage

### Initialize a Repository

```bash
# Full setup (commands + experiments + spec-kit)
workflow init /path/to/repo

# Without spec-kit
workflow init . --no-speckit

# Without experiments
workflow init . --no-experiments

# Force overwrite existing files
workflow init . --force
```

### Available Commands After Init

**Claude Code Commands:**
- `/prime` - Prime context for the codebase
- `/prep-parallel-experiments <name> <count>` - Set up parallel experiments
- `/execute-parallel-experiments <name>` - Run and compare experiments

**Spec-kit Commands (if enabled):**
- `/speckit.constitution` - Establish project principles
- `/speckit.specify` - Create requirements
- `/speckit.plan` - Technical architecture
- `/speckit.tasks` - Generate task list
- `/speckit.implement` - Execute implementation

### Other CLI Commands

```bash
# List available templates
workflow list-templates

# Show version
workflow version
```

## Hybrid Workflow

Combine spec-kit's structured thinking with empirical validation:

```
/speckit.constitution     → Project principles
/speckit.specify          → Requirements (what/why)
/speckit.clarify          → Resolve ambiguities
/speckit.plan             → Architecture options
        ↓
/prep-parallel-experiments  → Test approaches
/execute-parallel-experiments → Compare results
        ↓
/speckit.tasks            → Tasks using validated approach
/speckit.implement        → Build with confidence
```

## Customization

After init, customize for your project:

1. **Edit `.claude/commands/prime.md`** - Add your key files
2. **Edit `experiments/template/run.py`** - Your experiment logic
3. **Edit `experiments/template/requirements.txt`** - Dependencies

## Upgrading

```bash
uv tool install ai-workflow-kit --force --from git+https://github.com/YOUR_USERNAME/ai-workflow-kit.git
```

## Requirements

- Python 3.11+
- uv package manager
- Docker (for experiments)
- spec-kit (optional, for spec-driven commands)
