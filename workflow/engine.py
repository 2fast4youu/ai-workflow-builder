"""AI workflow engine."""
from typing import List, Dict
from dataclasses import dataclass, field

@dataclass
class Step:
    name: str
    prompt: str
    depends_on: List[str] = field(default_factory=list)
    def execute(self, ctx):
        p = self.prompt
        for k,v in ctx.items():
            p = p.replace("{"+k+"}", str(v))
        return f"[{self.name}]"

@dataclass
class Workflow:
    name: str
    steps: List[Step] = field(default_factory=list)
    def add_step(self, name, prompt, depends_on=None, **kw):
        self.steps.append(Step(name=name, prompt=prompt, depends_on=depends_on or [], **kw))
    def run(self, **ctx):
        results = {}
        for s in self.steps:
            for d in s.depends_on:
                ctx[d] = results[d]
            results[s.name] = s.execute(ctx)
            ctx[s.name] = results[s.name]
        return results
