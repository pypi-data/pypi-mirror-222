from __future__ import annotations

import asyncio
from abc import ABC, abstractmethod

from cardsharp.blackjack.action import Action


class IOInterface(ABC):
    """
    Abstract base class for an IO interface.

    Methods
    -------
    @abstractmethod
    async def output(self, message: str):
        Output a message to the interface.

    @abstractmethod
    async def get_player_action(self, player: "Actor"):
        Retrieve an action from a player.

    @abstractmethod
    async def check_numeric_response(self, ctx):
        Check if a response is numeric.
    """

    @abstractmethod
    async def output(self, message: str):
        pass

    @abstractmethod
    async def get_player_action(
        self, player: "Actor", valid_actions: list[Action]  # type: ignore # noqa: F821
    ) -> Action:
        pass

    @abstractmethod
    async def check_numeric_response(self, ctx):
        pass


class DummyIOInterface(IOInterface):
    """
    A dummy IO interface for simulation purposes. Does not perform any actual IO.

    Methods
    -------
    def output(self, message):
        Simulates output operation.

    def get_player_action(self, player, actions) -> str:
        Retrieve an action from a player.

    def check_numeric_response(self, response, min_val, max_val):
        Simulates numeric response check.
    """

    async def output(self, message):
        await asyncio.sleep(0)

    async def get_player_action(
        self, player: "Actor", valid_actions: list[Action]  # type: ignore # noqa: F821
    ) -> Action:
        await asyncio.sleep(0)
        return player.decide_action(valid_actions)

    async def check_numeric_response(self, response, min_val, max_val):
        await asyncio.sleep(0)
        return True


class TestIOInterface(IOInterface):
    """
    A test IO interface for testing purposes. Collects output messages and simulates input actions.

    Methods
    -------
    async def output(self, message):
        Collect an output message.

    def add_player_action(self, action: str):
        Add a player action to the queue.

    async def get_player_action(self, player: "Actor") -> str:
        Retrieve an action from a player.

    async def check_numeric_response(self, ctx):
        Simulates numeric response check.

    async def prompt_user_action(self, player: "Actor", valid_actions: list[str]) -> str:
        Prompt a player for an action.
    """

    __test__ = False

    def __init__(self):
        self.sent_messages = []
        self.player_actions = []

    async def output(self, message):
        await asyncio.sleep(0)  # Simulate asynchronous behavior
        self.sent_messages.append(message)

    def add_player_action(self, action: Action):
        self.player_actions.append(action)

    async def get_player_action(
        self, player: "Actor", valid_actions: list[Action]  # type: ignore # noqa: F821
    ) -> Action:
        await asyncio.sleep(0)  # Simulate asynchronous behavior
        if self.player_actions:
            return self.player_actions.pop(0)
        else:
            raise ValueError("No more actions left in TestIOInterface queue.")

    async def check_numeric_response(self, ctx):
        await asyncio.sleep(0)  # Simulate asynchronous behavior
        pass

    async def prompt_user_action(
        self, player: "Actor", valid_actions: list[Action]  # type: ignore # noqa: F821
    ) -> Action:
        await asyncio.sleep(0)  # Simulate asynchronous behavior
        return await self.get_player_action(player, valid_actions)


class ConsoleIOInterface(IOInterface):
    """
    A console IO interface for interactive gameplay.

    Methods
    -------
    def output(self, message: str):
        Output a message to the console.

    async def get_player_action(self, player: "Actor", valid_actions: list[str]):
        Retrieve an action from a player and check if it's valid.

    async def check_numeric_response(self, ctx):
        Check if a response is numeric.
    """

    async def output(self, message: str):
        print(message)

    async def get_player_action(
        self, player: "Actor", valid_actions: list[Action]  # type: ignore # noqa: F821
    ) -> Action:
        attempts = 0
        while attempts < 3:  # Setting a maximum number of attempts
            action_input = input(
                f"{player.name}, it's your turn. What's your action? "
            ).lower()
            await asyncio.sleep(0)  # Simulate asynchronous behavior
            for action in Action:
                if action_input == action.name.lower() and action in valid_actions:
                    return action
            print(
                f"Invalid action, valid actions are: {', '.join([a.name for a in valid_actions])}"
            )
            attempts += 1
        raise Exception("Too many invalid attempts. Game aborted.")

    async def check_numeric_response(self, ctx):
        attempts = 0
        while attempts < 3:  # Setting a maximum number of attempts
            response = input(ctx)
            await asyncio.sleep(0)  # Simulate asynchronous behavior
            try:
                return int(response)
            except ValueError:
                print("Invalid response, please enter a number.")
                attempts += 1
        raise Exception("Too many invalid responses. Operation aborted.")


class LoggingIOInterface(IOInterface):
    """
    A logging IO interface for recording purposes. Writes output messages to a log file.

    Methods
    -------
    async def output(self, message):
        Write an output message to the log file.

    async def get_player_action(self, player: "Actor") -> str:
        Retrieve an action from a player.

    async def check_numeric_response(self, ctx):
        Simulates numeric response check.
    """

    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

    async def output(self, message):
        with open(self.log_file_path, "a") as log_file:
            log_file.write(message + "\n")
        await asyncio.sleep(0)  # Simulate asynchronous behavior

    async def get_player_action(
        self, player: "Actor", valid_actions: list[Action]  # type: ignore # noqa: F821
    ) -> Action:
        await asyncio.sleep(0)
        return player.decide_action(valid_actions)

    async def check_numeric_response(self, ctx):
        await asyncio.sleep(0)  # Simulate asynchronous behavior
        pass
