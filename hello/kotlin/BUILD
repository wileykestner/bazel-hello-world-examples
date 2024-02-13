load("@io_bazel_rules_kotlin//kotlin:jvm.bzl", "kt_jvm_binary", "kt_jvm_library")

kt_jvm_library(
    name = "hello-world_lib",
    srcs = ["Hello.kt"],
)

kt_jvm_binary(
    name = "hello-world",
    main_class = "example.HelloKt",
    runtime_deps = [":hello-world_lib"],
)

