import pyfiglet  
from colorama import Fore, Style  
import argparse  
import sys  
import requests  
from bs4 import BeautifulSoup  
import subprocess  
import signal  
  
# Define a function to handle the SIGINT signal  
def signal_handler(sig, frame):  
   print(Fore.RED + "\nInterrupted by user. Exiting..." + Style.RESET_ALL)  
   sys.exit(0)  
  
# Register the signal handler for SIGINT  
signal.signal(signal.SIGINT, signal_handler)  
  
# Display the ASCII banner  
def display_banner():  
   banner = pyfiglet.figlet_format("ReconGen Venom")  
   print(Fore.RED + banner[:len(banner)//2] + Fore.BLUE + banner[len(banner)//2:] + Style.RESET_ALL)  
  
   dev_box = f"""  
*******************************************************  
*        *  
*  ***********************************************  *  
*  *       *  *  
*  *  {Fore.WHITE + "Developer: Saconyfx AKA Terminal Venom"}  *  *  
*  *  {Fore.BLUE + "Portfolio: https://Saconychukwu.com"}  *  *  
*  *  {Fore.RED + "GitHub Profile: https://github.com/Saconyfx"}  *  *  
*  *  {Fore.YELLOW + "GitHub Repo: https://github.com/Saconyfx/EnumVenom"}  *  *  
*  *  {Fore.GREEN + "Other Profile: https://linktr.ee/Chidubemc"}  *  *  
*  *       *  *  
*  ***********************************************  *  
*        *  
*******************************************************  
"""  
   print(dev_box)  
  
   description = """  
ReconGen Venom is a versatile cybersecurity reconnaissance tool designed for domain and network intelligence. It provides users with essential tools for domain research, network reconnaissance, and web development debugging. With features like WHOIS lookup, DNS and IP address resolution, HTTP header inspection, and network scanning, it equips professionals with valuable insights into target systems. Whether you're a security researcher, penetration tester, or developer, ReconGen Venom simplifies information gathering for enhanced analysis and decision-making.  
"""  
   print(Fore.GREEN + description + Style.RESET_ALL)  
  
# Define the function to display usage examples  
def display_usage():  
   usage = f"""  
Usage Examples:  
  python enum_venom.py -d example.com -w  # Perform WHOIS lookup for example.com  
  python enum_venom.py -d example.com -n  # Perform network scan for example.com  
  python enum_venom.py -d example.com -p  # Find pages for example.com  
  python enum_venom.py -d example.com -l  # Perform DNS lookup for example.com  
  python enum_venom.py -i 8.8.8.8    # Perform IP address lookup for 8.8.8.8  
  python enum_venom.py -h   # Display this help message  
  python enum_venom.py -d example.com -H  # Display HTTP headers for example.com  
"""  
   print(Fore.CYAN + usage + Style.RESET_ALL)  
  
# Define the function to perform WHOIS lookup using the Whois.com website  
def get_whois_data(domain):  
   try:  
      whois_url = f'https://www.whois.com/whois/{domain}'  
      response = requests.get(whois_url)  
      soup = BeautifulSoup(response.text, 'html.parser')  
      whois_info = soup.find('pre').text  
      return whois_info  
   except Exception as e:  
      print(f"Error: {e}")  
      return None  
  
def find_pages(website):  
   pagelink = 'https://api.hackertarget.com/pagelinks/?q='+website  
   try:  
      info = requests.get(pagelink)  
      info.raise_for_status()  # Raise an exception for HTTP errors  
      print(Fore.CYAN + info.text + Style.RESET_ALL)  
   except requests.exceptions.RequestException as err:  
      print(Fore.RED + f"Error fetching page links: {err}" + Style.RESET_ALL)  
  
def get_ip_info(ip_address):  
   try:  
      ipinfo_url = f'https://ipinfo.io/{ip_address}/json'  
      response = requests.get(ipinfo_url)  
      if response.status_code == 401:  
        return None  
      ip_info = response.json()  
      return ip_info  
   except Exception as e:  
      print(f"Error: {e}")  
      return None  
  
def network_scan(ip_address):  
   nmap_command = f"nmap -sS -O {ip_address}"  
   try:  
      output = subprocess.check_output(nmap_command, shell=True)  
      return output.decode("utf-8")  
   except subprocess.CalledProcessError as e:  
      print(f"Error: {e}")  
      return None  
  
def display_http_headers(url):  
   try:  
      response = requests.get(url)  
      headers = response.headers  
      print("HTTP Headers:")  
      for key, value in headers.items():  
        print(f"{key}: {value}")  
   except Exception as e:  
      print(f"Error: {e}")  
  
def dns_lookup(website):  
   try:  
      dnslook = 'https://api.hackertarget.com/dnslookup/?q='+website  
      info = requests.get(dnslook)  
      info.raise_for_status()  # Raise an exception for HTTP errors  
      print('\033[99m')  
      print(info.text)  
   except requests.exceptions.RequestException as err:  
      print(Fore.RED + f"Error performing DNS lookup: {err}" + Style.RESET_ALL)  
  
# Define the main function  
def main():  
   parser = argparse.ArgumentParser(description='Enumeration Tool', add_help=False)  
   parser.add_argument('-h', '--help', action='store_true', help='Display this help message')  
   parser.add_argument('-d', '--domain', help='Domain name to enumerate')  
   parser.add_argument('-w', '--whois', action='store_true', help='Perform WHOIS lookup')  
   parser.add_argument('-n', '--network', action='store_true', help='Perform network scan')  
   parser.add_argument('-p', '--pages', action='store_true', help='Find pages')  
   parser.add_argument('-l', '--dns', action='store_true', help='Perform DNS lookup')  
   parser.add_argument('-i', '--ip', help='IP address to lookup')  
   parser.add_argument('-H', '--headers', action='store_true', help='Display HTTP headers')  
   args = parser.parse_args()  
  
   if len(sys.argv) == 1:  
      display_banner()  
      print(Fore.YELLOW + "To see available options and usage examples, run the script with '-h'." + Style.RESET_ALL)  
   else:  
      display_banner()  
      if args.help:  
        display_usage()  
      if args.domain:  
        if args.whois:  
           print(Fore.GREEN + f"Performing WHOIS lookup for {args.domain}:" + Style.RESET_ALL)  
           try:  
              whois_data = get_whois_data(args.domain)  
              if whois_data:  
                lines = whois_data.splitlines()  
                filtered_lines = []  
                for line in lines:  
                   if not line.startswith("Search results obtained from the RegistrarSafe, LLC WHOIS database are"):  
                      filtered_lines.append(line)  
                   else:  
                      break  
                filtered_whois_data = "\n".join(filtered_lines)  
                print(Fore.GREEN + "\nWHOIS Lookup Results:" + Style.RESET_ALL)  
                print(Fore.GREEN + "---------------------" + Style.RESET_ALL)  
                print(Fore.GREEN + filtered_whois_data + Style.RESET_ALL)  
                print(Fore.GREEN + "***" + Style.RESET_ALL)  
                print(Fore.GREEN + " End of WHOIS Results " + Style.RESET_ALL)  
                print(Fore.GREEN + "***" + Style.RESET_ALL)  
              else:  
                print(Fore.RED + "Failed to retrieve WHOIS data from Whois.com website." + Style.RESET_ALL)  
           except KeyboardInterrupt:  
              print(Fore.RED + "\nInterrupted by user. Exiting..." + Style.RESET_ALL)  
              sys.exit(0)  
        elif args.pages:  
           print(Fore.GREEN + f"Finding pages for {args.domain}:" + Style.RESET_ALL)  
           try:  
              find_pages(args.domain)  
           except KeyboardInterrupt:  
              print(Fore.RED + "\nInterrupted by user. Exiting..." + Style.RESET_ALL)  
              sys.exit(0)  
        elif args.network:  
           print(Fore.GREEN + f"Performing network scan for {args.domain}:" + Style.RESET_ALL)  
           try:  
              network_scan_output = network_scan(args.domain)  
              if network_scan_output:  
                print(Fore.GREEN + network_scan_output + Style.RESET_ALL)  
              else:  
                print(Fore.RED + "Failed to perform network scan." + Style.RESET_ALL)  
           except KeyboardInterrupt:  
              print(Fore.RED + "\nInterrupted by user. Exiting..." + Style.RESET_ALL)  
              sys.exit(0)  
        elif args.dns:  
           print(Fore.GREEN + f"Performing DNS lookup for {args.domain}:" + Style.RESET_ALL)  
           try:  
              dns_lookup(args.domain)  
           except KeyboardInterrupt:  
              print(Fore.RED + "\nInterrupted by user. Exiting..." + Style.RESET_ALL)  
              sys.exit(0)  
        elif args.headers:  
           print(Fore.GREEN + f"Displaying HTTP headers for {args.domain}:" + Style.RESET_ALL)  
           try:  
              url = f"https://{args.domain}"  
              display_http_headers(url)  
           except KeyboardInterrupt:  
              print(Fore.RED + "\nInterrupted by user. Exiting..." + Style.RESET_ALL)  
              sys.exit(0)  
        else:  
           print(Fore.RED + "Please specify an action to perform." + Style.RESET_ALL)  
      if args.ip:  
        print(Fore.GREEN + f"Performing IP address lookup for {args.ip}:" + Style.RESET_ALL)  
        try:  
           ip_info = get_ip_info(args.ip)  
           if ip_info:  
              print(Fore.GREEN + "\nIP Address Lookup Results:" + Style.RESET_ALL)  
              print(Fore.GREEN + "---------------------------" + Style.RESET_ALL)  
              for key, value in ip_info.items():  
                print(Fore.GREEN + f"{key}: {value}" + Style.RESET_ALL)  
           else:  
              print(Fore.RED + "Failed to retrieve IP address information." + Style.RESET_ALL)  
        except KeyboardInterrupt:  
           print(Fore.RED + "\nInterrupted by user. Exiting..." + Style.RESET_ALL)  
           sys.exit(0)  
  
# Example usage of the function  
if __name__ == "__main__":  
   main()















