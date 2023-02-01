import time

import pytest

from Loger import logclass
from requirements import Requirement


@pytest.mark.usefixtures("setup")
class Test_registration(logclass):
    def test_001(self):
        log = self.getthelogs()
        req = Requirement(self.driver)
        log.info("entered into website successfully")
        # req.user_id()
        log.info("user id entered")
        req.password()
        log.info("password entered")
        req.repeat_password()
        log.info("password entered")
        req.first_name()
        log.info("name entered")
        req.lst_name()
        log.info("last name entered")
        req.email()
        log.info("email entered")
        req.phone()
        log.info("phone entered")
        req.address1()
        log.info("adress1 entered")
        req.address2()
        log.info("address2 entered")
        req.city()
        log.info("city entered")
        req.state()
        log.info("state entered")
        req.zip()
        log.info("zip code entered")
        req.country()
        log.info("country entered")
        req.drop_down1()
        log.info("drop down selected ")
        req.drop_down2()
        log.info("drop down 2 selected ")
        req.checkbox1()
        log.info("checkbox tick ")
        req.checkbox2()
        log.info("checkbox tick ")
        req.save_btn()
        log.info("save button click ")
        time.sleep(3)
