# Experiments Framework

Parallel experimentation framework for A/B testing different approaches.

## Quick Start

1. **Set up parallel experiments:**
   ```
   /prep-parallel-experiments my-test 3
   ```

2. **Configure each variant** with different settings in their `.env` files

3. **Run all variants:**
   ```
   /execute-parallel-experiments my-test
   ```

4. **Review results** in `experiments/my-test-COMPARISON.md`

## Directory Structure

```
experiments/
├── template/           # Base template for new experiments
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── run.py          # Main experiment runner
│   ├── requirements.txt
│   ├── .env.example
│   └── PLAN.md
├── my-test-1/          # Variant 1
├── my-test-2/          # Variant 2
├── my-test-3/          # Variant 3
├── my-test-parallel.json
└── my-test-COMPARISON.md
```

## Customization

1. Edit `template/run.py` for your experiment logic
2. Add dependencies to `template/requirements.txt`
3. Configure environment variables in `.env`
