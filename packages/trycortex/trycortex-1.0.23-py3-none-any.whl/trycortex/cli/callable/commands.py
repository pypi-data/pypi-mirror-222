from dataclasses import asdict
import functools
import importlib
import pathlib
import re
from typing import List
import click
import validators
import os
import urllib.request
import trycortex
import rich.console as rich_console
from typing import Dict, List, Tuple
import venv
import subprocess
from trycortex.callables.base import Callable
import json
import sys

from trycortex.cli.callable import callable_config
from trycortex.callables import blocks

# Regex pattern to match valid entry points: "module:object"
VAR_NAME_RE = r"(?![0-9])\w+"
ENTRY_POINT_PATTERN = re.compile(rf"^{VAR_NAME_RE}(\.{VAR_NAME_RE})*:{VAR_NAME_RE}$")
VISIBILITY_RE = r"^(Private|private|Public|public|Unlisted|unlisted)$"
VISIBILITY_PATTERN = re.compile(VISIBILITY_RE)
TEMPLATE_RE = r"^(barbone|chat|chat with history)$"
TEMPLATE_PATTERN = re.compile(TEMPLATE_RE)

REQUIREMENTS_TXT = "requirements.txt"
CURRENT_CORTEX_REQUIREMENT = f"trycortex ~= {trycortex.__version__}"
CORTEX_REQUIREMENT_PATTERN = re.compile(r"^\s*trycortex([^\w]|$)")

CALLABLE_TEMPLATE_URL = (
    "https://raw.githubusercontent.com/kinesysai/cortex-py/main/template.py"
)



@click.group(help="Callable-related commands")
def callable():
    pass

def _slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s)
    s = s.strip("-")
    return s

def _update_callable_requirements(
    existing_requirements: List[str], new_requirements: List[str]
) -> List[str]:
    """Returns an updated list of callable requirements to go in requirements.txt."""

    # If the user specified a trycortex requirement, use that.
    cortex_requirement = next(
        filter(
            functools.partial(re.match, CORTEX_REQUIREMENT_PATTERN), new_requirements
        ),
        CURRENT_CORTEX_REQUIREMENT,
    )

    # Ensure that a compatible version of the Cortex SDK is present.
    resolved_requirements: List[str] = []

    for existing_requirement in existing_requirements:
        if (
            re.match(CORTEX_REQUIREMENT_PATTERN, existing_requirement)
            and existing_requirement != cortex_requirement
        ):
            # Ignore any existing (but different) cortex requirements.
            continue

        resolved_requirements.append(existing_requirement)

    for new_requirement in [cortex_requirement] + new_requirements:
        if new_requirement not in resolved_requirements:
            resolved_requirements.append(new_requirement)

    return resolved_requirements

@callable.command("addblock", help="Adds a block to the callable.")
@click.option("--type", help="Type of the block.")
@click.option("--name", help="Name of the block.")
@click.argument("path", required=False)
def add_block(path, type:str, name:str):
    click.echo("add block")
    path = pathlib.Path(path or ".")
    blocks_path = os.path.join(path, "blocks")
    os.makedirs(blocks_path, exist_ok=True)

    if type is None:
        type = click.prompt("Type")

    while name is None or not validators.slug(name):
        if name is not None:
            click.secho("Name can be alpha numerics and dashes only.")
        name = click.prompt("Name")

    block_path = os.path.join(blocks_path, name.upper())
    os.makedirs(block_path, exist_ok=True)
    if type.lower() == "code":
        
        default_code = """\
_fun = (env) => {
  // use `env.state.BLOCK_NAME` to refer output from previous blocks.
 return; 
}
"""
        code_path = os.path.join(block_path, "code.js")
        with open(code_path, "w") as file:
            file.write(default_code)
        
        script_content = """\
from trycortex.callables import blocks
with open('code.js', 'r') as file:
    js_code = file.read()
spec = blocks.CodeSpec(code=js_code)
block = blocks.Block(type=\"""" + type +  """",name=\"""" + name + """", indent=0, spec=spec)
"""
        script_name = name.lower() + ".py"
        script_path = os.path.join(block_path, script_name)
        with open(script_path, "w") as file:
            file.write(script_content)

        main_path = os.path.join(path, "main.py")
        with open(main_path, 'r') as file:
            main_content = file.read()
        import_statement = f"import blocks.{name.upper()}.{name.lower()} as {name.lower()}\n"
        updated_import = import_statement + main_content
        with open(main_path, 'w') as file:
            file.write(updated_import)

    # check what type of block it is
    # create block according to type and name and initialize it
    # create new folder in blocks folder for the new block
    # add a python file initializing the new block



@callable.command("init", help="Creates an callable.yaml file.")
@click.option("--name", help="Name of the callable.")
@click.option("--description", help="Description of the callable.")
@click.option("--visibility", help="Visibility of the callable.")
@click.option("--template", help="Template of the callable.")
@click.option("--entry-point", help="Python entry point of the callable.")
@click.option(
    "--requirement",
    multiple=True,
    type=str,
    help="Additional requirements for requirements.txt. Can be specified multiple times.",
)
@click.argument("path", required=False)
def init_callable(path, name, description, visibility, template, entry_point:str,requirement):
    click.echo("init callable")
    path = pathlib.Path(path or ".")
    path.mkdir(parents=True, exist_ok=True)

    try:
        current_config = callable_config.load_config(path)
    except FileNotFoundError:
        current_config = callable_config.CallableConfig(name=_slugify(path.resolve().name))

    
    while name is None or not validators.slug(name):
        if name is not None:
            click.secho("Name can be alpha numerics, underscores and dashes only.")
        name = click.prompt("Name", default=current_config.name)

    if description is None:
        description = click.prompt("Description", default=current_config.description)

    while entry_point is None or not ENTRY_POINT_PATTERN.match(entry_point):
        if entry_point is not None:
            click.echo(
                "Entrypoint must be in module:attribute format (e.g. 'main:callable', 'main:run')"
            )

        entry_point = click.prompt(
            "Python Entrypoint (module:attribute)", default=current_config.entry_point
        )
    
    while visibility is None or not VISIBILITY_PATTERN.match(visibility):
        if visibility is not None:
            click.secho("Visibility should be one of private, public or unlisted.")
        visibility = click.prompt("Visibility", default=current_config.visibility)

    while template is None or not TEMPLATE_PATTERN.match(template):
        if template is not None:
            click.secho("Template should be one of barbone, chat or chat with history")
        template = click.prompt("Template", default=current_config.template)
    
    current_config.name = name
    current_config.description = description
    current_config.entry_point = entry_point
    current_config.visibility = visibility
    current_config.template = template
    callable_config.save_config(current_config, path)

    entry_module, _ = entry_point.split(":")
    expected_main_path = path / (entry_module.replace(".", "/") + ".py")
    if not os.path.exists(expected_main_path):
        urllib.request.urlretrieve(CALLABLE_TEMPLATE_URL, expected_main_path)
        click.secho(
            f"Initialized callable.yaml and made a template callable file at {expected_main_path}",
            fg="green",
        )
    else:
        click.secho(f"Initialized callable.yaml.", fg="green")
    
    try:
        with open(path / REQUIREMENTS_TXT, "rt") as requirements_txt:
            existing_requirements = list(
                r.strip() for r in requirements_txt.readlines()
            )
    except FileNotFoundError:
        existing_requirements = []

    resolved_requirements = _update_callable_requirements(
        existing_requirements, list(requirement)
    )
    if not existing_requirements:
        write_requirements = True
    else:
        new_requirements = [
            r for r in resolved_requirements if r not in existing_requirements
        ]
        removed_requirements = [
            r for r in existing_requirements if r not in resolved_requirements
        ]

        if new_requirements or removed_requirements:
            click.secho(
                f"{path / REQUIREMENTS_TXT} already exists.",
                fg="yellow",
            )
            if new_requirements:
                click.secho(
                    f"The following requirements will be added: {new_requirements}",
                    fg="yellow",
                )
            if removed_requirements:
                click.secho(
                    f"The following requirements will be removed: {removed_requirements}",
                    fg="yellow",
                )
            write_requirements = click.confirm("Okay to proceed?", default=True)
        else:
            write_requirements = False

    if write_requirements:
        with open(path / REQUIREMENTS_TXT, "wt") as requirements_txt:
            requirements_txt.writelines(r + "\n" for r in resolved_requirements)

def _configure_venv(
        console: rich_console.Console, callable_dir: str
) -> Tuple[str, Dict[str,str]]:
    venv_path = os.path.join(callable_dir, ".callable.venv")
    console.print(f"Configuring virtual environment in {venv_path}")
    is_windows = os.name == "nt"
    bin_path = os.path.join(venv_path, "bin" if not is_windows else "Scripts")
    python_exe = os.path.join(bin_path, "python")
    if not os.path.exists(python_exe):
        # Match `python -m venv` behavior with symlinks on non-Windows to work around https://bugs.python.org/issue38705
        venv.create(venv_path, with_pip=True, symlinks=not is_windows)
    requirements_txt_path = os.path.join(callable_dir, REQUIREMENTS_TXT)
    if not os.path.exists(requirements_txt_path):
        raise ValueError(
            f"There is no {REQUIREMENTS_TXT} file at {requirements_txt_path}, please re-run [bold]fixie init[/bold]."
        )
    subprocess.run(
        [
            python_exe,
            "-m",
            "pip",
            "install",
            "-r",
            requirements_txt_path,
            "--disable-pip-version-check",
        ]
    ).check_returncode()
    console.print(f"[green]Requirements installed successfully.[/green]")
    env = os.environ.copy()
    env["PATH"] = bin_path + ":" + env.get("PATH", "")
    return python_exe, env

def _validate_callable_path(ctx, param, value):
    normalized = callable_config.normalize_path(value)
    if not os.path.exists(normalized):
        if not click.confirm(
            f"{normalized} does not exist. Would you like to create a new callable?",
            default=True,
        ):
            raise click.BadParameter(f"{normalized} does not exist")

        ctx.invoke(init_callable, path=value)

        # Re-normalize it after running init.
        normalized = callable_config.normalize_path(value)

    return normalized

@callable.command("update", help="Deploy the current agent.")
@click.argument("path", callback=_validate_callable_path, required=False)
@click.pass_context
def update(ctx, path):
    console = rich_console.Console(soft_wrap=True)
    config = callable_config.load_config(path)
    callable_dir = os.path.dirname(path) or "."
    sys.path.insert(0, callable_dir)
    entry_point_parts = config.entry_point.split(":", 1)
    module_name = entry_point_parts[0]
    attr = entry_point_parts[1] if len(entry_point_parts) == 2 else "agent"
    module = importlib.import_module(module_name)
    impl = getattr(module, attr)
    if isinstance (impl, Callable):
        callable_impl = impl
    else:
        console.print("configured entry point is not a callable")
        pass
    callable_blocks = callable_impl.get_blocks()
    testasdict = asdict(callable_blocks[0])
    # block_json = json.dumps([json.dumps(asdict(block)) for block in callable_blocks])
    with open('output.json', 'w') as file:
        json.dump(testasdict, file)