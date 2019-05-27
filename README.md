# repo2charliecloud

Wrapper around repo2docker producing charliecloud compatible tarballs

## What is repo2docker?

[repo2docker](https://repo2docker.readthedocs.io/) takes a repository
as input, and applies some heuristics to build a docker image that
runs from it. It doesn't require a `Dockerfile` - instead it looks
for language standard files (such as `requirements.txt`, `environment.yml`,
`REQUIRE`, etc) and automatically sets up appropriate environment
for it. It has built in support for Python, R, Julia, NixOS, etc.

The popular [mybinder.org](https://mybinder.org) services uses
repo2docker to build images and launch them interactively for
users. Click the link below to try out a sample

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/yuvipanda/requirements/98744e8f91132a5f875da6fa08d7e6595da8ce9e)

## What is Charliecloud?

[Charliecloud](https://hpc.github.io/charliecloud/) is a lightweight
container runtime targeted at HPC systems. It is an open source project
from the [Los Alamos National Lab](https://www.lanl.gov)>

## What is repo2charliecloud?

It's a wrapper around repo2docker that produces tarballs that can be
run by charliecloud. 

## Demo

### Building the container image

Building images still requires docker, so you'd do it on your
laptop.

[![asciicast](https://asciinema.org/a/N9lb1rJJ7IAFnqUn9ONMquKea.svg)](https://asciinema.org/a/N9lb1rJJ7IAFnqUn9ONMquKea)

### Running the container image

Running the image doesn't require docker, and has very [minimal
dependencies](https://hpc.github.io/charliecloud/install.html#run-time).

[![asciicast](https://asciinema.org/a/248542.svg)](https://asciinema.org/a/248542)

## Installation

You can install repo2charliecloud with:

```
pip install repo2charliecloud
```

This will automatically install charliecloud with the 
[charliecloud-bin](https://github.com/yuvipanda/charliecloud-bin)
project.

## Usage

Once installed, it can be invoked with

```
repo2charliecloud <git-url> --ref <optional-ref>
```

`<git-url>` is the required parameter, and should point to
a cloneable git repository. Local directories are also supported,
and we can support non-git local directories.

`--ref` points to an optional git ref to build. It defaults to
`master` but you can specify a branch, tag or commit hash for
better reproducibility.

Running this will output a `.tar.gz` file in the current directory.

You can then [transfer](https://hpc.github.io/charliecloud/tutorial.html#distribute-tarball), [unpack](https://hpc.github.io/charliecloud/tutorial.html#distribute-tarball)
and [run](https://hpc.github.io/charliecloud/tutorial.html#unpack-tarball)
the image as you would any other image with charliecloud.

## What's next?

Lots, but first this needs a few more Weird Al references.