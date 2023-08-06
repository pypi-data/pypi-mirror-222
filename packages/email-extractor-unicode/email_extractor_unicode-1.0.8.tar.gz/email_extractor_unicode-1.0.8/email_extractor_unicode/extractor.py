import undetected_chromedriver as uc
import re

counter = 0

def extract_emails(text):
    # Regular expression pattern to find emails
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, text)
    return emails

def extract_emails_from_phone_file(phone_file_path, emails_file_path):
    global counter
    # Create a single driver instance
    driver = None

    try:
        driver = uc.Chrome()

        # Open the phone.txt file to read phone numbers line by line
        with open(phone_file_path, 'r') as file:
            phone_numbers = [phone.strip() for phone in file.readlines()]

        # Initialize a set to store all emails without duplicates
        all_emails = set()

        # Loop through each phone number, visit the corresponding URL, and extract emails
        for phone in phone_numbers:
            if "+1" in phone:
                phone = phone.replace("+1" , "")
            try:
                url = f'https://www.smartbackgroundchecks.com/phone/{phone}'
                driver.get(url)

                # Get the page source
                page_source = driver.page_source

                # Define the pattern to extract URLs from anchor tags
                pattern = r'<a\s+href="(.*?)".*?>'

                # Use re.findall to find all occurrences of the pattern in the source code
                links = re.findall(pattern, page_source)

                # Filter and extract only the links you need
                target_links = [link for link in links if link.startswith('https://www.smartbackgroundchecks.com/people/')]

                # Remove duplicates by converting the list to a set and then back to a list
                unique_links = list(set(target_links))

                # Visiting each link, collecting emails, and writing them to the file
                for link in unique_links:
                    try:
                        driver.get(link)
                        emails_on_page = extract_emails(driver.page_source)
                        if emails_on_page:
                            for email in emails_on_page:
                                if email not in all_emails:
                                    all_emails.add(email)
                                    with open(emails_file_path, 'a') as file:
                                        file.write(f"{email}\n")
                                    counter+=1
                                    print(f"{counter}: {phone} >> {email}")
                    except Exception as e:
                        print(f"Error while processing link {link}: {e}")
            except Exception as e:
                print(f"Error while processing phone number {phone}: {e}")
                continue

    finally:
        # Close the driver when you're done visiting all URLs
        if driver is not None:
            driver.quit()
