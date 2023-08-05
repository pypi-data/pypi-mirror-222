# Copyright 2020 Karlsruhe Institute of Technology
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

import click
from flask.cli import FlaskGroup
from flask.cli import routes_command
from flask.cli import ScriptInfo
from flask.cli import shell_command
from flask_limiter.commands import cli as limiter_command
from flask_migrate.cli import db as migrations_command

import kadi.lib.constants as const
from .utils import echo
from kadi import __version__
from kadi.app import create_app


# Command groups that are only available in dev environments.
DEV_ONLY_COMMANDS = ["assets", "i18n", "limiter", "migrations", "routes", "run"]


class KadiGroup(FlaskGroup):
    """Click group for use in custom commands.

    Automatically makes commands run inside an application context. Wraps Flask's own
    custom Click group.
    """

    def __init__(self, **kwargs):
        super().__init__(
            add_default_commands=False,
            add_version_option=False,
            set_debug_flag=False,
            create_app=create_app,
            **kwargs,
        )

        # Set a global flag that indicates that the app was created from the CLI.
        os.environ[const.VAR_CLI] = "1"

        def _print_version(ctx, param, value):
            if not value or ctx.resilient_parsing:
                return

            echo(__version__)
            ctx.exit()

        # Also removes the global parameters added by Flask.
        self.params = [
            click.Option(
                ["--version"],
                help="Print the Kadi version and exit.",
                is_flag=True,
                is_eager=True,
                expose_value=False,
                callback=_print_version,
            )
        ]

    def _load_plugin_commands(self):
        pass

    def get_command(self, ctx, name):
        command = super().get_command(ctx, name)

        info = ctx.ensure_object(ScriptInfo)
        app = info.load_app()

        if app.environment != const.ENV_DEVELOPMENT and name in DEV_ONLY_COMMANDS:
            return None

        return command


@click.group(cls=KadiGroup)
def kadi():
    """The Kadi command line interface."""


# Adjust the help output of some extension commands.
limiter_command.help = "Wrapper command for Flask-Limiter."
migrations_command.help = "Wrapper command for Flask-Migrate."


kadi.add_command(limiter_command, name="limiter")
kadi.add_command(migrations_command, name="migrations")
kadi.add_command(routes_command)
kadi.add_command(shell_command)


# pylint: disable=unused-import


from .commands.assets import assets
from .commands.celery import celery
from .commands.db import db
from .commands.files import files
from .commands.i18n import i18n
from .commands.run import run
from .commands.search import search
from .commands.users import users
from .commands.utils import utils
