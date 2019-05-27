import subprocess
import argparse
from urllib.parse import urlparse
from repo2docker.app import Repo2Docker

def resolve_ref(repo_url, ref):
    """
    Return resolved commit hash for branch / tag.

    Return ref unmodified if branch / tag isn't found
    """
    stdout = subprocess.check_output(
        ['git', 'ls-remote', repo_url]
    ).decode()
    # ls-remote output looks like this:
    # <hash>\t<ref>\n
    # <hash>\t<ref>\n
    # Since our ref can be a tag (so refs/tags/<ref>) or branch
    # (so refs/head/<ref>), we get all refs and check if either
    # exists
    all_refs = [l.split('\t') for l in stdout.strip().split('\n')]
    for hash, ref in all_refs:
        if ref in (f'refs/heads/{ref}', f'refs/heads/{ref}'):
            return hash

    if stdout:
        return stdout.split()[0]
    return ref

def readable_image_name(repo, resolved_ref):
    """
    Make a readable image name for repo and ref.

    This *is* going to cause collisions!
    """
    parts = urlparse(repo)
    return '{}-{}:{}'.format(
        parts.netloc,
        parts.path.replace('/', '-'),
        resolved_ref
    )


def main():
    argparser = argparse.ArgumentParser()

    argparser.add_argument(
        'repo',
        help='Repository to build'
    )

    argparser.add_argument(
        '--ref',
        help='Remote repository reference to build. Defaults to master',
        default='master'
    )

    args = argparser.parse_args()

    resolved_ref = resolve_ref(args.repo, args.ref)
    r2d = Repo2Docker()
    r2d.repo = args.repo
    r2d.ref = resolved_ref
    r2d.output_image_spec = readable_image_name(args.repo, resolved_ref)
    # charliecloud doesn't read ENV from r2d
    # so we explicitly save it and load it back
    r2d.appendix = r"""
    USER root
    # Prefixing with 000- means bash -l will source it first
    RUN ln -s /environment /etc/profile.d/000-repo2docker-env.sh
    USER ${NB_USER}
    """

    r2d.initialize()
    r2d.build()
    
    r2d.log.info('Exporting built image to tar\n')
    subprocess.check_call([
        'ch-docker2tar',
        r2d.output_image_spec,
        '.'
    ])

if __name__ == '__main__':
    main()