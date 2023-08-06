# VerisPTab

## Description
VerisPTab is a Python package that generates a "private duplicate" of a given table, obfuscating any potential Personally Identifiable Information (PII) in the process. 

## Installation
VerisPTab can be installed via pip:

```bash
pip install verisptab
```

After installation, you can import the `generate` function and use it as follows:

```python
from verisptab import generate

new_df = generate.generate("path_to_the_original_table")
```

This will create a new dataframe `new_df` that is a "private" version of the original table.

## Special Rules for PII Removal
Please rename the columns in your input table (CSV) to follow the following rules

If a column contains full names, please name the column FULL_NAME.

If a column contains last names, please name the column LAST_NAME.

If a column contains first names, please name the column FIRST_NAME.

If a column contains addresses, please name the column LOC_ADDRESS.


## Example Input Table
| FULL_NAME        | FIRST_NAME | LAST_NAME | LOC_ADDRESS                               | RANDOM_COLOR | RANDOM_INTEGER | Email                         | Phone Number     |
|------------------|------------|-----------|-------------------------------------------|--------------|----------------|-------------------------------|------------------|
| Alexander Cook   | Alexander  | Cook      | 6262 Diana Views Apt. 635, Cathymouth, SD 39278 | Purple       | 362            | alexander.cook@fakeemail.com  | 792-322-1210x91380 |
| Kenneth Townsend | Kenneth    | Townsend  | 8960 Danielle Fields, Wrightview, NY 05647 | White        | 570            | kenneth.townsend@fakeemail.com | 367.691.1088x8574  |
| Leah Harvey      | Leah       | Harvey    | USNS Bradford, FPO AA 06578               | Gray         | 500            | leah.harvey@fakeemail.com     | 232.914.1072x685   |


## Troubleshooting and Known Issues
This section will be updated as new issues are identified and solutions or workarounds are developed.

## License
VerisPTab is open source and free for use. Please use responsibly and respect the privacy of all individuals. 
