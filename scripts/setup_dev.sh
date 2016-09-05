#!/bin/bash
parent_path=$( cd "$(dirname "${BASH_SOURCE}")" ; pwd -P )
project_root=$(dirname "$parent_path")
previous_dir=$(pwd)

python_version="2.7"

if [ "$1" != "" ]; then
	python_version=$1
fi

python_exe="python$python_version"

if [ ! -f "$project_root/venv/bin/activate" ]; then
	cd $project_root
	virtualenv venv --python=$python_exe
else
	echo "Virtual Environment Already Created"
fi

source $project_root/venv/bin/activate

temp_folder="$project_root/temp"

mkdir $temp_folder
cd $temp_folder

git clone https://github.com/josh-hernandez-exe/pyjs.git
cd pyjs
python setup.py install

rm -rf $temp_folder

# Install Project
cd "$project_root"
python setup.py install


cd $previous_dir
