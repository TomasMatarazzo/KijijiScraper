    def Extract( url , driver):

            driver.get(url)
            information = {
                'Page Link': url,
                'Date':'-',
                'Unique Id':'-',
                'Title': '-',
                'Description': '-',
                'Address': '-',
                'Phone': '-',
            }
            # Searching the information for each item of the dic
            #Finding id


            id = [int(s) for s in re.findall(r'-?\d+\.?\d*',url )][0]
            information['Unique Id'] = id

            # Finding url
            information['link'] = url;

            # Finding the Title

            title = driver.find_element(By.CSS_SELECTOR,
                                            "h1[class = 'title-2323565163'] ")
            print(title.text)
            information['Title'] = title.text

            # Finding the name of the profile

            # Finding the description

            des = driver.find_element(By.CSS_SELECTOR,
                                            "p").text

            number = [s for s in re.findall(r'\d\d\d.\d\d\d.\d\d\d\d',des)]

            information['Description'] = des
            try:
                information['Phone'] = number[0]
            except:
                information['Phone'] = '-'

            #Finding the date

            enter = False

            try:
                enter = True
                date = driver.find_element(By.CSS_SELECTOR,
                                            ".datePosted-383942873 time")
                date = date.get_attribute('datetime')

                date = date.split('T')

                date = date[0]

            except:
                date = driver.find_element(By.CSS_SELECTOR,
                                            ".datePosted-383942873 span")
                date = date.get_attribute('title')

            information['Date'] = date


        #Address

            address = driver.find_element(By.CSS_SELECTOR,
                                            ".address-3617944557").text
            print(address)

            information['Address'] = address

            return information