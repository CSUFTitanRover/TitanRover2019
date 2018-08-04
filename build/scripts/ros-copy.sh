git_repo_var="git@github.com:CSUFTitanRover/TitanRover2019.git"

mkdir ros_copy #Create temp directory
cd ros_copy #change into temp directory

#Git Process to copy only desired sub(s)/folders
git init
git config core.sparseCheckout true
git remote add origin -f $git_repository
git checkout -b development
echo "ros/*"> .git/info/sparse-checkout
git checkout development
