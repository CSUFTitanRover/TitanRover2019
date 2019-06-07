#Author: Can Dalgir
#Sparse-Copy Script Push TitanRover 2019

mkdir ros_copy #Create temp directory
cp -R catkin_ws ros_copy #Recursive copying of files to the desired location
cd ros_copy #change into temp directory

#Git Process to copy only desired sub(s)/folders
git init
git remote add origin -f git@github.com:CSUFTitanRover/TitanRover2019.git
git checkout -b development
git add *
git commit -m "Updating the ros_copy"
#git push -u origin development -f #might need to force push

echo Last commit hash:
git rev-parse HEAD

#Self cleaning
#cd ..
#rm -r -f ros_copy
