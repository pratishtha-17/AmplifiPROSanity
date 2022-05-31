from pages_Ampro.navigation_page import NavigationPage
from selenium import webdriver
from pages_Ampro.sourcing_destinations_page import SourcingDestinationsPage
from utilities_Ampro.teststatus import StatusCheck
import unittest, pytest
from ddt import ddt, data, unpack
from utilities_Ampro.read_data import getCSVData
from pages_Ampro.navigation_page import NavigationPage
from configfiles_ampro import config

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class SourcingDestinationsCSVDataTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ts=StatusCheck(self.driver)
        self.sd=SourcingDestinationsPage(self.driver)
        self.nav=NavigationPage(self.driver)

    @pytest.mark.run(order=36)
    @data(*getCSVData("D:/Python/Automation2020/AmplifiPROSanity/Test Data_Ampro/testdata_sourcing_destinations.csv"))
    @unpack    
    def test_navigateToSourcingDestinations(self, CommodityGroup, Commodity, DestinationCountry): 
        config.text_commodity = Commodity
        config.text_country = DestinationCountry
        self.nav.navigateToAllIntelligence()
        self.nav.navigateToSourcingDestinations()  
        self.sd.FilterSelectionSourcingDestinations(CommodityGroup, Commodity, DestinationCountry)      
        result = self.sd.verifyNavigationToSourcingDestinations()
        self.ts.mark(result,"Navigation to Sourcing destinations and filter application done")

    @pytest.mark.run(order=37)    
    def test_downloadOnSourcingDestinations(self):    
        self.sd.downloadData()
        result = self.sd.verifyDownloadCompleted(config.text_commodity, config.text_country, ".xlsx")
        self.ts.markFinal("test_downloadOnSourcingDestinations", result, "Download Sourcing destinations data")        

    @pytest.mark.run(order=38)
    @data(*getCSVData("D:/Python/Automation2020/AmplifiPROSanity/Test Data_Ampro/testdata_tools_n_templates.csv"))
    @unpack     
    def test_shareOnSourcingDestinations(self,Email, Comment):    
        result = self.sd.fileSharing(Email, Comment)
        self.ts.markFinal("test_navigateToSourcingDestinations",result,"Navigation to Sourcing destinations and filter application done")  

    @pytest.mark.run(order=39)
    @data(*getCSVData("D:/Python/Automation2020/AmplifiPROSanity/Test Data_Ampro/testdata_sourcing_destinations.csv"))
    @unpack
    def test_addToFavouritesOnSourcingDestinations(self, CommodityGroup, Commodity, DestinationCountry):
        self.sd.addToFavourites(CommodityGroup, Commodity, DestinationCountry)
        result = self.sd.verifyAddToFavourites()
        self.ts.markFinal("test_addToFavouritesOnSourcingDestinations", result ,"Add To Favourites on Sourcing destinations")
   
    @pytest.mark.run(order=40)
    def test_copyLinkToClipboard(self):
        self.sd.copyLink() 
        result = self.sd.verifyLinkCopied()
        self.ts.markFinal("test_copyLinkToClipboard",result,"Copying link to Clipboard on Sourcing Destinations")  

    @pytest.mark.run(order=41)
    def test_NavigationToAdditionalIntelligence(self):
        self.sd.clickOnAdditionalIntelligence()
        result = self.sd.verifyNavigationToAdditionalIntelligence() 
        self.ts.markFinal("test_NavigationToAdditionalIntelligence", result, "Navigation to Additional Intelligence report dashboard")  
    
    @pytest.mark.run(order=42)
    def test_carouselClick(self):
        self.sd.clickOnCarousel()
        result = self.sd.verifyClickOnCarouselItems() 
        self.ts.markFinal("test_carouselClick", result, "Click on carousel items")     

      
