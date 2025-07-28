"""
🌱 Earth911 Recycling Locator Scraper
------------------------------------
✅ Automates the process of searching for recycling centers on Earth911.com.
✅ Extracts: Business Name, Address (3 lines combined), and Materials Accepted.
✅ Saves all data into a CSV file for further analysis.
"""

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# -------------------------
# Function to close popup if it appears
# -------------------------
def popup_check():
    """Checks for and closes the popup window if it appears."""
    try:
        close_button = driver.find_element(By.CLASS_NAME, "_close")
        close_button.click()
        time.sleep(1)  # small delay to ensure popup closes
    except:
        pass  # if no popup, continue silently

# -------------------------
# SETUP SECTION
# -------------------------

# Create a list to store scraped data
data = []

# Setup Chrome WebDriver using WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# -------------------------
# STEP 1: Open Earth911 Search Page
# -------------------------
driver.get("https://search.earth911.com/")
time.sleep(3)
popup_check()

# -------------------------
# STEP 2: Enter search parameters
# -------------------------
# Enter “Electronics” in the “Search for” box
search_box = driver.find_element(By.ID, "what")
search_box.clear()
search_box.send_keys("Electronics")

# Enter ZIP code “10001”
zip_box = driver.find_element(By.ID, "where")
zip_box.clear()
zip_box.send_keys("10001")

popup_check()

# -------------------------
# STEP 3: Click Search Button
# -------------------------
search_button = driver.find_element(By.ID, "submit-location-search")
search_button.click()
time.sleep(5)  # Wait for results to load
print("✅ Search submitted successfully")

popup_check()

# -------------------------
# STEP 4: Select 100 miles from the dropdown
# -------------------------
dropdown = driver.find_element(By.CSS_SELECTOR, "div.result-range select")
radius_dropdown = Select(dropdown)
radius_dropdown.select_by_value("100")
time.sleep(3)  # Wait for page refresh after selection

popup_check()

# -------------------------
# STEP 5: Scrape Results
# -------------------------
results = driver.find_elements(By.CSS_SELECTOR, "li.result-item")  # All search results on page

for r in results:
    # ✅ Extract Business Name
    try:
        business_name = r.find_element(By.CSS_SELECTOR, "h2.title a").text
    except:
        business_name = ""

    # ✅ Extract Address (combine all lines)
    try:
        address1 = r.find_element(By.CSS_SELECTOR, "p.address1").text
    except:
        address1 = ""
    try:
        address2 = r.find_element(By.CSS_SELECTOR, "p.address2").text
    except:
        address2 = ""
    try:
        address3 = r.find_element(By.CSS_SELECTOR, "p.address3").text
    except:
        address3 = ""

    # Combine non-empty address parts
    full_address = ", ".join([a for a in [address1, address2, address3] if a])

    # ✅ Extract Materials Accepted
    try:
        materials_spans = r.find_elements(By.CSS_SELECTOR, "span.material")
        materials = ", ".join([m.text for m in materials_spans if m.text])
    except:
        materials = ""

    # Append scraped data to list
    data.append({
        "business_name": business_name,
        "street_address": full_address,
        "materials": materials
    })

# -------------------------
# STEP 6: Save Data to CSV
# -------------------------
df = pd.DataFrame(data)
df.to_csv("earth911_page1.csv", index=False, encoding="utf-8-sig")
print(f"✅ Scraped {len(results)} items from page 1")

# -------------------------
# STEP 7: Close the Browser
# -------------------------
driver.quit()
print("🚪 Browser closed")
