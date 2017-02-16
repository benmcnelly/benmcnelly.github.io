---
title: First Post
author: ben
date: 2017-02-13
template: article.jade
---

Inspired by some online friends, I am going to start posting thoughts and updates here on github, in a static format. This will be nice for archiving and let me host it just about anywhere.

---

Alright, with that out of the way: In just what overly complicated way should I do this static site?

I thought of doing this as a parody of a lot of the "static" site generators I have seen, but adding in some compiling from source, custom kernels, and multiple versions of python for different build processes; but settled for using [Wintersmith](https://github.com/jnordberg/wintersmith) to generate things, and some python (inspired by [Jeff Triplett's personal goals](https://github.com/jefftriplett/personal-goals) ) to push it all live.

### tasks.py

```python
from invoke import task, run

@task
def push(ctx):
    ctx.run('echo UNGH!''')
    ctx.run('wintersmith build')
    ctx.run('cp -R build/* ../')
    ctx.run('cp ../articles/now/index.html ../now.html')
    ctx.run('git add -A')
    ctx.run('git commit -m "automated push from terminal" ')
    ctx.run('git push -f origin master')
    ctx.run('firefox http://github.benmcnelly.com')
    ctx.run('firefox https://github.com/benmcnelly/benmcnelly.github.io')
```

I really like that I can see changes live as I work on the template, style or content.

```bash
⟫ wintersmith preview
starting preview server
server running on: http://localhost:8080/
```

I was also inspired to create a "[now](http://github.benmcnelly.com/now)" page, although I was hoping for a couple more people to branch out the list of people it was inspired by, I couldn't wait for that to happen to implement it.
