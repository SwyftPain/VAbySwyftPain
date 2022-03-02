#---------------------------------------
# Import Libraries
#
# This is where you will import any necessary
# libraries that you require for your Python Script.
#
#---------------------------------------
import cgi, clr, codecs, json, os, sys, urllib
sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

ScriptName = "VAbyAez"
Website = "https://www.aezrath.live"
Description = "Running VoiceAttack commands"
Creator = "Aezrath and Pfield"
Version = "1.0.3"

def Init():

    global settings
    with codecs.open(os.path.join(os.path.dirname(__file__), "settings.json"), encoding="utf-8-sig") as f:
        settings = json.load(f)
    return

def Execute(data):
	if data.IsChatMessage() and data.GetParam(0).startswith(settings["prefix"]):
		os.system(settings["va_location"] +' -command "' + data.Message[len(settings["prefix"]):].strip() + '"')
	return

def OpenReadMe():
    os.startfile(os.path.join(os.path.dirname(__file__), "README.txt"))

def Tick():
	return

#---------------------------
#   [Optional] Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
#---------------------------
def ReloadSettings(jsonData):
    # Execute json reloading here
    settings = json.loads(jsonData)
    return