#Author: Cody Azevedo
#Language: Python v2.7
#Disneyland Recommender System Android Application

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from AttractionsList import ATTRACTIONS

#Load the window size in pixels
Window.size = (1080, 1920)
#This Builder loads the KV(kivy) file that contains the GUI for each screen
Builder.load_file("androidui.kv")

#Global variable, for use by the screens' functions
ride = []

#Initialize screens, pass contents
class ParkScreen(Screen):
    pass
class DisneylandAreaScreen(Screen):
    pass
class DCAAreaScreen(Screen):
    pass
class MainStreetScreen(Screen):
    pass
class TomorrowlandScreen(Screen):
    pass
class FantasylandScreen(Screen):
    pass
class ToontownScreen(Screen):
    pass
class FrontierlandScreen(Screen):
    pass
class CritterCountryScreen(Screen):
    pass
class NewOrleansScreen(Screen):
    pass
class AdventurelandScreen(Screen):
    pass
class BuenaVistaStreetScreen(Screen):
    pass
class ParadisePierScreen(Screen):
    pass
class GrizzlyPeakScreen(Screen):
    pass
class HollywoodlandScreen(Screen):
    pass
class ABugslandScreen(Screen):
    pass
class CarslandScreen(Screen):
    pass
class ShortWaitScreen(Screen):
    pass
class MediumWaitScreen(Screen):
    pass
class LongWaitScreen(Screen):
    pass
class VeryLongWaitScreen(Screen):
    pass
class ShortLongWaitScreen(Screen):
    pass
class ShortMediumWaitScreen(Screen):
    pass
class ShortMediumLongWaitScreen(Screen):
    pass

class FinalScreen(Screen):
    #Resets ride
    def resetRide(self, *args):
        global ride
        ride = []

#screenManager initializes and transitions screens when needed
#Returned in main method
def screenManager():
    
    sm = ScreenManager()
    sm.add_widget(ParkScreen(name='parkscreen'))
    sm.add_widget(DisneylandAreaScreen(name='disneylandareascreen'))
    sm.add_widget(DCAAreaScreen(name='dcaareascreen'))
    sm.add_widget(MainStreetScreen(name='mainstreetscreen'))
    sm.add_widget(ShortWaitScreen(name='shortwaitscreen'))
    sm.add_widget(MediumWaitScreen(name='mediumwaitscreen'))
    sm.add_widget(ShortLongWaitScreen(name='shortlongwaitscreen'))
    sm.add_widget(ShortMediumWaitScreen(name='shortmediumwaitscreen'))
    sm.add_widget(ShortMediumLongWaitScreen(name='shortmediumlongwaitscreen'))
    sm.add_widget(LongWaitScreen(name='longwaitscreen'))
    sm.add_widget(VeryLongWaitScreen(name='verylongwaitscreen'))
    sm.add_widget(TomorrowlandScreen(name='tomorrowlandscreen'))
    sm.add_widget(FantasylandScreen(name='fantasylandscreen'))
    sm.add_widget(ToontownScreen(name='toontownscreen'))
    sm.add_widget(FrontierlandScreen(name='frontierlandscreen'))
    sm.add_widget(CritterCountryScreen(name='crittercountryscreen'))
    sm.add_widget(NewOrleansScreen(name='neworleansscreen'))
    sm.add_widget(AdventurelandScreen(name='adventurelandscreen'))
    sm.add_widget(BuenaVistaStreetScreen(name='buenavistastreetscreen'))
    sm.add_widget(ParadisePierScreen(name='paradisepierscreen'))
    sm.add_widget(GrizzlyPeakScreen(name='grizzlypeakscreen'))
    sm.add_widget(HollywoodlandScreen(name='hollywoodlandscreen'))
    sm.add_widget(ABugslandScreen(name='abugslandscreen'))
    sm.add_widget(CarslandScreen(name='carslandscreen'))
    sm.add_widget(FinalScreen(name='finalscreen'))

    return sm

#Main class, contains app elements
class MainApp(App):

    #Set the title of the window
    title = 'Disneyland Ride Selector'
    #Set a string property for final ride
    finalride = StringProperty()

    #Allows self reference to app
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)

    #Logic for determining ride
    #Compares the set provided by the user with the sets in the attraction list
    def determineRide(self, *args):

        self.finalride = ""

        for key in ATTRACTIONS:
            if(set(ride) == ATTRACTIONS[key]):
                self.finalride += "\n - " + key #str(key) + "!"

    #Park setter methods
    def setParkDisneyland(self, *args):
        ride.append('Disneyland')
    def setParkDCA(self, *args):
        ride.append('DCA')

    #Area setter methods
    #Disneyland
    def setAreaMainStreet(self, *args):
        ride.append('Main Street USA')
    def setAreaTomorrowland(self, *args):
        ride.append('Tomorrowland')
    def setAreaFantasyland(self, *args):
        ride.append('Fantasyland')
    def setAreaMickeysToontown(self, *args):
        ride.append('Mickey\'s Toontown')
    def setAreaFrontierland(self, *args):
        ride.append('Frontierland')
    def setAreaCritterCountry(self, *args):
        ride.append('Critter Country')
    def setAreaNewOrleans(self, *args):
        ride.append('New Orleans Square')
    def setAreaAdventureland(self, *args):
        ride.append('Adventureland')
    #DCA
    def setAreaBuenaVistaStreet(self, *args):
        ride.append('Buena Vista Street')
    def setAreaParadisePier(self, *args):
        ride.append('Paradise Pier')
    def setAreaGrizzlyPeak(self, *args):
        ride.append('Grizzly Peak')
    def setAreaHollywoodLand(self, *args):
        ride.append('Hollywood Land')
    def setAreaABugsLand(self, *args):
        ride.append('A Bug\'s Land')
    def setAreaCarsLand(self, *args):
        ride.append('Cars Land')

    #Time setter methods
    def setTimeShort(self, *args):
        ride.append('Short')
    def setTimeMedium(self, *args):
        ride.append('Medium')
    def setTimeLong(self, *args):
        ride.append('Long')
    def setTimeVeryLong(self, *args):
        ride.append('Very Long')

    #Type setter methods
    def setTypeSlow(self, *args):
        ride.append('Slow')
    def setTypeFast(self, *args):
        ride.append('Fast')
    def setTypeGettingAround(self, *args):
        ride.append('Getting Around')
    def setTypeSpinning(self, *args):
        ride.append('Spinning')
    def setTypeShow(self, *args):
        ride.append('Show')
    def setTypeWater(self, *args):
        ride.append('Water')

    #For debugging purposes
    def printRide(self, *args):
        print ride

    #Builds the app by returning screenManager()
    def build(self):
        return screenManager()

#Main loop, starts program
if __name__ == "__main__":
	MainApp().run()
