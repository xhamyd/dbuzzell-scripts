RETURN_DIR=$(pwd)

cd "${DBUZZELL_GIT_DIR}" || (echo "ERROR: Cannot enter ${DBUZZELL_GIT_DIR}" && exit)

# Source: https://unix.stackexchange.com/a/86724
for git_dir in */; do
    cd "${git_dir}" || exit
    BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)
    echo "Pulling ${git_dir} on ${BRANCH_NAME}..."
    git pull -q
    cd ..
done

cd "${RETURN_DIR}" || (echo "ERROR: Cannot enter ${RETURN_DIR}" && exit)
