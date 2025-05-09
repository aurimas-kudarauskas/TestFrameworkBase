from typing import ANY
import pytest

class TestFramewor:
    context = {}
    def __init__(self, path_to_test:str):
        self.path = path_to_test
        TestFramewor.context["hw"] = {}

    def get_hardware_context() -> dict[str,ANY]:
        return TestFramewor.context["hw"]
    
    def get_hardware_by_key(key:str) -> ANY:
        return TestFramewor.context["hw"][key]
    
    def set_hw_context(context: dict[str, ANY]):
        TestFramewor.context["hw"] = context

    def append_context(context: dict[str, ANY]):
        TestFramewor.context.update(context)

    def run_tests(self, extra_args: list[str]):
        return pytest.main([self.path] + extra_args)