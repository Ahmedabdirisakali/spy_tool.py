import requests
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from colorama import Fore, Style, init

# Qurxi console-ka
init(autoreset=True)

def banner():
    print(Fore.MAGENTA + Style.BRIGHT + "=" * 60)
    print(Fore.CYAN + Style.BRIGHT + "               TOOLKA BAARISTA IP & TELEFOONKA")
    print(Fore.GREEN + Style.BRIGHT + "               Qoraaga: Ahmed Abdirisak Ali")
    print(Fore.YELLOW + Style.BRIGHT + "             Ujeeddo: Educational Purposes Only")
    print(Fore.RED + Style.BRIGHT + "         ** Fadlan Adeegso Qalabkan Si Sharci Ah! **")
    print(Fore.MAGENTA + Style.BRIGHT + "=" * 60)

def get_ip_info(ip_address):
    """
    Baarista IP Address: Wadanka, magaalada, iyo xogta kale.
    """
    try:
        # Token-kaaga API
        token = "af46259f12e3b7"
        url = f"https://ipinfo.io/{ip_address}?token={token}"

        # Codsi API ah
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            print(Fore.YELLOW + Style.BRIGHT + f"\nNatiijooyinka IP: {ip_address}")
            print(Fore.GREEN + f"IP Address: {data.get('ip', 'Unknown')}")
            print(Fore.CYAN + f"Magaalada: {data.get('city', 'Unknown')}")
            print(Fore.MAGENTA + f"Gobolka: {data.get('region', 'Unknown')}")
            print(Fore.BLUE + f"Dalka: {data.get('country', 'Unknown')}")
            print(Fore.YELLOW + f"Goobta (Latitude, Longitude): {data.get('loc', 'Unknown')}")
            print(Fore.RED + f"Hay’adda: {data.get('org', 'Unknown')}")
        else:
            print(Fore.RED + "Khalad ayaa dhacay:", data.get("error", "Unknown error"))

    except Exception as e:
        print(Fore.RED + "Waxaa dhacay khalad:", str(e))

def get_phone_info(phone_number):
    """
    Baarista nambarka telefoonka: Wadanka, shirkadda, iyo xogta kale.
    """
    try:
        # Parse garee lambarka telefoonka
        parsed_number = phonenumbers.parse(phone_number)

        # Soo bandhig xogta muhiimka ah
        country = geocoder.description_for_number(parsed_number, "en")
        operator = carrier.name_for_number(parsed_number, "en")
        timezones = timezone.time_zones_for_number(parsed_number)

        print(Fore.YELLOW + Style.BRIGHT + f"\nNatiijooyinka Nambarka: {phone_number}")
        print(Fore.GREEN + f"Wadanka: {country}")
        print(Fore.CYAN + f"Shirkadda: {operator if operator else 'Unknown'}")
        print(Fore.MAGENTA + f"Timezone(s): {', '.join(timezones)}")

    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(Fore.RED + f"Khalad ayaa dhacay: {e}")

def main():
    banner()
    while True:
        print(Fore.CYAN + "\nFadlan dooro mid ka mid ah xulashooyinka soo socda:")
        print(Fore.YELLOW + "1. Baadh IP Address")
        print(Fore.GREEN + "2. Baadh Numberka Telefoonka")
        print(Fore.RED + "3. Ka bax toolka")
        choice = input(Fore.MAGENTA + "\nDooro ikhtiyaar (1, 2, ama 3): ")

        if choice == "1":
            ip_address = input(Fore.CYAN + "Gali IP Address-ka: ")
            get_ip_info(ip_address)
        elif choice == "2":
            phone_number = input(Fore.CYAN + "Gali Numberka Telefoonka (w/ code +252): ")
            get_phone_info(phone_number)
        elif choice == "3":
            print(Fore.YELLOW + "\nWaad ku mahadsan tahay isticmaalka toolka! Nabad galyo.")
            break
        else:
            print(Fore.RED + "\nFadlan dooro 1, 2 ama 3!")

if __name__ == "__main__":
    main()

