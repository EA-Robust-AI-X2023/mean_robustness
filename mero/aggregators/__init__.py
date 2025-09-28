"""
# Robust aggregators

This module contains a collection of additional robust aggregators that are compatible
with `byzfl`.

## Available aggregators

- **`FABA`**: An algorithm that iteratively removes outliers.
- **`LFighter`**: A clustering-based defense against label-flipping attacks.


## Usage

```python
import mero.aggregators
# LFighter is now registered in byzfl!
from byzfl.aggregators.aggregators import FABA, LFighter

server = Server({
    ...,
    "aggregator_info": {"name": "LFighter", "parameters": ...},
    ...
})
```
"""

import byzfl.fed_framework.robust_aggregator as robust_aggregator

from .faba import FABA
from .lfighter import LFighter

__all__ = [
    'FABA',
    'LFighter',
    'register_aggregator_in_byzfl',
]

def register_aggregator_in_byzfl(aggregator_cls: type):
    """Monkeypatch `byzfl` by registering a custom aggregator.

    # Examples

    Register a third-party aggregator in `byzfl`:

    ```python
    from torch import nn
    from byzfl import Server

    from mero.models import register_aggregator_in_byzfl

    class MyAggregator:
        ...

    register_aggregator_in_byzfl(MyAggregator)

    # The registered aggregator can be used as follows:
    server = Server({
        ...,
        "aggregator_info": {"name": "MyAggregator", "parameters": ...},
        ...
    })
    ```
    """
    setattr(robust_aggregator.aggregators, aggregator_cls.__name__, aggregator_cls)

register_aggregator_in_byzfl(FABA)
register_aggregator_in_byzfl(LFighter)
