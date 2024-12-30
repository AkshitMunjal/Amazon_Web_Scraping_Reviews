
# Amazon Product Reviews Scraper

This project is a Python-based web scraper that automates the process of collecting and analyzing product reviews from Amazon using the Selenium library. The scraper logs into an Amazon account, searches for a specified product, navigates to its reviews section, and extracts valuable information such as star ratings, review titles, review content, verification status, review dates, and product variations (like color). The extracted data is organized into a structured format and saved as a CSV file for further analysis.


## Key Features:

✅Automated Login: Uses Selenium to log into Amazon securely with user credentials.

✅Product Search: Automatically searches for a specified product.

✅Review Extraction: Scrapes detailed reviews, including star ratings, review titles, full comments, verification status, and more.

✅Pagination Handling: Iterates through multiple pages of reviews to collect comprehensive data.

✅Data Storage: Stores the extracted data in a well-organized CSV file using Pandas.

✅Error Handling: Includes exception handling for missing elements and timeouts.
## Dependencies:

✔️Selenium

✔️Pandas

✔️Google Chrome/Chromium WebDriver

## Usage:

1. Install the required libraries using pip install    selenium pandas.

2. Download and set up the ChromeDriver compatible with your version of Chrome.

3. Update the script with your Amazon login credentials (email and password).

4. Run the script to search for a product and scrape its reviews.

5. Review the data in the generated CSV file.
## Output:

The script generates a CSV file containing the following columns:

⭐Ratings: Star ratings of the reviews.

💬Comments_Title: Title of the reviews.

💬Actual_Comment: Full review comments.

📅Review_Date_place: Date of the reviews and any additional location information.

❓Verified_or_Not?: Whether the purchase is verified or not.

🌈Product_Color: The color or variation of the product (if applicable).

## Potential Use Cases:

👉Market Research: Analyze consumer feedback to understand product strengths and weaknesses.

👉Sentiment Analysis: Perform text analysis on reviews to gauge customer sentiment.

👉Competitive Analysis: Compare reviews across products to evaluate market trends.

👉E-commerce Insights: Use the data to improve product listings or identify common customer concerns.

## Limitations:

👉Dynamic Content: Amazon's website layout may change over time, which could break the scraper. Maintenance may be required.

👉Legal Compliance: Ensure the scraper adheres to Amazon's terms of service to avoid legal issues.

👉Data Volume: For large datasets, scraping multiple pages may take significant time.

## Disclaimer:

This project is for educational purposes only. The user must ensure compliance with Amazon's terms of service and any applicable laws. Unauthorized scraping of data may result in account suspension or legal action.






