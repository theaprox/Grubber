class Router:
    def __init__(self, layout):
        self.layout = layout
        self.current_page = None
        self.previous_page = None

    def clean(self):
        """Clear the current layout."""
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

    def load(self, page_widget):
        """Load the provided page widget."""
        if self.current_page is not None:
            self.previous_page = self.current_page

        self.clean()  # Clear existing page
        self.current_page = page_widget
        self.layout.addWidget(page_widget)  # Add the new page

    def go_back(self):
        """Go back to the previous page if available."""
        if self.previous_page is not None:
            self.load(self.previous_page)

    def load_initial(self, page_widget):
        """Load the initial page without setting a previous page."""
        self.clean()
        self.current_page = page_widget
        self.previous_page = None
        self.layout.addWidget(page_widget)

    def reset_navigation(self):
        """Reset navigation history."""
        self.current_page = None
        self.previous_page = None