
echo "Titan Rover Build Automation Scripts"
echo "Version 1.0.0"
echo " "
echo "Python Compile Module"
echo "Python Bootstrap will start..."
cd ../bootstrap/

RESULT=`python3.5 -c 'import bstrp; print(bstrp.python_file_check())'`
if [[ "$RESULT" == "True" ]]; then
	echo "All files are complete."
else
	echo "There are missing files..."
	echo "Running missing files check script..."
fi

if command -v python3 &>/dev/null; then
    echo Python 3 is installed
else
    echo Python 3 is not installed
fi
