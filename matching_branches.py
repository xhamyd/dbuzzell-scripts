import argparse
from pathlib import Path
import subprocess


def matching_branches(git_dir: str, branch_type: str, search_term: str) -> dict:
    branch_arg = dict(all="-a", local="", remote="-r")
    result = dict()
    for repo_dir in Path(git_dir).iterdir():
        if repo_dir.is_dir():
            proc = subprocess.run(["git", "branch", branch_arg[branch_type], "--list", search_term],
                                  cwd=repo_dir, capture_output=True)
            if proc.returncode == 0 and proc.stdout:
                # Format the captured output
                stdout = proc.stdout.decode("utf-8")
                result[repo_dir] = list(f"{branch.strip(' ')}" for branch in stdout.split("\n") if branch)
    return result


if __name__ == "__main__":
    # NOTE: using argparse instead of Click to use only standard Python libs
    def parse_arguments() -> tuple:
        """This function is only called during CLI usage, so that other python
        modules can import this file without including this function.

        This is done to avoid potential nameclashing during import.

        """
        parser = argparse.ArgumentParser(description="List out matching git branches in all repos")
        parser.add_argument("parent_dir", help="The parent directory containing all of the repos to look into")
        parser.add_argument("--branch-type", dest="branch_type", default="remote", choices=["all", "local", "remote"],
                            help="The type of branches to list for each repo")
        parser.add_argument("--search-term", dest="search_term", default="*dbuzzell/*",
                            help="Filter branches in each repo if matching this term")
        args = parser.parse_args()
        return args.parent_dir, args.branch_type, args.search_term

    # Example usage: python matching_branches.py C:\git
    git_dir, branch_type, search_term = parse_arguments()
    matches = matching_branches(git_dir, branch_type, search_term)
    for repo_dir, branches in matches.items():
        print(f"Branches in {repo_dir.name}:")
        print("\n".join(f"    - {branch}" for branch in branches))
        print()
