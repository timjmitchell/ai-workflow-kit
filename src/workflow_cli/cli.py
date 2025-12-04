"""CLI commands for AI Workflow Kit."""

import subprocess
import shutil
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.panel import Panel

app = typer.Typer(
    name="workflow",
    help="AI workflow toolkit for Claude Code projects",
    add_completion=False,
)
console = Console()


def get_templates_dir() -> Path:
    """Get the templates directory from the package."""
    return Path(__file__).parent / "templates"


@app.command()
def init(
    path: str = typer.Argument(".", help="Target directory to initialize"),
    with_experiments: bool = typer.Option(
        True, "--experiments/--no-experiments", help="Include experiment framework"
    ),
    with_speckit: bool = typer.Option(
        True, "--speckit/--no-speckit", help="Initialize spec-kit"
    ),
    force: bool = typer.Option(
        False, "--force", "-f", help="Overwrite existing files"
    ),
):
    """Initialize AI workflow in a repository.

    Sets up:
    - Claude Code commands (prime, parallel experiments)
    - Experiment framework (Docker-based A/B testing)
    - Spec-kit integration (optional)
    """
    target = Path(path).resolve()
    templates = get_templates_dir()

    if not target.exists():
        target.mkdir(parents=True)

    console.print(Panel(
        f"[bold]AI Workflow Kit[/bold]\n\n"
        f"Target: {target}\n"
        f"Experiments: {'Yes' if with_experiments else 'No'}\n"
        f"Spec-kit: {'Yes' if with_speckit else 'No'}",
        title="Initializing",
    ))

    # Copy .claude commands
    claude_src = templates / ".claude"
    claude_dest = target / ".claude"

    if claude_dest.exists() and not force:
        # Merge: only copy commands directory
        commands_dest = claude_dest / "commands"
        commands_dest.mkdir(parents=True, exist_ok=True)
        for cmd_file in (claude_src / "commands").glob("*.md"):
            dest_file = commands_dest / cmd_file.name
            if not dest_file.exists() or force:
                shutil.copy2(cmd_file, dest_file)
                console.print(f"  [green]✓[/green] Added {cmd_file.name}")
            else:
                console.print(f"  [yellow]→[/yellow] Skipped {cmd_file.name} (exists)")
    else:
        shutil.copytree(claude_src, claude_dest, dirs_exist_ok=True)
        console.print("  [green]✓[/green] Added .claude/commands/")

    # Copy experiments framework
    if with_experiments:
        exp_src = templates / "experiments"
        exp_dest = target / "experiments"

        if exp_dest.exists() and not force:
            console.print("  [yellow]→[/yellow] Skipped experiments/ (exists)")
        else:
            shutil.copytree(exp_src, exp_dest, dirs_exist_ok=True)
            console.print("  [green]✓[/green] Added experiments/template/")

    # Initialize spec-kit
    if with_speckit:
        console.print("  [blue]...[/blue] Initializing spec-kit...")
        try:
            result = subprocess.run(
                ["specify", "init", ".", "--force", "--ai", "claude", "--ignore-agent-tools"],
                cwd=target,
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                console.print("  [green]✓[/green] Spec-kit initialized")
            else:
                console.print(f"  [red]✗[/red] Spec-kit failed: {result.stderr}")
        except FileNotFoundError:
            console.print("  [yellow]![/yellow] Spec-kit not installed (run: uv tool install specify-cli --from git+https://github.com/github/spec-kit.git)")

    # Summary
    console.print(Panel(
        "[bold green]Setup complete![/bold green]\n\n"
        "Available commands:\n"
        "  /prime - Prime context for the codebase\n"
        "  /prep-parallel-experiments - Set up parallel experiments\n"
        "  /execute-parallel-experiments - Run and compare experiments\n"
        + ("\n  /speckit.* - Spec-driven development commands" if with_speckit else ""),
        title="Done",
    ))


@app.command()
def version():
    """Show version information."""
    from . import __version__
    console.print(f"ai-workflow-kit v{__version__}")


@app.command()
def list_templates():
    """List available templates."""
    templates = get_templates_dir()

    console.print("[bold]Available templates:[/bold]\n")

    # Commands
    commands = templates / ".claude" / "commands"
    if commands.exists():
        console.print("[blue]Commands (.claude/commands/):[/blue]")
        for f in sorted(commands.glob("*.md")):
            console.print(f"  - {f.stem}")

    # Experiments
    experiments = templates / "experiments"
    if experiments.exists():
        console.print("\n[blue]Experiments (experiments/):[/blue]")
        console.print("  - template/ (Docker-based experiment framework)")


if __name__ == "__main__":
    app()
