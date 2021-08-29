
python3 setup.py sdist

echo "TYPE USERNAME"
read UNAME

echo "TYPE PASSWORD"
read PASSWORD

python3 -m twine upload dist/* -u $UNAME -p $PASSWORD

rm -rf dist/*
