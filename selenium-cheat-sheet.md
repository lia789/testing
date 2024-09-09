# **Selenium**


## **Documentation**
```
Selenium Docs: https://selenium-python.readthedocs.io/index.html
Web driver manager: https://github.com/SergeyPirogov/webdriver_manager
```


```
What are list of things setup on client machine?
0. Project Directory
1. Python
2. Python virtual env
3. VS Code, VS Code setting, and VS code extensions
4. Jupyter Notebook
5. Selenium Setup
```

```python
# Import Selenium library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Using Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://quotes.toscrape.com/')



# Locating Elements
# By ID
element = driver.find_element(By.ID, "element_id")

# By Name
element = driver.find_element(By.NAME, "element_name")

# By Class Name
element = driver.find_element(By.CLASS_NAME, "element_class")

# By CSS Selector
element = driver.find_element(By.CSS_SELECTOR, "css_selector")

# By XPath
element = driver.find_element(By.XPATH, "//*[@id='element_id']")

# By Tag Name
element = driver.find_element(By.TAG_NAME, "tag_name")

# By Link Text
element = driver.find_element(By.LINK_TEXT, "link_text")

# By Partial Link Text
element = driver.find_element(By.PARTIAL_LINK_TEXT, "partial_link_text")



# Common Element Actions
# Click an element
element.click()

# Send text to an input box
element.send_keys("text to input")

# Clear text from an input box
element.clear()

# Submit a form
element.submit()

# Simulate pressing Enter key
element.send_keys(Keys.RETURN)


# Handling Waits
#Implicit Waits
driver.implicitly_wait(10)  # seconds

# Explicit Waits
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'element_id')))


# Handling Browser Actions
# Navigate forward and back
driver.back()
driver.forward()

# Refresh the page
driver.refresh()

# Maximize the browser window
driver.maximize_window()

# Get current page URL
current_url = driver.current_url

# Get page title
page_title = driver.title

# Taking Screenshots
# Save a screenshot
driver.save_screenshot('screenshot_name.png')




# Scrolling the Page
# Scroll by a specific amount
driver.execute_script("window.scrollBy(0, 500);")

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Scroll to an element
element = driver.find_element(By.ID, "element_id")
driver.execute_script("arguments[0].scrollIntoView();", element)



# Handling Dropdowns
from selenium.webdriver.support.ui import Select

# Locate the dropdown element
dropdown = Select(driver.find_element(By.ID, 'dropdown_id'))

# Select by visible text
dropdown.select_by_visible_text('Option 1')

# Select by index
dropdown.select_by_index(1)

# Select by value
dropdown.select_by_value('value1')


# Keyboard and Mouse Actions
from selenium.webdriver.common.action_chains import ActionChains

# Move to an element and click
actions = ActionChains(driver)
element = driver.find_element(By.ID, "element_id")
actions.move_to_element(element).click().perform()

# Double-click an element
actions.double_click(element).perform()

# Right-click an element
actions.context_click(element).perform()

# Drag and drop
source = driver.find_element(By.ID, 'source_id')
target = driver.find_element(By.ID, 'target_id')
actions.drag_and_drop(source, target).perform()





# Closing and Quitting the Browser
# Close the current tab
driver.close()

# Close the browser completely
driver.quit()



## Running Headless Browser
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(executable_path='path_to_chromedriver', options=options)




```
