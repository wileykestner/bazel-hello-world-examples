# bazel-hello-world-examples

## Requirements

* Install bazelisk on MacOS using homebrew:

`brew install bazelisk`

## Running the examples

See all binary (executable) targets with:

`bazelisk query 'kind(binary, ...)'`

Run any of those targets with: `bazel run <target label>`

For example:

`bazelisk run //examples/hello/c:hello-world`
