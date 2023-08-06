# DriveScanner

DriveScanner is a Python library created by [The Analytics Lab](https://www.theanalyticslab.nl/), which is powered by [Cmotions](https://cmotions.nl/). This library aims to help you with identifying files on your filesystem that could be a potential GDPR threat. To do this, the file contents are scanned, looking for specific information like IBAN, social security numbers (Dutch: BSN), telephone numbers, email addresses, credit card numbers and more. 

## Installation
Install DriveScanner using pip

```bash
pip install drivescanner
```

## Usage
```python
import drivescanner

# set the location of the files you want to scan
# all files in all subdirectories will also be taken into account
file_path = "C:/MyFiles"
file_list = drivescanner.list_all_files(file_path)

# create an overview of all the filetypes on our example drive
drivescanner.extension_stats(file_list)

# if we want we can include/exclude certain extensions
file_list = drivescanner.select_files(file_list, include=["xlsx", "xls", "docx", "doc", "pdf", "ppt", "pptx"], exclude=None)

# now we are ready to scan all the files in the list
resultdict = drivescanner.scan_drive(file_list)

# and calculate the risk score for all scanned files
# there might be some files which gave problems and are not scanned
# your retrieve those in a separate dataframe
df_result, df_not_processed = drivescanner.calculate_severity(resultdict)

# that's it, now you can use and inspect the result any way you like
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)

## Contributors
Jeanine Schoonemann, Rick Flamand, Sem Frankenberg, Wim Verboom and Wouter van Gils<br>
[Contact us](mailto:info@theanalyticslab.nl)