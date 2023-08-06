from __future__ import annotations

from marshmallow import Schema, RAISE, fields

from argrelay.misc_helper.TypeDesc import TypeDesc

base_path_ = "base_path"
repo_aliases_ = "repo_aliases"


class GitRepoBasePathConfigSchema(Schema):
    class Meta:
        unknown = RAISE
        strict = True

    base_path = fields.String()

    # Map key as `GitRepoRelPath` to value as `GitRepoAlias`:
    repo_aliases = fields.Dict(
        keys = fields.String(),
        values = fields.String(),
        required = True,
    )


git_repo_base_path_config_desc = TypeDesc(
    dict_schema = GitRepoBasePathConfigSchema(),
    ref_name = GitRepoBasePathConfigSchema.__name__,
    dict_example = {
        base_path_: "~",
        repo_aliases_: {
            "argrelay.git": "ar",
        }
    },
    default_file_path = "",
)
