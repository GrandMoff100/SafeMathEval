export FILE_NAME="evalsafe"

echo Deploying Custom Parser:

echo - Installing Dependencies...

pip install pyinstaller -q -q

echo - Assembling Binary...

pyinstaller --onefile -c --name $FILE_NAME --distpath $(pwd) --log-level WARN parser.py

echo - Done Compiling...
echo - Cleansing Temp Files...
rm -rf build/ dist/ *.spec
echo
echo Tests:
echo - Testing Binary with "(20*10/2-2 -0/3)"
echo -
echo - Output below

./$FILE_NAME "(20*10/2-2 -0/3)"

