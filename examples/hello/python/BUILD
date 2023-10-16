py_binary(
    name = "hello-world",
    srcs = ["hello.py"],
    main = "hello.py",
    deps = [
        ":friends",
        ":work_friends",
        ":school_friends",
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

py_library(
    name = "school_friends",
    srcs = ["school_friend_provider.py"],
    deps = [":friends"],
)
