from selenium import webdriver
from bs4 import BeautifulSoup
import time

def test(profile_url):


	# profile_url = ""
	print("hiii")


	# Now using beautiful soup
	# soup = BeautifulSoup(src, 'lxml')
	# intro = soup.find('div', {'class': 'pv-text-details__left-panel'})
	#
	# # print(intro)
	# # In case of an error, try changing the tags used here.
	#
	# name_loc = intro.find("h1")
	#
	# # Extracting the Name
	# name = name_loc.get_text().strip()
	# # strip() is used to remove any extra blank spaces
	#
	# works_at_loc = intro.find("div", {'class': 'text-body-medium'})
	#
	# # this gives us the HTML of the tag in which the Company Name is present
	# # Extracting the Company Name
	# works_at = works_at_loc.get_text().strip()
	#
	#
	# location_loc = intro.find_all("span", {'class': 'text-body-small'})
	#
	# # Ectracting the Location
	# # The 2nd element in the location_loc variable has the location
	# location = location_loc[0].get_text().strip()
	#
	# print("Name -->", name,
	# 	"\nWorks At -->", works_at)
	# Getting the HTML of the Experience section in the profile
	try:
		options = webdriver.ChromeOptions()
		options.headless = False
		options.headless= True
		# Creating an instance
		driver = webdriver.Chrome(chrome_options=options)
		profile_url = str(profile_url)
		# Logging into LinkedIn
		driver.get("https://linkedin.com/uas/login")
		# time.sleep(0)

		username = driver.find_element("id", "username")
		username.send_keys("rudra.s.singh20@gmail.com")  # Enter Your Email Address

		pword = driver.find_element("id", "password")
		pword.send_keys("rudra2811")  # Enter Your Password

		driver.find_element("xpath", "//button[@type='submit']").click()
		driver.get(profile_url)  # this will open the link
		print("hiii")
		start = time.time()

		# will be used in the while loop
		initialScroll = 0
		finalScroll = 1000

		while True:
			driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
			# this command scrolls the window starting from
			# the pixel value stored in the initialScroll
			# variable to the pixel value stored at the
			# finalScroll variable
			initialScroll = finalScroll
			finalScroll += 1000

			# we will stop the script for 3 seconds so that
			# the data can load
			time.sleep(1)
			# You can change it as per your needs and internet speed

			end = time.time()

			# We will scroll for 20 seconds.
			# You can change it as per your needs and internet speed
			if round(end - start) > 2:
				break
		src = driver.page_source
		soup = BeautifulSoup(src, 'lxml')
		intro = soup.find('div', {'class': 'pv-text-details__left-panel'})

		# print(intro)
		# In case of an error, try changing the tags used here.

		name_loc = intro.find("h1")

		# Extracting the Name
		name = name_loc.get_text().strip()
		# strip() is used to remove any extra blank spaces

		works_at_loc = intro.find("div", {'class': 'text-body-medium'})

		# this gives us the HTML of the tag in which the Company Name is present
		# Extracting the Company Name
		works_at = works_at_loc.get_text().strip()


		# Ectracting the Location
		# The 2nd element in the location_loc variable has the location

		# print("Name -->", name,
		# 	  "\nWorks At -->", works_at)
		# print(intro)
		experience = soup.find("li", {"class": "pv-text-details__right-panel-item"})
		company_loc=experience.find_all("div",{"inline-show-more-text inline-show-more-text--is-collapsed inline-show-more-text--is-collapsed-with-line-clamp inline"})

		# for name in company_loc:
		# 	print(name.get_text().strip())
		# print(experience)
		print(company_loc[0].get_text().strip())
		return company_loc[0].get_text().strip(),name
		# photuu=soup.find("div",{"class":"pv-top-card--photo text-align-left pv-top-card--photo-resize"})
		# print(photuu)
	except:
		company_name="NAN"
		Name="NAN"
		print(company_name)
		return company_name,Name
# test('https://www.linkedin.com/in/shivam-verma-1554b9223')
