from RPA.Browser.Selenium import Selenium
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create a new instance
browser = Selenium()

class Robot:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"************* Hello My Name is {self.name}, I am going to get Scientist Details *****************************")

    def open_wikipedia_page(self,scientist):
        print(f"******************************************* {scientist} ****************************************************")
        print()
        print(f"---> I am going to open a web browser and navigate to wikipedia page of {scientist}....")
        print()

        # Open the webpage from availble browser
        browser.open_available_browser("https://www.wikipedia.org")

        #Enter scientist name in search input box
        browser.input_text("id=searchInput", scientist)

        #Click on search button to get redirected to wikipedia page of the scientist
        browser.click_button("css=#search-form button[type='submit']")

        #Wait for the page to load
        browser.wait_until_element_is_visible("id=searchInput")

    def extract_first_paragraph(self):
        print("---> Now, I am going to extract the first paragraph from this wikipedia page....")
        # Find the <p> element without any class inside <div class="mw-parser-output">
        p_element = browser.find_element("xpath:.//div[@class='mw-parser-output']/p[not(@class)]")

        print("About:")
        # Print the visible text
        print(p_element.text)
        print()

        with open("Scientist_details.txt", 'a', encoding='utf-8') as file:
        # Write the content to the file
            file.write(p_element.text)
            file.write('\n')

    def extract_birth_death_date(self):
        print("---> Extracting birth and death date....")
        print()
        #Get <span> that contains class="bday"
        birth_day_element = browser.get_webelement("css=td.infobox-data span.bday")

        #Extract birth date in text format
        birth_date_text = birth_day_element.get_attribute("textContent")

        print("Birth Date: ", birth_date_text)

        # Find the <th> element with the text "Died"
        died_parent_element = browser.find_element("xpath://th[contains(text(), 'Died')]")

        # Find the child <td> element of the parent <th> element
        died_child_element = browser.find_element("xpath:./following-sibling::td", parent=died_parent_element)

        # Get the innerHTML of the child <td> element
        died_html = browser.get_element_attribute(died_child_element, "innerHTML")

        # Remove parentesis and get died date
        start_tag = "<span style=\"display:none\">("
        end_tag = ")</span>"
        died_date_text = died_html.split(start_tag)[1].split(end_tag)[0]

        print("Death Date: ", died_date_text)
        print()

        # Declare date format 
        date_format = "%Y-%m-%d"

        # Convert the date string to a datetime object
        birth_date_object = datetime.strptime(birth_date_text, date_format)
        death_date_object = datetime.strptime(died_date_text, date_format)

        print("---> Calculating Age....")
        print()
        # Calculate age
        scientist_age = relativedelta(death_date_object, birth_date_object).years

        print("Age:", scientist_age)
        print()

        with open("Scientist_details.txt", 'a', encoding='utf-8') as file:
        # Write the content to the file
            file.write(f"Birth Date: {birth_date_text}\n")
            file.write(f"Death Date: {died_date_text}\n")
            file.write(f"Age: {scientist_age}\n")
            file.write('\n\n')
            file.write("---------------------------------------------------------------------------------------------------------------------\n")

    def extract_details(self, scientist):
        
        self.open_wikipedia_page(scientist)
        self.extract_first_paragraph()
        self.extract_birth_death_date()

    def say_goodbye(self):
        print("******************************************* Good Bye ****************************************************")

