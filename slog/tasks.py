from invoke import task, run

@task
def push(ctx):
    ctx.run('echo UNGH!''')
    ctx.run('wintersmith build')
    ctx.run('cp -R build/* ../')
    ctx.run('cp ../articles/now/index.html ../now.html')
    ctx.run('cd ..')
    ctx.run('git add -A')
    ctx.run('git commit -m "automated push from terminal" ')
    ctx.run('git push -f origin master')
    ctx.run('firefox http://github.benmcnelly.com')
    ctx.run('firefox https://github.com/benmcnelly/benmcnelly.github.io')
