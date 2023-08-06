<h1>Email Extractor Unicode</h1>
<p>Email Extractor Unicode is a Python library that allows you to extract emails from web pages related to phone
   numbers. It utilizes the undetected_chromedriver library to browse web pages and extract emails using regular
   expressions.
</p>
<h2>Installation</h2>
<p>To install Email Extractor Unicode, you can use pip:</p>
<pre><code>pip install email-extractor-unicode</code></pre>
<h2>Usage</h2>
<p>To use the library, you can import the <code>extract_emails_from_phone_file</code> function from the package and
   call it with the path to the phone numbers file and the path where you want to save the extracted emails.
</p>
<pre><code>from email_extractor_unicode import extract_emails_from_phone_file

phone_file_path = 'path/to/phone.txt'
emails_file_path = 'path/to/emails.txt'

extract_emails_from_phone_file(phone_file_path, emails_file_path)</code></pre>
<p>Replace <code>'path/to/phone.txt'</code> with the file path containing phone numbers, and
   <code>'path/to/emails.txt'</code> with the desired file path to save the extracted emails.
</p>
<h2>Example</h2>
<pre><code>from email_extractor_unicode import extract_emails_from_phone_file

phone_file_path = 'phone.txt'
emails_file_path = 'emails.txt'

extract_emails_from_phone_file(phone_file_path, emails_file_path)</code></pre>
<h2>Contact</h2>
<p>For any inquiries or feedback, you can reach out to me on Telegram at <a href="https://t.me/iamunicode"
   target="_blank">@iamunicode</a>. I'd be happy to hear from you and assist with any questions or issues
   related to Email Extractor Unicode.
</p>
<h2>Disclaimer</h2>
<p>Please use this library responsibly and respect the terms of service of the websites you are scraping. Email
   extraction from websites may be subject to legal restrictions in some jurisdictions. Always ensure you have the
   right to extract data from the websites you visit.
</p>

<h2>Change Log</h2>
<ul>
    <li><strong>1.0.8 (07/31/2023)</strong></li>
    <ul>
        <li>Second Release</li>
        <li>Changed print(email) to print(f"{counter}: {phone} >> {email}") </li>
    </ul>
</ul>
