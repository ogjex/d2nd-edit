import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Vertical Tabs Example", size=(800, 600))
        
        # Main panel to hold all the components
        main_panel = wx.Panel(self)
        
        # Create a vertical box sizer for the main panel
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Create a horizontal box sizer for the banner and button
        banner_button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Banner panel
        banner_panel = wx.Panel(main_panel, size=(700, 100))
        banner_panel.SetBackgroundColour(wx.Colour(255, 255, 255))  # Set banner color
        
        # Add banner panel to the horizontal sizer
        banner_button_sizer.Add(banner_panel, 0, wx.EXPAND)
        
        # Button
        button = wx.Button(main_panel, label="Button", size=(100, 100))
        
        # Add spacer to push button to the right
        banner_button_sizer.AddStretchSpacer()
        
        # Add button to the horizontal sizer
        banner_button_sizer.Add(button, 0, wx.ALIGN_BOTTOM)
        
        # Add the banner-button sizer to the main vertical sizer
        main_sizer.Add(banner_button_sizer, 0, wx.EXPAND)
        
        # Notebook to hold the tabs
        notebook = wx.Notebook(main_panel, style=wx.NB_LEFT | wx.NB_MULTILINE)
        
        # Image list to store icons
        image_list = wx.ImageList(48, 48)  # Initial size of icons
        
          # Add tabs with icons only
        tab_labels = ["Inventory", "Monsters", "Drops", "Unused Tab", "Unused Tab", "Unused Tab"]
        for i, label in enumerate(tab_labels):
            page = wx.Panel(notebook)
            icon_path = f"img/tab_{i+1}.png"
            icon = wx.Bitmap(icon_path, wx.BITMAP_TYPE_PNG)
            #icon = image_list.Add(wx.Bitmap("icon_path", wx.BITMAP_TYPE_PNG))
            image_list.Add(icon)
            notebook.AddPage(page, "", imageId=i)  # Empty string for label
            sizer_page = wx.BoxSizer(wx.VERTICAL)
            label_text = wx.StaticText(page, label=label)
            sizer_page.Add(label_text, 0, wx.ALL, 10)
            page.SetSizer(sizer_page)
             
        # Set the image list for the notebook
        notebook.AssignImageList(image_list)
        
        # Add notebook to the main sizer
        main_sizer.Add(notebook, 1, wx.EXPAND)
        
        # Set main sizer for the main panel
        main_panel.SetSizer(main_sizer)
        
        # Center the frame on the screen
        self.Center()
        
        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()