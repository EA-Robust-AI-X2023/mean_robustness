"""
# Models

This module contains a collection of additional models to be used for experiments.
"""

def register_model_in_byzfl(model_cls: type):
    """Monkeypatch `byzfl` by registering a custom model architecture.
    
    # Example

    ```python
    from torch import nn
    from byzfl import Client

    from mero.models import register_model_in_byzfl

    # Any imported model or even a custom model architecture
    class MyNetwork(nn.Module):
        ...

    register_model_in_byzfl(MyNetwork)

    # The registered model can be used as follows:
    client = Client({
        "model_name": "MyNetwork",
        ...
    })
    ```
    """
    import byzfl.fed_framework.models as models
    setattr(models, model_cls.__name__, model_cls)