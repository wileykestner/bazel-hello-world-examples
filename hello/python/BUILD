load("//hello/python:dynamic.bzl", "dynamic_friend_provider")

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
