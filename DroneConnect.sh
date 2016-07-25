#!/bin/bash
REPO=https://github.com/nlurski/summersdrspectrum.git
GITFILE=summersdrspectrum.git
echo -e "Please enter the name of the file from the git repo to run:"
read FILE
git clone --bare $REPO
cd ./summersdrspectrum/3dr_Solo_scripts
solo script pack
solo script run $FILE
i = 1
while [$i > 0]
do
    echo -e "Done? Y/n"
    read DONE
    if [ $DONE = "Y" ] || [ $DONE = "Yes" ] || [ $DONE = "y" ] || [ $DONE = "yes" ]
    then
        echo "Done!"
        i = 0
    fi
done
rm -rf $GITFILE