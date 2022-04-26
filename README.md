Canvas to FSC
===

This script converts a Canvas export to the FSC format, automatically.

## Usage:
You need an export from Canvas and an initial export from FSC to provide the
additional required fields.
The script will merge the "Final Score" column from Canvas into the FSC
spreadsheet.

```
python3 fsc.py sample-canvas.csv sample-fsc-input.xls sample-fsc-output.csv
```
or
```
./fsc.py sample-canvas.csv sample-fsc-input.xls sample-fsc-output.csv
```

## Requirements:
Requires Python 3, Pandas, and python-xlrd.
```
pip3 install pandas xlrd
```
