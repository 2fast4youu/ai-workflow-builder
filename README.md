# AI Workflow Builder

Orchestrate AI workflows with Python.

```python
from workflow import Workflow
wf = Workflow(name="Pipeline")
wf.add_step("extract", prompt="Extract: {text}")
result = wf.run(text="Hello")
```
