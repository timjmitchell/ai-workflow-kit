---
description: Set up parallel Docker-based experiments for A/B testing configurations
argument-hint: <experiment-name> <number-of-variants>
---

# Prepare Parallel Experiments

Set up multiple Docker containers to run the same task with different configurations.

## Variables

Parse from $ARGUMENTS:
- **EXPERIMENT_NAME**: First argument (kebab-case name)
- **NUM_VARIANTS**: Second argument (number of parallel variants, default: 3)

## Pre-flight Checks

1. Validate experiment name is kebab-case
2. Ensure `experiments/template/` exists
3. Verify root `.env` has required credentials
4. Check no existing experiments with this name pattern exist

## Step 1: Create Experiment Branch

```bash
git checkout -b experiment/$EXPERIMENT_NAME-parallel
```

## Step 2: Generate Variant Directories

For each variant (1 to NUM_VARIANTS), create:

```bash
experiments/$EXPERIMENT_NAME-1/
experiments/$EXPERIMENT_NAME-2/
experiments/$EXPERIMENT_NAME-3/
...
```

Each is a copy of the template:

```bash
cp -r experiments/template experiments/$EXPERIMENT_NAME-1
cp -r experiments/template experiments/$EXPERIMENT_NAME-2
# etc.
```

## Step 3: Configure Shared Input

Ask the user to provide the **shared input** that all variants will use.

All variants test the **same input** with **different configurations**.

## Step 4: Configure Variant Differences

For each variant, ask user what to vary. Common options:

| Variant | Example Difference |
|---------|-------------------|
| Variant 1 | Baseline configuration |
| Variant 2 | Alternative model/approach |
| Variant 3 | Different parameters |

Create `.env` for each variant with appropriate overrides from root `.env`.

## Step 5: Update docker-compose Container Names

For each variant, update `docker-compose.yml` to use unique container name:

```yaml
container_name: experiment-$EXPERIMENT_NAME-1
```

This prevents container name conflicts when running in parallel.

## Step 6: Create Parallel Config File

Create `experiments/$EXPERIMENT_NAME-parallel.json`:

```json
{
  "name": "$EXPERIMENT_NAME",
  "variants": [
    {
      "id": 1,
      "path": "experiments/$EXPERIMENT_NAME-1",
      "description": "Baseline"
    },
    {
      "id": 2,
      "path": "experiments/$EXPERIMENT_NAME-2",
      "description": "Variant A"
    },
    {
      "id": 3,
      "path": "experiments/$EXPERIMENT_NAME-3",
      "description": "Variant B"
    }
  ],
  "created": "$(date -Iseconds)"
}
```

## Step 7: Commit Scaffold

```bash
git add experiments/$EXPERIMENT_NAME-*/
git add experiments/$EXPERIMENT_NAME-parallel.json
git commit -m "feat(experiment): scaffold $EXPERIMENT_NAME parallel variants"
```

## Step 8: Report Ready State

Output summary and instructions for running with `/execute-parallel-experiments`.
