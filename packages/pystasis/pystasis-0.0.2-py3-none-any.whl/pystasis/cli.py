import ast
import logging
from logging import info, warning

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
        if child.__class__.__name__ == "AnnAssign":
            if child.target.id == name:
                return True
    return False


def compare(ast_1, ast_2):
    for item in ast.walk(ast_1):
        if item.__class__.__name__ == "ClassDef":
            class_to_search = item.name
            info(f"Checking {class_to_search}")
            new_class = find(ast_2, class_to_search)
            children_old = [child for child in ast.iter_child_nodes(item)]
            children_new = [child for child in ast.iter_child_nodes(new_class)]
            for child in children_old:
                if child.__class__.__name__ == "AnnAssign":
                    to_search = child.target.id
                    if not find_assign(to_search, children_new):
                        warning(
                            f'Possible breaking change: "{to_search}" '
                            f"has been removed or renamed"
                        )


def scan():
    repo = Repo(".")
    changedFiles = [
        item.a_path
        for item in repo.index.diff(None)
        if item.a_path.endswith(".py")
    ]

    if len(changedFiles) == 0:
        info("Nothing to do.")

    for file in changedFiles:
        try:
            source_old = repo.commit("Head").tree[file].data_stream.read()
            with open(file, "r") as f:
                source_new = f.read()
            info(f"Scanning in {file}...")
            tree_old = ast.parse(source_old)
            tree_new = ast.parse(source_new)
            compare(tree_old, tree_new)
        except KeyError:
            pass


def main():
    scan()
