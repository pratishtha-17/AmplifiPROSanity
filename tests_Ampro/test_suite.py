import unittest
from tests_Ampro.test_invalidlogin_csv_data import InvalidLoginCSVDataTests
from tests_Ampro.test_validlogin_csv_data import LoginCSVDataTests
from tests_Ampro.test_home_page import HomePageTests
from tests_Ampro.test_add_to_favourite import AddToFavouriteTests
from tests_Ampro.test_create_new_strategy import NewStrategyCSVDataTests
from tests_Ampro.test_topical_insights import TopicalInsightsTests
from tests_Ampro.test_categories import CategoriesCSVDataTests
from tests_Ampro.test_all_intelligence import AllIntelligenceCSVDataTests
from tests_Ampro.test_tools_n_templates import ToolsCSVDataTests
from tests_Ampro.test_sourcing_destinations import SourcingDestinationsCSVDataTests
from tests_Ampro.test_resources import ResourcesCSVDataTests
from tests_Ampro.test_solutions import SolutionsCSVDataTests
from tests_Ampro.test_request_custom_intelligence import RequestCustomIntelligenceTests

tc1 = unittest.TestLoader().loadTestsFromTestCase(InvalidLoginCSVDataTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(LoginCSVDataTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(HomePageTests)
tc4 = unittest.TestLoader().loadTestsFromTestCase(AddToFavouriteTests)
tc5 = unittest.TestLoader().loadTestsFromTestCase(NewStrategyCSVDataTests)
tc6 = unittest.TestLoader().loadTestsFromTestCase(TopicalInsightsTests)
tc7 = unittest.TestLoader().loadTestsFromTestCase(CategoriesCSVDataTests)
tc8 = unittest.TestLoader().loadTestsFromTestCase(AllIntelligenceCSVDataTests)
tc9 = unittest.TestLoader().loadTestsFromTestCase(ToolsCSVDataTests)
tc10 = unittest.TestLoader().loadTestsFromTestCase(SourcingDestinationsCSVDataTests)
tc11 = unittest.TestLoader().loadTestsFromTestCase(ResourcesCSVDataTests)
tc12 = unittest.TestLoader().loadTestsFromTestCase(SolutionsCSVDataTests)
tc13 = unittest.TestLoader().loadTestsFromTestCase(RequestCustomIntelligenceTests)

SanitySuite = unittest.TestSuite([tc1,tc2,tc3,tc4,tc5,tc6,tc7,tc8,tc9,tc10,tc11,tc12,tc13])
#SanitySuite = unittest.TestSuite([tc10])
unittest.TextTestRunner(verbosity=2).run(SanitySuite)