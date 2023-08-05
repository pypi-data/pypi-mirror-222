from typing import Literal

from powerpwn.machinepwn.enums.command_to_run_enum import CommandToRunEnum
from powerpwn.machinepwn.models.cmd_arguments import CommandArguments
from powerpwn.machinepwn.models.command_args_properties_base_model import CommandArgsPropertiesBaseModel


class StealPowerAutomateTokenCommandArgs(CommandArguments[CommandArgsPropertiesBaseModel]):
    command_to_run: Literal[CommandToRunEnum.STEAL_POWER_AUTOMATE_TOKEN] = CommandToRunEnum.STEAL_POWER_AUTOMATE_TOKEN
