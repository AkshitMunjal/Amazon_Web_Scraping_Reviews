from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import re


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://www.amazon.in/')
time.sleep(10)


sign_in_button = driver.find_element(By.XPATH,value='//*[@id="nav-link-accountList-nav-line-1"]')
sign_in_button.click()

try:
    email_input = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.ID, 'ap_email'))
        )
    email_input.send_keys('munjal.ginni@live.com')  # Replace with your email or phone number
    email_input.send_keys(Keys.ENTER)
except TimeoutException:
    print("Email input field not found!")
    driver.quit()

try:
    password_input = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'ap_password'))
    )
    password_input.send_keys('laksat@98')  # Replace with your password
    password_input.send_keys(Keys.ENTER)
except TimeoutException:
    print("Password input field not found!")
    driver.quit()

time.sleep(5)

amazon_search_box = driver.find_element(By.NAME,value='field-keywords')
amazon_search_box.send_keys("OnePlus Nord Buds 2r",Keys.ENTER)


my_product = []
my_links = []

def product_link():
    a_link_href = driver.find_elements(By.CSS_SELECTOR,value='div.a-section a.a-link-normal.s-line-clamp-2.s-link-style.a-text-normal')

    for text in a_link_href:
        try:
            my_product.append(text.text)
        except NoSuchElementException:
            my_product.append("N/A")

    print(my_product)
    print(len(my_product))

    for link in a_link_href:
        try:
            my_links.append(link.get_attribute('href'))
        except NoSuchElementException:
            my_links.append("N/A")

    print(my_links)
    print(len(my_links))

product_link()


driver.get(my_links[2])
time.sleep(2)
# print(my_links[0])
click_more_reviews = driver.find_element(By.XPATH,value='//*[@id="reviews-medley-footer"]/div[2]/a')
click_more_reviews.click()


# Deep Dive Into Product

my_star_ratings = []
my_comments_title = []
my_actual_comment = []
my_review_date = []
my_check_verification = []
my_color = []


while True:
    try:
        # star_ratings = driver.find_elements(By.XPATH, "//li[@data-hook='review' and @class='review aok-relative']//i[@data-hook='review-star-rating']//span")
        # comments_title = driver.find_elements(By.XPATH,"//li[@data-hook='review' and @class='review aok-relative']//a[@data-hook='review-title']//span[not(@class='a-icon-alt' or @class='a-letter-space' or @class='cr-translated-review-content aok-hidden')]")
        # actual_comment = driver.find_elements(By.XPATH,"//li[@data-hook='review' and @class='review aok-relative' and not(@id='RKLYO1WKC5EF2')]//span[@data-hook='review-body']")
        # review_date = driver.find_elements(By.XPATH,"//li[@data-hook='review' and @class='review aok-relative']//span[@data-hook='review-date']")
        # check_verification = driver.find_elements(By.XPATH,"//li[@data-hook='review' and @class='review aok-relative']//span[@data-hook='avp-badge']")

        star_ratings = driver.find_elements(By.XPATH,
                                            "//li[@data-hook='review' and @class='review aok-relative' and not(@id='RKLYO1WKC5EF2')]//i[@data-hook='review-star-rating']//span")
        comments_title = driver.find_elements(By.XPATH,
                                              "//li[@data-hook='review' and @class='review aok-relative' and not(@id='RKLYO1WKC5EF2')]//a[@data-hook='review-title']//span[not(@class='a-icon-alt' or @class='a-letter-space' or @class='cr-translated-review-content aok-hidden')]")
        actual_comment = driver.find_elements(By.XPATH,
                                              "//li[@data-hook='review' and @class='review aok-relative' and not(@id='RKLYO1WKC5EF2')]//span[@data-hook='review-body']")
        review_date = driver.find_elements(By.XPATH,
                                           "//li[@data-hook='review' and @class='review aok-relative' and not(@id='RKLYO1WKC5EF2')]//span[@data-hook='review-date']")
        check_verification = driver.find_elements(By.XPATH,
                                                  "//li[@data-hook='review' and @class='review aok-relative' and not(@id='RKLYO1WKC5EF2')]//span[@data-hook='avp-badge']")

        # color = driver.find_elements(By.XPATH,"//li[@data-hook='review' and @class='review aok-relative']//a[@data-hook='format-strip']")
        # reviews = driver.find_elements(By.XPATH, "//li[@data-hook='review' and @class='review aok-relative']")
        reviews = driver.find_elements(By.XPATH,
                                       "//li[@data-hook='review' and @class='review aok-relative' and not(@id='RKLYO1WKC5EF2')]")

        try:
            for item in star_ratings:
                my_star_ratings.append(item.get_attribute('innerHTML'))
        except NoSuchElementException:
            my_star_ratings.append("N/A")

        try:
            for item in comments_title:
                my_comments_title.append(item.text)
        except NoSuchElementException:
            my_comments_title.append("N/A")

        try:
            for item in actual_comment:
                my_actual_comment.append(item.text)
        except NoSuchElementException:
            my_actual_comment.append("N/A")

        try:
            for item in review_date:
                my_review_date.append(item.text)
        except NoSuchElementException:
            my_review_date.append("N/A")

        try:
            for item in check_verification:
                my_check_verification.append(item.text)
        except NoSuchElementException:
            my_check_verification.append("N/A")

        # Loop through each review and extract color
        for review in reviews:
            try:
                # Extract color option (if available)
                color_tag = review.find_element(By.XPATH, ".//a[@data-hook='format-strip']")
                my_color.append(color_tag.text.strip() if color_tag else "NA")
            except NoSuchElementException:
                my_color.append("NA")

        # Locate the "Next page" button using XPath
        try:
            next_page_button = driver.find_element(By.XPATH, '//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a')
            next_page_button.click()
            print("Clicked on the Next page button successfully!")

            time.sleep(3)

        except NoSuchElementException:
            print("No more pages to navigate.")
            break

    except NoSuchElementException:
        print("Error with scraping the reviews.")
        break  # Exit loop if there's an error while scraping

print("Collected Reviews:")
print(my_star_ratings)
print(len(my_star_ratings))

print(my_comments_title)
print(len(my_comments_title))

print(my_actual_comment)
print(len(my_actual_comment))

print(my_review_date)
print(len(my_review_date))

print(my_check_verification)
print(len(my_check_verification))

print(my_color)
print(len(my_color))


review = 0
for item in my_comments_title:
    review = review + 1
    print(f"{review}:{item}")

new_review = 0
for item in my_actual_comment:
    new_review = new_review + 1
    print(f"{new_review}:{item}")

driver.quit()

my_data = {"Ratings":my_star_ratings,"Comments_Title":my_comments_title,
           "Actual_Comment":my_actual_comment,"Review_Date_place":my_review_date,
           "Verified_or_Not?":my_check_verification,"Product_Color":my_color}


df = pd.DataFrame(my_data)
print(df.head())

df.to_csv("Reviews_OnePlus_Nord_Buds_2r.csv",index=True,header=True)
print("Data Printed Succesfully!!😁")
