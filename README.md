# canLogParse
This is a library for importing and parsing data from Kvaser CAN files when you don't have a DBC file. The code should be fairly simple and self-documenting, and all other information should be contained within this file.

## Functions
### `importCanData(file, outputFormat="2dArray")`
Imports data from a log file and returns it as an array of records. The possible formats are `2dArray` (the default), `tupleArray`, and `dict`.
####  
The 2d array is structured as follows
