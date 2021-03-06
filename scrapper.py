from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep


driver = webdriver.Chrome()

driver.get("https://result.ganpatuniversity.ac.in")
sleep(2)
en = "18162121001"

en_bda_list = []
for i in range(1,40):
    if(i<=9):
        en = "1816212100"+str(i)
    else:
        en = "181621210"+str(i)
    en_bda_list.append(en)

print(en_bda_list)

def Process():
    global en_bda_list
    for en in en_bda_list:
        college = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[1]/td[2]/select/option[17]").click()
        branch = driver.find_element_by_xpath('//*[@id="ddlDegree"]/option[5]').click()
        sem = driver.find_element_by_xpath('//*[@id="ddlSem"]/option[6]').click()
        exam = driver.find_element_by_xpath('//*[@id="ddlScheduleExam"]/option[2]').click()
        en_element = driver.find_element_by_xpath('//*[@id="txtEnrNo"]').send_keys(en)

        show_marksheet = driver.find_element_by_xpath('//*[@id="btnSearch"]').click()

        driver.execute_script("document.body.style.zoom='67%'")

        destination= en+".png"
        if driver.save_screenshot(destination):
            print(en+" saved in destination path")
        else:
            print(en+" could not be stored")
        
        driver.get("https://result.ganpatuniversity.ac.in")
        sleep(1)

Process()