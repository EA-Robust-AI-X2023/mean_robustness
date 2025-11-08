# mero - Mean Aggregator vs Robust Aggregators

`mero` is a shared Python library. It depends on our [fork of `byzfl`](../byzfl/).

### Directory structure

```bash
└── mero             # Shared Python library for notebooks and scripts
    ├── aggregators  # Implemented gradient aggregators
    ├── attacks      # Data poisoning attacks
    ├── datasets     # Used datasets
    ├── metrics      # Gradient metrics (heterogeneity, disturbance...)
    ├── modeling     # Models and training hyperparameters
    └── plots        # Code for plotting figures
```