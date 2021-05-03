#!/usr/bin/env -S python -B
# -B prevents creating __pycache__/ directory

"""
all-grades.py - aggregate all the course component canvas sheets into
                one big one
"""

import pandas as pd
import math
import argparse

def roundNotCrappily(n):
    """
    None of this accountant nonsense please!
    """
    # convert_dtypes seems to have not worked
    try:
        n = int (n)
    except ValueError:
        n = float(n)
    return math.floor(n + 0.5) # normal people rounding

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Convert Canvas CSV into a FSC CSV")
  parser.add_argument('canvas_file', nargs=1, help="Canvas file name, a CSV file exported from Canvas")
  parser.add_argument('fsc_file', nargs=1, help="Initial FSC file name, a CSV export from FSC.")
  parser.add_argument('output_fsc_file', nargs=1, help="Output FSC file name, a CSV file that will be populated from the two input files and can be uploaded to FSC.")
  ns = parser.parse_args()

  courseMarks = pd.read_csv(ns.canvas_file[0]).convert_dtypes()
  fscIn = pd.read_excel(ns.fsc_file[0]).convert_dtypes()

  #courseMarks.drop(["Points Possible", "Student, Test"], inplace=True)
  courseMarks.drop([0], inplace=True)

  fscIn.drop(columns=["Percent Grade"],inplace=True)

  courseMarks["Percent Grade"] = \
       [roundNotCrappily(series["Final Score"])
        for (index,series) in courseMarks.iterrows() ]


  marks = courseMarks[["SIS User ID","Percent Grade"]]\
      .rename(columns={"SIS User ID" : "Student Number"})

  fscOut = fscIn.merge(marks,how="left",on="Student Number")

  fscOut.to_csv(ns.output_fsc_file[0], index=False)
