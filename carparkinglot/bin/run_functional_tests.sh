
cd ..
FILE=keyelements/tests/test_parking_lot.py
if [ -f "$FILE" ]; then
    echo "$FILE exist"
    echo "testing the custom test cases"
    python -m pytest -q keyelements/tests/test_parking_lot.py
else
    echo "run the bash script from the bin folder."
fi
