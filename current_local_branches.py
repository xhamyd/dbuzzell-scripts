import argparse
from pathlib import Path
import subprocess


def current_local_branches(git_dir: str) -> dict:
    result = dict()
    for repo_dir in Path(git_dir).iterdir():
        if repo_dir.is_dir():
            proc = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"],
                                  cwd=repo_dir, capture_output=True)
            if proc.returncode == 0 and proc.stdout:
                # Format the captured output
                stdout = proc.stdout.decode("utf-8")
                result[repo_dir] = stdout.strip("\n")
    return result


if __name__ == "__main__":
    # NOTE: using argparse instead of Click to use only standard Python libs
    def parse_arguments() -> str:
        """This function is only called during CLI usage, so that other python
        modules can import this file without including this function.

        This is done to avoid potential nameclashing during import.

        """
        parser = argparse.ArgumentParser(description="List out matching git branches in all repos")
        parser.add_argument("parent_dir", help="The parent directory containing all of the repos to look into")
        args = parser.parse_args()
        return args.parent_dir

    # Example usage: python matching_branches.py C:\git
    git_dir = parse_arguments()
    matches = current_local_branches(git_dir)
    output = "\n".join(f"{repo_dir.name}: {branch}" for repo_dir, branch in matches.items())
    print(output)
