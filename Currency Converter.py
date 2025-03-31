import requests

# Function to fetch exchange rate from an API
def get_exchange_rate(base_currency, target_currency):
    """
    Fetches the exchange rate for the given currency pair from an API.
    Returns the exchange rate if found, otherwise returns None.
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    return data['rates'].get(target_currency, None)

# Function to convert currency using the fetched exchange rate
def convert_currency(amount, base_currency, target_currency):
    """
    Converts the given amount from the base currency to the target currency using the fetched exchange rate.
    Returns the converted amount if successful, otherwise returns None.
    """
    rate = get_exchange_rate(base_currency, target_currency)
    if rate:
        converted_amount = amount * rate
        return converted_amount
    else:
        return None

# Main function to interact with the user
def main():
    """
    Handles user input and performs currency conversion.
    Ensures proper validation of input values.
    """
    print("Currency Converter")
    print("Available currency codes: USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, SEK, NZD, etc.")
    
    # Loop to get a valid amount from the user
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                print("Amount must be greater than zero. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    # Loop to get a valid base currency code
    while True:
        base_currency = input("Enter the base currency (e.g., USD): ").upper()
        if len(base_currency) != 3 or not base_currency.isalpha():
            print("Invalid currency code. Please enter a valid 3-letter currency code.")
        else:
            break
    
    # Loop to get a valid target currency code
    while True:
        target_currency = input("Enter the target currency (e.g., EUR): ").upper()
        if len(target_currency) != 3 or not target_currency.isalpha():
            print("Invalid currency code. Please enter a valid 3-letter currency code.")
        else:
            break
    
    # Converting currency and displaying the result
    result = convert_currency(amount, base_currency, target_currency)
    
    if result:
        print(f"{amount} {base_currency} is equal to {result:.2f} {target_currency}")
    else:
        print("Invalid currency code or conversion failed.")

# Entry point of the script
if __name__ == "__main__":
    main()
