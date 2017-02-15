---
title: First Post
author: ben
date: 2017-02-13
template: article.jade
---

Inspired by some online friends, I am going to start posting thoughts and updates here on github, in a static format. This will be nice for archiving and let me host it just about anywhere.

---

Alright, with that out of the way, just what overly complicate way am I doing this?

I thought of doing this as a parody of a lot of the "static" site generators I have seen, but adding in some compiling from source, custom kernels and multiple versions of python for different build processes, but settled for using [Wintersmith](https://github.com/jnordberg/wintersmith) to generate things, and some python (inspired by [Jeff Triplett's personal goals](https://github.com/jefftriplett/personal-goals) ) to push it all live.

### Update.py

```python
from invoke import run, task

@task
def push():
    run('cd /home/bmcnelly/projects/benmcnelly.github.io/slog')
    run('wintersmith build')
    run('cp -R build/* ../')
    run('cp ../articles/now/index.html ../now.html')
    run('git checkout master')
    run('git add -A')
    run('git cia -m "automated push from terminal"')
    run('git push origin master')
    run('open https://benmcnelly.com')
```

I really like that I can see changes live as I work on the template, style or content.

```bash
⟫ wintersmith preview
starting preview server
server running on: http://localhost:8080/
```

I was also inspired to create a "[now](http://benmcnelly.com/now)" page, although I was hoping for a couple more people to branch out the list of people it was inspired by, I couldn't wait for that to happen to implement it.