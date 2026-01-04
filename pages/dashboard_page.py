class DashboardPage:
    def check_welcome_message(self):
        text = self.page.text_content(".oxd-topbar-header-breadcrumb")
        assert "Dashboard" in text

    def check_menu_links(self):
        menu_items = self.page.query_selector_all(
            ".oxd-main-menu-item-wrapper")
        expected = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info"]
        assert all(item.inner_text() in expected for item in menu_items)
