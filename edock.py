from calendar import c
from pywinauto.application import Application
import time

def automate_edock():

    app = Application(backend="uia").start("C:\Program Files (x86)\Estes Express Line\DockWorkerAppInstaller\eDock.exe")
    time.sleep(5)
    forkliftID = app['pnlLogin']['Edit2']
    forkliftID.type_keys("891984")

    operatorID = app['pnlLogin']['Edit']
    operatorID.type_keys("01008")

    loginButton = app['pnlLogin']['btnLogIn']
    loginButton.click_input()
    time.sleep(5)
    noScale = app['frmCalibration']['Button']
    noScale.click_input()
    app['eDock'].child_window(title="Manifest", auto_id="btnManifest", control_type="Button").click_input()
    time.sleep(5)
    app['eDock']['frmViewManifest'].child_window(auto_id="txtID", control_type="Edit").type_keys("842")
    time.sleep(2)
    app['eDock']['Bay'].click()
    time.sleep(2)
    app['eDock']['frmViewManifest'].child_window(title="Pro Number Row 3", control_type="DataItem").click_input()
    time.sleep(7)
    app['eDock']['Pickup Door'].wait('visible', timeout=10)
    app['eDock'].child_window(title=">", auto_id="btnNext", control_type="Button").click_input() 
    app['eDock'].child_window(title="No-Wgt", auto_id="btnNoWgt", control_type="Button").click_input()
    app['eDock'].child_window(title="DIM-Frt", auto_id="btnFreightDimension", control_type="Button").click_input()
    app['eDock'].child_window(auto_id="txtFreightDimUnits", control_type="Edit").type_keys("D008")
    app['eDock'].child_window(title="Start Dim", auto_id="btnFreightDimOk", control_type="Button").click_input()
    app['eDock'].child_window(title="Drop Door", auto_id="lblDoor", control_type="Text").wait('visible', timeout=10)
    app['eDock'].child_window(title="New / Undo", auto_id="btnNew", control_type="Button").click_input()
    app['eDock'].child_window(title="OK", auto_id="btnOK", control_type="Button").click_input()
    app['eDock'].child_window(title="Logout", auto_id="btnLogout", control_type="Button").click_input()
    app['eDock'].child_window(auto_id="btnYes", control_type="Button").click_input()
    app['frmLogin'].child_window(title="Close", control_type="Button").click_input()








 
  
   




   
if __name__ == "__main__":
    automate_edock()
    