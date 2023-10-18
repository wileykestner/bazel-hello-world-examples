def friend_provider_impl(ctx):
    python_source_file_output = ctx.actions.declare_file("{}_friend_provider.py".format(ctx.attr.name))
    ctx.actions.expand_template(
        output = python_source_file_output,
        template = ctx.file._template,
        substitutions = {
            "{NAMES}": ", ".join(['"{}"'.format(friend) for friend in ctx.attr.friends]),
            "{KLASS}": ctx.attr.name.capitalize(),
        }
    )
    return DefaultInfo(files = depset([python_source_file_output]))


dynamic_friend_provider = rule(
    implementation = friend_provider_impl,
    attrs = {
        "friends": attr.string_list(mandatory = True),
        "_template": attr.label(default = "dynamic_friend_provider.tmpl", allow_single_file = True)
    }
)
