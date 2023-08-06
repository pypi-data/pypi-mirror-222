from __future__ import annotations

from marshmallow import Schema, RAISE, fields

from argrelay.custom_integ.GitRepoBasePathConfigSchema import git_repo_base_path_config_desc
from argrelay.misc_helper.TypeDesc import TypeDesc

is_plugin_enabled_ = "is_plugin_enabled"
load_repo_commits_ = "load_repo_commits"
base_paths_ = "base_paths"


class GitRepoLoaderConfigSchema(Schema):
    class Meta:
        unknown = RAISE
        strict = True

    is_plugin_enabled = fields.Boolean()

    load_repo_commits = fields.Boolean()

    base_paths = fields.List(
        fields.Nested(git_repo_base_path_config_desc.dict_schema),
        required = True,
    )


git_repo_loader_config_desc = TypeDesc(
    dict_schema = GitRepoLoaderConfigSchema(),
    ref_name = GitRepoLoaderConfigSchema.__name__,
    dict_example = {
        is_plugin_enabled_: False,
        load_repo_commits_: False,
        base_paths_: [
            git_repo_base_path_config_desc.dict_example,
        ],
    },
    default_file_path = "",
)
