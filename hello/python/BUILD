load("//hello/python:dynamic.bzl", "dynamic_friend_provider")
load("@rules_python//python:py_binary.bzl", "py_binary")
load("@rules_python//python:py_library.bzl", "py_library")
load("@rules_python//python:py_test.bzl", "py_test")

py_binary(
    name = "hello-world",
    srcs = ["hello.py", ":mobile",],
    main = "hello.py",
    deps = [
        ":friends",
        ":executive_friends",
    ]
)

py_library(
    name = "friends",
    srcs = ["friend_provider.py"],
)

py_library(
    name = "executive_friends",
    srcs = ["executive_friend_provider.py"],
    deps = [":friends"],
)

dynamic_friend_provider(
    name = "mobile",
    friends = [
        "Jesse",
        "Matt",
        "Mike",
        "Daian",
        "Elton",
        "Eli",
        "Jade",
        "Matt",
        "Sherry",
        "Uriel",
    ]
)

py_test(
    name = "executive_friends_test",
    srcs = ["test_executive_friends.py"],
    main = "test_executive_friends.py",
    deps = [":executive_friends"],
)
