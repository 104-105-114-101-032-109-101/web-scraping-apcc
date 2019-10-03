import xlwt
from selenium import webdriver

# Start web driver
driver = webdriver.Chrome()
driver.get("http://www.apcc.pt/centros/")

# Create first auxiliary file (used for tracing and debugging the data extraction)
auxFile = open('aux1.txt', 'a', encoding='utf-8')

for i in range(1, 84):
    # Access each associate page
    driver.find_element_by_xpath(f"/html/body/section/div[2]/div/div/section/article[{i}]").click()
    # Extract HTML information and write it into the file
    auxFile.write(driver.find_element_by_xpath(
        "/html/body/section/div[2]/div/div/article/div[2]/table/tbody").get_attribute('innerHTML'))
    # go back to the associates page
    driver.get("http://www.apcc.pt/centros/")
    auxFile.write("-----separator-----")
    
auxFile.close()
driver.quit()


# Remove HTML tags and clean each line to put it into a spreadsheet
def clean_line(lin):
    tag = False
    quote = False
    result = ""
    for character in lin:
        if character == '<' and not quote:
            tag = True
        elif character == '>' and not quote:
            tag = False
        elif (character == '"' or character == "'") and tag:
            quote = not quote
        elif not tag:
            result = result + character
    return result


# Gather information from the first aux file
# Create the second auxiliary file (used for tracing and debugging the formatting)
sourceFile = open("aux1.txt", "r", encoding='utf-8')
outputFile = open('aux2.txt', 'a', encoding='utf-8')

# Clean each line
for line in sourceFile:
    outputFile.write(clean_line(line))

sourceFile.close()
outputFile.close()


# Gather information from the second aux file
sourceFile = open("aux2.txt", "r", encoding='utf-8')

# Create the final spreadsheet
wb = xlwt.Workbook()
mainSheet = wb.add_sheet('Centros Comerciais')

attributes = {"Contacto": 1, "Promotor": 2, "Proprietário": 3, "Gestor": 4, "Área Bruta Locável(ABL)": 5, "Nº Lojas": 6,
              "Morada": 7, "Código Postal": 8, "Localidade": 9, "Telefone": 10, "Fax": 11, "Email": 12, "Website": 13}

# Organize each attribute in one column
for attribute in attributes:
    mainSheet.write(0, attributes[attribute], attribute)

# Distribute information according to each attribute
businessIndex = 0
for line in sourceFile:
    if "-----separator-----" in line:
        businessIndex += 1
    for attribute in attributes:
        if (attribute + ":") in line:
            mainSheet.write(businessIndex, attributes[attribute], line.replace(attribute + ":", "").strip())

wb.save('result.xls')
sourceFile.close()
