load("//examples/hello/python:dynamic.bzl", "dynamic_friend_provider")

py_binary(
    name = "hello-world",
    srcs = ["hello.py", ":school",],
    main = "hello.py",
    deps = [
        ":friends",
        ":work_friends",
    ]
)

py_library(
    name = "friends",
    srcs = ["friend_provider.py"],
)

py_library(
    name = "work_friends",
    srcs = ["work_friend_provider.py"],
    deps = [":friends"],
)

dynamic_friend_provider(
    name = "school",
    friends = [
        "Alice",
        "Bob",
        "Chester",
        "Sherry",
    ]
)
