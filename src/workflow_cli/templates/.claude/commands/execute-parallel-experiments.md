---
description: Run parallel Docker experiments and compare results
argument-hint: <experiment-name>
---

# Execute Parallel Experiments

Run all variants of a parallel experiment simultaneously using Docker containers.

## Variables

- **EXPERIMENT_NAME**: $ARGUMENTS (the experiment name used with prep-parallel-experiments)

## Pre-flight Checks

1. Verify `experiments/$EXPERIMENT_NAME-parallel.json` exists
2. Read the parallel config to get variant paths
3. Ensure all variant directories exist with `.env` files
4. Check Docker daemon is running

## Step 1: Read Parallel Config

```bash
cat experiments/$EXPERIMENT_NAME-parallel.json
```

Parse the variants array to get all paths.

## Step 2: Launch All Containers in Parallel

Run Docker commands in parallel using background processes:

```bash
(cd experiments/$EXPERIMENT_NAME-1 && docker compose up --abort-on-container-exit) &
(cd experiments/$EXPERIMENT_NAME-2 && docker compose up --abort-on-container-exit) &
(cd experiments/$EXPERIMENT_NAME-3 && docker compose up --abort-on-container-exit) &
wait
```

## Step 3: Wait for All Containers

Monitor until all containers complete. Check exit codes for failures.

## Step 4: Collect Results

For each variant, read:
- `experiments/$EXPERIMENT_NAME-N/results/results.json`
- `experiments/$EXPERIMENT_NAME-N/results/` (any output files)

## Step 5: Generate Comparison Report

Create `experiments/$EXPERIMENT_NAME-COMPARISON.md`:

```markdown
# Parallel Experiment Results: $EXPERIMENT_NAME

## Overview

| Variant | Description | Status | Duration |
|---------|-------------|--------|----------|
| 1 | [description] | ✅/❌ | [time] |
| 2 | [description] | ✅/❌ | [time] |
| 3 | [description] | ✅/❌ | [time] |

## Configuration Differences

| Setting | Variant 1 | Variant 2 | Variant 3 |
|---------|-----------|-----------|-----------|
| [key] | [val] | [val] | [val] |

## Results Comparison

[Compare outputs from each variant]

## Observations

- [Notable differences]
- [Which performed better and why]

## Recommendation

Based on results, **Variant N** appears to be the best approach because:
- [Reason 1]
- [Reason 2]
```

## Step 6: Cleanup Containers

```bash
(cd experiments/$EXPERIMENT_NAME-1 && docker compose down -v) &
(cd experiments/$EXPERIMENT_NAME-2 && docker compose down -v) &
(cd experiments/$EXPERIMENT_NAME-3 && docker compose down -v) &
wait
```

## Step 7: Commit Results

```bash
git add experiments/$EXPERIMENT_NAME-*/results/
git add experiments/$EXPERIMENT_NAME-COMPARISON.md
git commit -m "feat(experiment): add $EXPERIMENT_NAME parallel results"
```

## Step 8: Ask User for Next Steps

Present options:

1. **Create PR** - Push branch and create pull request with comparison
2. **Re-run specific variant** - Modify and re-run one configuration
3. **Adopt winner** - Apply winning configuration as default
4. **Discard** - Clean up all experiment files
