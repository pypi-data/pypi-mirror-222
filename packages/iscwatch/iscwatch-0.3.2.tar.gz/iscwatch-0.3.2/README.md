# iscwatch - A Command Line Application For Monitoring Intel Security Center Product Advisories

![Version](https://img.shields.io/badge/version-0.3.1-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Description

`iscwatch` is a command line application that searches for summaries of [Intel's Security Center Product Advisories](https://www.intel.com/content/www/us/en/security-center/default.html) and outputs those summaries in CSV format. Included in the output per advisory is its title, full text url, advisory ID, updated date, and released date.

## Features

- Fetches some or all summaries of Intel's Security Center Product advisories.
- Outputs advisory summary data in CSV format with our without headers.
- Date filtering enables iscwatch to be used to only show latest changes.

## Installation

You can install `iscwatch` using pip:

```
pip install iscwatch
```

## Usage

```
Usage: iscwatch [OPTIONS]

Retrieve Security Advisory summaries from Intel website and output as CSV.

Options
--since         -s      [%Y-%m-%d]  Exclude summaries before date.
                                    [default: 0001-01-01 00:00:00]
--version       -v                  Output product version and exit.
--no-headers    -n                  Omit column headers from CSV output.
--last-updated  -l                  Output date when last updated and exit.
--help                              Show this message and exit.
```

The application will fetch the latest advisories from Intel's Security Center and display the summaries in CSV format to the standard output (stdout). You can redirect the output to a file if needed:

```bash
iscwatch > advisories.csv
```

## CSV Format

The CSV output will contain the following columns:

- Advisory Title
- Advisory Page Link
- Advisory ID
- Updated Date
- Released Date

```bash
> iscwatch --since 2023-07-01 --no-headers
2023.2 IPU – BIOS Advisory,https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00807.html,INTEL-SA-00807,2023-07-07,2023-05-09
Intel® NUC Laptop Kit Advisory,https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00712.html,INTEL-SA-00712,2023-07-07,2022-08-09
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to create an issue or submit a pull request.

## Acknowledgments

- This application relies on Intel's Security Center for fetching advisories data.
