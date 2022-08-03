RETURN_DIR=$(pwd)

cd "${DBUZZELL_GIT_DIR}" || echo "ERROR: Cannot enter ${DBUZZELL_GIT_DIR}" && exit

# Source: https://unix.stackexchange.com/a/86724
for git_dir in */; do
    cd "${git_dir}" || exit
    echo "Pulling ${git_dir}..."
    git pull -q
    cd ..
done

cd "${RETURN_DIR}" || echo "ERROR: Cannot enter ${RETURN_DIR}" && exit
