```
cd \PATH\TO\dbuzzell-scripts\python-docker\<PROJECT_NAME>
.\build_and_run_docker.bat
```

Each folder should contain the following files:

* `build_and_run_docker.bat`
  * Aliases the Docker `build` and `run` commands
* `Dockerfile`
* `src\`
  * Contains the Python source code files for the project
* `requirements.txt`
  * Python libraries needed for the source code
