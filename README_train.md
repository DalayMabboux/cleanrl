# AI Train routing 
Added: ./cleanrl/ppo_train.py
Outcome example: ./cleanrl/runs/traintrack_env/Railway-v0__ppo_train__1__1743834889/ppo_train.cleanrl_model

```
Problem (ähnlich):
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/home/USER/venvs/torchgpu/lib/python3.10/site-packages/torch/__init__.py", line 239, in <module>
        from torch._C import *  # noqa: F403
    ImportError: /home/USER/venvs/torchgpu/lib/python3.10/site-packages/torch/lib/../../nvidia/cusparse/lib/libcusparse.so.12: undefined symbol: __nvJitLinkAddData_12_1, version libnvJitLink.so.12

Lösung:
    https://github.com/pytorch/pytorch/issues/111469
    Das habe ich gemacht:
        python -m pip uninstall torch
        python -m pip install --pre torch --index-url https://download.pytorch.org/whl/nightly/cu121
```