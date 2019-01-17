#Created by: Ashton VonBergen

#Check for existing Windows File Explorer window
if(exists("1545071809294.png")):
    click("1545071809294.png")
    wait(5)
    
#Check for existing Chrome window
if(exists("1540486053638.png")):
    click("1540486053638.png")
    wait(5)
    
#Main body of script
if(exists("1528366069988.png")): #Check for icon, exits script if it does not exist
    wait(5)
    doubleClick("1528366069988.png")
    wait(10)
    type("1540495355439.png", "https://cis.cernerworkswan.com/Citrix/greaseboardWeb/" + Key.ENTER)
    wait(5)
    type("1528366085495.png", "tbclsdcsdcgb2")
    wait(1)
    type("1528366095431.png", "M0ntana2")
    wait(1)
    click("1528366283674.png")
    wait(10)
    click("1528366312619.png") #Select Firstnet Greaseboard application
    wait(30)
    if(exists("1538666054667.png")): #Check for Permissions Dialog Box, exits statment if it does not exist
        click("1538666065521.png")
        click("1538666074201.png")
    wait(10)
    click("1540486053638.png") #Closes Chrome window in case Firstnet board times out
    wait(5)
    click("1538666247071.png") #Select Cerner Citrix login from taskbar
    wait(3)
    type("1528428987074.png", "tbclsdcsdcgb2")
    wait(1)
    type("1528366384081.png", "Tr@ck1ngB0@rd")
    wait(1)
    click("1528366404282.png")
    wait(15)
    click("1528367433871.png")
    wait(1)
    type("b")
    wait(1)