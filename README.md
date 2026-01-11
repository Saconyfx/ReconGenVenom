# ReconGenVenom
A Cybersecurity Reconnaissance Tool
ReconGen Venom is a cybersecurity reconnaissance tool designed to gather domain and network intelligence.

### Features

- Performs WHOIS lookups for domain registration information
- Conducts DNS lookups for domain name system records
- Executes network scans for open ports and services
- Allows users to inspect HTTP headers for a given URL
- Retrieves IP address information for network insights


### Installation & Usage

```bash

To use ReconGen Venom, simply run the script and follow the prompts:  
  
Clone the repository:  
  
  git clone https://github.com/Saconyfx/ReconGenVenom.git  
  
Navigate to the repository directory  
  
  cd ReconGenVenom  
  
Install the required dependencies  
  
  pip install -r requirements.txt  
  
Run the script  
  
  python ReconGenVenom.py -h

This will display the help menu with available options.

```

# Options

```bash

The following options are available:

  -d, --domain       Specify the domain to gather intelligence on
  -w, --whois        Perform a WHOIS lookup for the specified domain
  -l, --dns         Perform a DNS lookup for the specified domain
  -i, --ip          Specify the IP address to gather intelligence on
  -n, --network      Perform a network scan for the specified domain or IP address
  -H, --headers      Inspect HTTP headers for the specified URL
  -h, --help        Show the help menu

```

# Examples

```bash


Perform a WHOIS lookup for a domain: 

  python recongen_venom.py -d example.com -w
 
Perform a DNS lookup for a domain: 
 
  python recongen_venom.py -d example.com -l

Retrieve information about an IP address:

  python recongen_venom.py -i 8.8.8.8

Perform a network scan for a domain:

  python recongen_venom.py -d example.com -n

Inspect HTTP headers for a URL:
 
  python recongen_venom.py -d example.com -H

Display the help menu: 

  python recongen_venom.py -h

```


# License

ReconGen Venom is released under the GNU General Public License version 3 (GPL-3.0). See the LICENSE file for details.

GPL-3.0 License
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later vers>

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.

# Contributing

Contributions are welcome! If you'd like to contribute to ReconGen Venom, please fork the repository and submit a pull request.

# Disclaimer

ReconGen Venom is designed for educational purposes only. It should not be used for malicious activities, such as cracking passwords without authorization. Use at your own risk.

By using ReconGen Venom, you acknowledge that you have read and understood the terms of the GPL-3.0 License and agree to abide by them.


