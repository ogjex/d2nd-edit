import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="D2ND Content Manager", size=(800, 650))
        
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
        image_list = wx.ImageList(200, 48)  # Initial size of icons
        
        # Add tabs with icons only
        tab_labels = ["Monsters", "Inventory", "Drops", "Backup and restore", "Content Manager Settings"]
        for i, label in enumerate(tab_labels):
            page = wx.Panel(notebook)
            icon_path = f"img/tab_{i+1}.png"
            icon = wx.Bitmap(icon_path, wx.BITMAP_TYPE_PNG)
            image_list.Add(icon)
            notebook.AddPage(page, "", imageId=i)  # Empty string for title
            sizer_page = wx.BoxSizer(wx.VERTICAL)
            if label == "Monsters":

                # Add Sizer to add content to
                monsters_sizer = wx.BoxSizer(wx.VERTICAL)

                # Add Tab title label
                title_text = wx.StaticText(page, label="Monster Modifications")
                title_text.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
                title_text.SetForegroundColour(wx.Colour(0, 0, 0))  # Set text color
                title_text.Wrap(300)  # Wrap text if it exceeds 300 pixels in width
                title_text.SetSize(title_text.GetBestSize())  # Adjust the size according to the text
                monsters_sizer.Add(title_text, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

                # Add content for Monsters tab
                difficulty_text = wx.StaticText(page, label="Difficulty:")
                monsters_sizer.Add(difficulty_text, 0, wx.ALL, 5)
                # Add checkboxes
                checkboxes = ["Easy", "Medium", "Hard"]
                for checkbox_label in checkboxes:
                    checkbox = wx.CheckBox(page, label=checkbox_label)
                    monsters_sizer.Add(checkbox, 0, wx.ALL, 5)
                
                # Add Monster Density label
                density_text = wx.StaticText(page, label="Monster Density:")
                monsters_sizer.Add(density_text, 0, wx.ALL, 5)
                
                # Add slider for Monster Density
                slider_density = wx.Slider(page, value=1, minValue=1, maxValue=8, size=(300, -1), style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_LABELS)
                monsters_sizer.Add(slider_density, 0, wx.ALL, 5)
               
                # Add Champion label
                champion_text = wx.StaticText(page, label="Champion Rarity")
                monsters_sizer.Add(champion_text, 0, wx.ALL, 5)
                
                # Add slider for Champion
                slider_champion = wx.Slider(page, value=1, minValue=1, maxValue=8, size=(300, -1), style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_LABELS)
                monsters_sizer.Add(slider_champion, 0, wx.ALL, 5)

                # Add Unique label
                unique_text = wx.StaticText(page, label="Unique Rarity:")
                monsters_sizer.Add(unique_text, 0, wx.ALL, 5)
                
                # Add slider for Unique
                slider_unique = wx.Slider(page, value=1, minValue=1, maxValue=8, size=(300, -1), style=wx.SL_HORIZONTAL|wx.SL_AUTOTICKS|wx.SL_LABELS)
                monsters_sizer.Add(slider_unique, 0, wx.ALL, 5)

                # Add Reset button
                reset_button = wx.Button(page, label="Reset values", size=(100, 50))
                monsters_sizer.Add(reset_button, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

                # Add monsters_sizer to the page sizer
                sizer_page.Add(monsters_sizer, 0, wx.ALL, 10)

            else:
                # Placeholder content for other tabs
                label_text = wx.StaticText(page, label=label)
                sizer_page.Add(label_text, 0, wx.ALL, 10)
            page.SetSizer(sizer_page)

        # Set the image list for the notebook
        notebook.AssignImageList(image_list)
        
        # Add notebook to the main sizer
        main_sizer.Add(notebook, 1, wx.EXPAND)
        
        # Save button
        save_button = wx.Button(main_panel, label="Save", size=(200, 48))
        main_sizer.Add(save_button, 0, wx.ALIGN_LEFT | wx.BOTTOM, border=10)

        # Set main sizer for the main panel
        main_panel.SetSizer(main_sizer)
        
        # Center the frame on the screen
        self.Center()
        
        self.Show()

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
