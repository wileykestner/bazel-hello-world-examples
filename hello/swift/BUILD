load("@build_bazel_rules_swift//swift:swift.bzl", "swift_binary", "swift_library")

swift_binary(
    name = "hello-world",
    srcs = ["hello.swift", ":dynamic"],
    deps = [":people"],
)

swift_library(
    name = "people",
    module_name = "People",
    srcs = ["people.swift"],
)

genrule(
    name = "dynamic",
    cmd = """echo 'struct GeneratedCode { func main() { print("hello generated!") } }' > $@""",
    outs = ["dynamic.swift"],
)