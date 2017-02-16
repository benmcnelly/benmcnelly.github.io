from invoke import task, run

@task
def push(ctx):
    ctx.run('echo root update!''')
    ctx.run('git add -A')
    ctx.run('git commit -m "automated push from terminal" ')
    ctx.run('git push -f origin master')
