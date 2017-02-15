from invoke import run, task

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
