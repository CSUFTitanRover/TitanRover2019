#Author: Can Dalgir
#Sparse-Copy Script TitanRover 2019

mkdir ros_copy #Create temp directory
cd ros_copy #change into temp directory

#Git Process to copy only desired sub(s)/folders
git init
git config core.sparseCheckout true
git remote add origin -f git@github.com:CSUFTitanRover/TitanRover2019.git
git checkout -b development #Bare minimum checkout as we only want the branch head pointer
echo "ros/*"> .git/info/sparse-checkout #Only include the desired sub-directories / files
git checkout development #Checkout again to populate with desired files

#Validation process for ros, can be more detailed if needed
if [ -d "ros" ]; then

	cd .. #Go back one level
	if [[ -n $(find / -type d -name "catkin_ws" -ls -printf '%h\n') ]]
	then
		echo Found.
		
		#copy process
		cd ros_copy #Goes into the temporary repo
		echo copying ros to $ROS_PACKAGE_PATH/catkin_ws/src
		cp -R ros_copy/ros $ROS_PACKAGE_PATH/catkin_ws/src #Recursive copying of files to the desired location
	fi
fi

echo copying is finished.
cd .. #Goes back one level
#rm -r -f ros_copy #removes the temporary repo after finished.
