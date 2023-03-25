#class is a blueprint
#has data, and behavior

class UITransform:
    screen_position
    dimensions

class UIElement :
    asset
    animation_handle
    ui_transform : UITransform

    UIElement(self):
        self.asset = "default.png"
        self.ui_transform.screen_position = (0, 0, 0)
        self.ui_transform.dimensions = (1, 1)
        self.animation_handle = None

    def OnClicked(self):
        pass

    def Draw(self):
        g_graphics.Draw(self.asset, self.ui_transform.screen_position, self.ui_transform.dimensions)

class UICheckbox (UIElement):
    is_checked = False
    checked_asset

    def Draw(self):
        if is_checked is True:
            g_graphics.Draw(self.checked_asset, self.ui_transform.screen_position, self.ui_transform.dimensions)
        else:
            g_graphics.Draw(self.asset, self.ui_transform.screen_position, self.ui_transform.dimensions)

class UIButton (UIElement):
    button_text
    is_clicked
    clicked_sound
    clicked_asset

    def Draw(self):
        if(is_clicked):
            g_graphics.Draw(self.clicked_asset, self.ui_transform.screen_position, self.ui_transform.dimensions)
        else:
            g_graphics.Draw(self.asset, self.ui_transform.screen_position, self.ui_transform.dimensions)

#     UIElement
#   /           \
# UIButton     UICheckbox

def Init():
    UIElement myInstance = UIElement.new()
    print(myInstance.asset)

    myInstance.asset = "Sprite.png"
    myInstance.Draw()
    
    show_helmet_checkbox = UICheckbox.new()
    show_helmet_checkbox.is_checked = True
    show_helmet_checkbox.Draw()

    yes_checkbox = UICheckbox.new()
    yes_checkbox.asset = "YesSprite.png"
    yes_checkbox.is_checked = False

    settings_button = UIButton.new()

    ui_elements : list[UIElement] = [show_helmet_checkbox, settings_button, yes_checkbox]
    for element in ui_elements:
        element.Draw()

def main():

    Init()

    while(True):
        UpdateTheGame()

        if TheGameIsDone():
            break
    
    Exit()

main() 


