load("@build_bazel_rules_swift//swift:swift.bzl", "swift_binary", "swift_library")

swift_binary(
    name = "hello-world",
    srcs = ["hello.swift", ":dynamic"],
    deps = [":hello-world_lib"],
)

swift_library(
    name = "hello-world_lib",
    module_name = "Names",
    srcs = ["names.swift"],
)

genrule(
    name = "dynamic",
    cmd = """echo 'struct GeneratedCode { func main() { print("hello generated!") } }' > $@""",
    outs = ["dynamic.swift"],
)