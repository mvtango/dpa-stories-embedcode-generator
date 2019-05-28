from invoke import task
import os
import socket

HERE = os.path.split(__file__)[0]

PWD = os.environ.get("PWD")
MYDIR = os.path.split(PWD)[1]

def highport():
    s=socket.socket()
    s.bind(("", 0))
    port = s.getsockname()[1]
    s.close()
    return port


@task
def sync(c):
    c.run(f"""
        cd {HERE}/htdocs
        aws --profile=martin.virtel@dpa-info.com --region=eu-central-1 \
            s3 sync --acl=public-read  \
            ./ s3://dpa-newslab-prototype-webspace/dpa-stories/embed/ --exclude='node_modules/*'
    """)


@task
def serve(c):

    PORT=highport()

    c.run(f"""

        cd {HERE}
        {{
          sleep 4
          echo opening browser
          xdg-open http://localhost:{PORT}
        }} &
        livereload --port {PORT} htdocs/


    """)

@task
def introspect(c):
    from IPython import embed
    embed()


