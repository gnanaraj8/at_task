#inspect element Data
class Homepage:
    logo_xpath="//*[@id='nava']/img"

class Signup:
    signup_button="signin2"
    signup_username="sign-username"
    signup_password="sign-password"
    signup_submit_button="//*[@id='signInModal']/div/div/div[3]/button[2]"
class Login:
    login_button="login2"
    login_usernam="loginusername"
    login_password="loginpassword"
    login_submit="//*[@id='logInModal']/div/div/div[3]/button[2]"
class Category:
    select_phone="itemc"
    select_samsung="//*[@id='tbodyid']/div[1]/div/div/h4/a"
    select_add_cart="//*[@id='tbodyid']/div[2]/div/a"


class Cart:
    select_cart="//*[@id='navbarExample']/ul/li[4]/a"
    select_plac_order="//*[@id='page-wrapper']/div/div[2]/button"
    input_name="name"
    input_country="country"
    input_city="city"
    input_credit_card="card"
    input_month="month"
    input_year="year"
    select_purchase="//*[@id='orderModal']/div/div/div[3]/button[2]"

class Logout:
    select_logout="logout2"

