from fabric import task
import os

HERE = os.path.split(__file__)[0]

PWD = os.environ.get("PWD")
MYDIR = os.path.split(PWD)[1]


@task
def sync(c):
    c.run(f"""
        cd {HERE}/htdocs
        aws --profile=martin.virtel@dpa-info.com --region=eu-central-1 \
            s3 sync --acl=public-read  \
            ./ s3://dpa-newslab-prototype-webspace/dpa-stories/embed/ --exclude='node_modules/*'
    """)



@task
def introspect(c):
    from IPython import embed
    embed()


