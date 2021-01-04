class Login:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_link_text("登 录").click()
