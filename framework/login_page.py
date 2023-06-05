import time
from framework.page import Page


class LoginPage(Page):

    def open_login_form(self, find_by, selector):

        login_button = self.find_element(find_by, selector)

        if login_button:
            self.click_element(login_button)

    def enter_email(self, find_by, selector, keys):

        email_input = self.find_element(find_by, selector)

        if email_input:
            email_input.send_keys(keys)

    def enter_password(self, find_by, selector, keys):

        password_input = self.find_element(find_by, selector)

        if password_input:
            password_input.send_keys(keys)

    def click_login(self, find_by, selector):

        confirm_login = self.find_element(find_by, selector)

        if confirm_login.get_attribute('enabled'):
            self.click_element(confirm_login)

        return confirm_login.get_attribute('enabled')

    def display_greetings(self, find_by, selector):

        greetings = self.find_element(find_by, selector)

        if greetings:
            return greetings.get_attribute('text')

    def display_error(self, find_by, selector):

        error = self.find_element(find_by, selector)

        if error:
            return error.get_attribute('text')

    def main(self, email, password):

        self.open_login_form('id', 'com.ajaxsystems:id/authHelloLogin')

        self.enter_email('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                  'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                                  'android.widget.FrameLayout/android.view.ViewGroup/'
                                  'androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[1]/'
                                  'androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.EditText',
                         email)

        self.enter_password('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                     'android.widget.FrameLayout/android.widget.LinearLayout/'
                                     'android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/'
                                     'androidx.recyclerview.widget.RecyclerView[1]/android.widget.FrameLayout[2]/'
                                     'androidx.compose.ui.platform.ComposeView/android.view.View/'
                                     'android.widget.EditText', password)

        login = self.click_login('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                          'android.widget.FrameLayout/android.widget.LinearLayout/'
                                          'android.widget.FrameLayout/android.widget.FrameLayout/'
                                          'android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[2]/'
                                          'android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/'
                                          'android.view.View/android.view.View')

        time.sleep(2)

        if login == 'true':

            error_message = self.display_error('id', 'com.ajaxsystems:id/snackbar_text')

            if not error_message:

                greetings_message = self.display_greetings('id', 'com.ajaxsystems:id/addFirstHub')

                return greetings_message

            return error_message

        return login
