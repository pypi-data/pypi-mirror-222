import os


def clear_environment_variables(variable_names: list[str]) -> None:
    """ Clearance of environmental variables """
    for v in variable_names:
        if v in os.environ:
            del os.environ[v]
