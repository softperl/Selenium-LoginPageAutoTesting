import time
import random
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

username = [
    "John@gmail.com", "Alice@gmail.com", "Michael@gmail.com", "Emily@gmail.com", "David@gmail.com", "Sophia@gmail.com", "Daniel@gmail.com", "Olivia@gmail.com",
"Matthew@gmail.com", "Emma@gmail.com", "Christopher@gmail.com", "Ava@gmail.com", "Andrew@gmail.com", "Isabella@gmail.com", "Joseph@gmail.com", "Mia@gmail.com",
"William@gmail.com", "Abigail@gmail.com", "James@gmail.com", "Ella@gmail.com", "Alexander@gmail.com", "Sofia@gmail.com", "Ethan@gmail.com", "Charlotte@gmail.com",
"Mason@gmail.com", "Amelia@gmail.com", "Benjamin@gmail.com", "Harper@gmail.com", "Logan@gmail.com", "Lily@gmail.com", "Henry@gmail.com", "Grace@gmail.com",
"Jackson@gmail.com", "Chloe@gmail.com", "Lucas@gmail.com", "Aria@gmail.com", "Aiden@gmail.com", "Evelyn@gmail.com", "Samuel@gmail.com", "Hannah@gmail.com",
"Sebastian@gmail.com", "Avery@gmail.com", "Carter@gmail.com", "Scarlett@gmail.com", "Matthew@gmail.com", "Layla@gmail.com", "Owen@gmail.com", "Zoey@gmail.com",
"Wyatt@gmail.com", "Addison@gmail.com", "Gabriel@gmail.com", "Eleanor@gmail.com", "Jayden@gmail.com", "Nora@gmail.com", "David@gmail.com", "Luna@gmail.com",
"Jack@gmail.com", "Riley@gmail.com", "Luke@gmail.com", "Camila@gmail.com", "Leo@gmail.com", "Penelope@gmail.com", "Ryan@gmail.com", "Leah@gmail.com",
"Isaac@gmail.com", "Natalie@gmail.com", "Dylan@gmail.com", "Savannah@gmail.com", "Nathan@gmail.com", "Victoria@gmail.com", "Caleb@gmail.com", "Brooklyn@gmail.com",
"Isaiah@gmail.com", "Stella@gmail.com", "Josiah@gmail.com", "Lillian@gmail.com", "Anthony@gmail.com", "Zoe@gmail.com", "Eli@gmail.com", "Ellie@gmail.com",
"Aaron@gmail.com", "Hailey@gmail.com", "Elijah@gmail.com", "Paisley@gmail.com", "Hunter@gmail.com", "Audrey@gmail.com", "Liam@gmail.com", "Skylar@gmail.com",
"Landon@gmail.com", "Violet@gmail.com", "Christian@gmail.com", "Claire@gmail.com", "Jonathan@gmail.com", "Bella@gmail.com", "Grayson@gmail.com", "Aurora@gmail.com",
"Charles@gmail.com", "Lucy@gmail.com", "Thomas@gmail.com", "Anna@gmail.com", "Connor@gmail.com", "Samantha@gmail.com", "MAJ_GHAFOOR@gmail.com"
]

password = [
    "John123", "Alice123", "Michael123", "Emily123", "David123", "Sophia123", "Daniel123", "Olivia123",
    "Matthew123", "Emma123", "Christopher123", "Ava123", "Andrew123", "Isabella123", "Joseph123", "Mia123",
    "William123", "Abigail123", "James123", "Ella123", "Alexander123", "Sofia123", "Ethan123", "Charlotte123",
    "Mason123", "Amelia123", "Benjamin123", "Harper123", "Logan123", "Lily123", "Henry123", "Grace123",
    "Jackson123", "Chloe123", "Lucas123", "Aria123", "Aiden123", "Evelyn123", "Samuel123", "Hannah123",
    "Sebastian123", "Avery123", "Carter123", "Scarlett123", "Matthew123", "Layla123", "Owen123", "Zoey123",
    "Wyatt123", "Addison123", "Gabriel123", "Eleanor123", "Jayden123", "Nora123", "David123", "Luna123",
    "Jack123", "Riley123", "Luke123", "Camila123", "Leo123", "Penelope123", "Ryan123", "Leah123",
    "Isaac123", "Natalie123", "Dylan123", "Savannah123", "Nathan123", "Victoria123", "Caleb123", "Brooklyn123",
    "Isaiah123", "Stella123", "Josiah123", "Lillian123", "Anthony123", "Zoe123", "Eli123", "Ellie123",
    "Aaron123", "Hailey123", "Elijah123", "Paisley123", "Hunter123", "Audrey123", "Liam123", "Skylar123",
    "Landon123", "Violet123", "Christian123", "Claire123", "Jonathan123", "Bella123", "Grayson123", "Aurora123",
    "Charles123", "Lucy123", "Thomas123", "Anna123", "Connor123", "Samantha123","Medix123@123"
]


driver= webdriver.Chrome()
driver.get('https://contrafinder.com/login')
time.sleep(2)

for x in range(101):
    driver.find_element(By.XPATH,'//input[@placeholder="Email address"]').send_keys(random.choice(username))
    time.sleep(2)
    driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys(random.choice(password))
    time.sleep(2)
    driver.find_element(By.XPATH,'//button[@class="btn btn-log btn-block btn-thm form-submit"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//input[@placeholder="Email address"]').clear()
    time.sleep(2)
    driver.find_element(By.XPATH,'//input[@placeholder="Password"]').clear()
    time.sleep(2)
while(True):
    pass