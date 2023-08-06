import ast
import logging
import sys
from logging import info, warning

from colored import Fore, Style
from git import Repo

FORMAT = "%(levelname)s - %(message)s"
logging.basicConfig(format=FORMAT)
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


def find(tree, name):
    for item in ast.walk(tree):
        if item.__class__.__name__ == "ClassDef" and item.name == name:
            return item


def find_assign(name, children):
    for child in children:
        if child.__class__.__name__ == "AnnAssign" and child.target.id == name:
            return True
    return False


def compare(filename, ast_1, ast_2):
    any_missing = False
    for item in ast.walk(ast_1):
        if item.__class__.__name__ == "ClassDef":
            class_to_search = item.name
            new_class = find(ast_2, class_to_search)
            old_assignments = []
            new_assignments = []
            for child in ast.iter_child_nodes(item):
                if child.__class__.__name__ in ["AnnAssign"]:
                    old_assignments.append(child.target.id)
                if child.__class__.__name__ in ["Assign"]:
                    old_assignments += [assign.id for assign in child.targets]

            for child in ast.iter_child_nodes(new_class):
                if child.__class__.__name__ in ["AnnAssign"]:
                    new_assignments.append(child.target.id)
                if child.__class__.__name__ in ["Assign"]:
                    new_assignments += [assign.id for assign in child.targets]
            missing = [
                assign
                for assign in old_assignments
                if assign not in new_assignments
            ]
            for assign in missing:
                any_missing = True
                warning(
                    f"{Fore.cyan}{assign}{Style.reset} has been renamed or "
                    f"removed in {Fore.cyan}{class_to_search}{Style.reset}"
                    f" ({filename})"
                )
    return any_missing


def scan():
    repo = Repo(".")
    changed_files = [
        item.a_path
        for item in repo.index.diff("HEAD")
        if item.a_path.endswith(".py")
    ]

    if len(changed_files) == 0:
        info("Nothing to do.")

    any_missing = False
    for file in changed_files:
        try:
            source_old = repo.commit("HEAD").tree[file].data_stream.read()
            with open(file, "r") as f:
                source_new = f.read()
            tree_old = ast.parse(source_old)
            tree_new = ast.parse(source_new)
            if compare(file, tree_old, tree_new):
                any_missing = True
        except KeyError:
            pass
    if any_missing:
        sys.exit(1)


def main():
    scan()
