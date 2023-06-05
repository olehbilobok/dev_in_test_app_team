from framework.login_page import LoginPage


class Sidebar(LoginPage):

    def click_sidebar(self, find_by, selector):

        sidebar = self.find_element(find_by, selector)

        if sidebar:
            self.click_element(sidebar)

    def sidebar_main_elements(self, find_by, selector_parent, selector_child):

        sidebar_parent = self.find_element(find_by, selector_parent)

        if sidebar_parent:
            sidebar_elements = sidebar_parent.find_elements_by_class_name(selector_child)

            return [element.get_attribute('text') for element in sidebar_elements]

    def sidebar_documentation(self, find_by, selector):

        documentation = self.find_element(find_by, selector)

        if documentation:
            return documentation.get_attribute('text')

    def sidebar_build(self, find_by, selector):

        build = self.find_element(find_by, selector)

        if build:
            return build.get_attribute('text')

    def sidebar_main(self, email, password):

        sidebar_all_elements = []

        login = self.main(email, password)

        if login == 'Add your first hub to start managing the security system':

            self.click_sidebar('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                        'android.widget.FrameLayout/android.widget.LinearLayout/'
                                        'android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/'
                                        'android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[2]/'
                                        'android.view.ViewGroup/android.widget.FrameLayout/android.widget.ImageView')

            sidebar_main_element = self.sidebar_main_elements('class_name', 'androidx.recyclerview.widget.RecyclerView',
                                                                            'android.widget.TextView')

            sidebar_all_elements.extend(sidebar_main_element)

            sidebar_documentation = self.sidebar_documentation('id', 'com.ajaxsystems:id/documentation_text')

            sidebar_all_elements.append(sidebar_documentation)

            sidebar_build = self.sidebar_build('id', 'com.ajaxsystems:id/build')

            sidebar_all_elements.append(sidebar_build)

        else:
            return f'Not authorized: {login}'

        return sidebar_all_elements
