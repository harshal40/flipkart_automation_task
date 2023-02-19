import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# to intialise the browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
driver.implicitly_wait(5)

#to close the login popup
x_btn = driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']")
x_btn.click()

#search for the ipad
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("ipad")
search_bar.send_keys(Keys.ENTER)

#applying filters one by one to all 

pric_min = driver.find_element(By.XPATH, "(//select[contains(@class,'_2YxCDZ')])[1]")
pric_min.send_keys("₹5000")

pric_max = driver.find_element(By.XPATH, "(//select[contains(@class,'_2YxCDZ')])[2]")
pric_max.send_keys("20000+")


time.sleep(1)
f_assrd_btn = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, "(//div[@class='_24_Dny _3tCU7L'])[1]")))
f_assrd_btn.click()


time.sleep(1)
brand_filtr = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable(driver.find_element(By.XPATH, "//div[contains(text(),'Brand')]")))
brand_filtr.click()


brand_nam = driver.find_element(By.XPATH, "(//div[@class='_24_Dny'])[1]")
brand_nam.click()

time.sleep(1)
disply_filtr = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable(driver.find_element(By.XPATH, "//div[contains(text(),'Display Size')]")))
disply_filtr.click()

disply_inch = driver.find_element(By.XPATH, "//div[contains(text(),'7 - 8 Inch')]")
disply_inch.click()


time.sleep(1)
gst_inno_filtr = driver.find_element(By.XPATH, "(//div[@class='_2gmUFU _3V8rao'][normalize-space()='GST Invoice Available'])[1]")
gst_inno_filtr.click()

gst_inno_optn = driver.find_element(By.XPATH, "(//div[@class='_3879cV'][normalize-space()='GST Invoice Available'])[1]")
gst_inno_optn.click()


time.sleep(1)
connctivty_filtr = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable(driver.find_element(By.XPATH, "//div[contains(text(),'Connectivity')]")))
connctivty_filtr.click()

connctivty_optn = driver.find_element(By.XPATH, "(//div[@class='_3879cV'][normalize-space()='Wi-Fi+4G'])[1]")
connctivty_optn.click()


time.sleep(1)
cust_rtng_filtr = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable(driver.find_element(By.XPATH, "//div[contains(text(),'Customer Ratings')]")))
cust_rtng_filtr.click()

cust_rtng_optn = driver.find_element(By.XPATH, "(//label[@class='_2iDkf8 t0pPfW'])[1]")
cust_rtng_optn.click()


time.sleep(1)
intrnl_storg_filtr = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable(driver.find_element(By.XPATH, "//div[contains(text(),'Internal Storage')]")))
intrnl_storg_filtr.click()

intrnl_storg_optn = driver.find_element(By.XPATH, "(//div[@class='_3879cV'][normalize-space()='256 GB'])[1]")
intrnl_storg_optn.click()


time.sleep(1)
opertng_sys_filtr = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable(driver.find_element(By.XPATH, "//div[contains(text(),'Operating System')]")))
opertng_sys_filtr.click()

opertng_sys_optn = driver.find_element(By.XPATH, "//div[contains(text(),'iOS')]")
opertng_sys_optn.click()

time.sleep(1)
disply_qlty = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable(driver.find_element(By.XPATH, "(//div[@class='_2gmUFU _3V8rao'][normalize-space()='Display'])[1]")))
disply_qlty.click()

disply_qlty_optn = driver.find_element(By.XPATH, "//div[contains(text(),'Full HD')]")
disply_qlty_optn.click()

time.sleep(1)
primry_cam_filtr = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable(driver.find_element(By.XPATH, "(//div[@class='_213eRC _2ssEMF'])[9]")))
primry_cam_filtr.click()

primry_cam_optn = driver.find_element(By.XPATH, "(//div[contains(@class,'_3879cV')][contains(text(),'8MP')])[1]")
primry_cam_optn.click()

time.sleep(1)
vc_cl_filtr = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable(driver.find_element(By.XPATH, "(//div[contains(text(),'Voice Calling Facility')])[1]")))
vc_cl_filtr.click()

vc_cl_optn = driver.find_element(By.XPATH, "(//div[contains(@class,'_3879cV')][normalize-space()='No'])[1]")
vc_cl_optn.click()


time.sleep(1)
procesr_filtr = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable(driver.find_element(By.XPATH, "//div[contains(text(),'Processor Clock Speed')]")))
procesr_filtr.click()

procesr_optn = driver.find_element(By.XPATH, "//div[contains(text(),'Less than 1 GHz')]")
procesr_optn.click()

time.sleep(1)
avlblty_filtr = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable(driver.find_element(By.XPATH, "//div[contains(text(),'Availability')]")))
avlblty_filtr.click()

avlblty_optn = driver.find_element(By.XPATH, "//div[contains(text(),'Exclude Out of Stock')]")
avlblty_optn.click()


# click on show more soo able too see all applied filters
time.sleep(1)
clck_show_mor_filtr = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, "//div[@class='_2w_U27 _2fYv1H']")))
clck_show_mor_filtr.click()



# this for loop give's us all filter which we applied above
filtr_optn = driver.find_elements(By.XPATH, "//div[@class='_3ztiZO']")
for filtr in filtr_optn:
    print(filtr.text)


# click on ipad 
prod_selct_nw_win = driver.find_element(By.XPATH, "//img[@alt='APPLE ipad Mini (2019) 256 GB ROM 7.9 inch with Wi-Fi+4G (Space Grey)']")
prod_selct_nw_win.click()

# switching window 
driver.switch_to.window(driver.window_handles[1])

# click on add to cart button
ad_to_crt = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, "//button[@class='_2KpZ6l _2U9uOA _3v1-ww']")))
ad_to_crt.click()


# click on place order button
plce_ordr = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Place Order']")))
plce_ordr.click()

# enter random email to place order
entr_email = driver.find_element(By.XPATH, "//input[@type='text']")
entr_email.send_keys("example@gmail.com")
time.sleep(1)

# click on contnue
clck_contn = driver.find_element(By.XPATH, "//button[@type='submit']")
clck_contn.click()

# quit the browser
driver.quit()
