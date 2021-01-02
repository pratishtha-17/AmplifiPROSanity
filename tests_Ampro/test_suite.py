import unittest
#from tests_Ampro.test_invalidlogin_csv_data import InvalidLoginCSVDataTests
#from tests_Ampro.test_loginA_csv_data import LoginCSVDataTests
from tests_Ampro.test_Covid19ResourceCentre import Covid19CSVDataTests
from tests_Ampro.test_tools_n_templates import ToolsCSVDataTests
#from tests_Ampro.test_categories import CategoriesCSVDataTests
from tests_Ampro.test_create_new_strategy import NewStrategyCSVDataTests
#from tests_Ampro.test_all_intelligence import AllIntelligenceCSVDataTests
#from tests_Ampro.test_resources import ResourcesCSVDataTests
#from tests_Ampro.test_solutions import SolutionsCSVDataTests

#tc1 = unittest.TestLoader().loadTestsFromTestCase(InvalidLoginCSVDataTests)
#tc2 = unittest.TestLoader().loadTestsFromTestCase(LoginCSVDataTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(Covid19CSVDataTests)
tc4 = unittest.TestLoader().loadTestsFromTestCase(ToolsCSVDataTests)
#tc5 = unittest.TestLoader().loadTestsFromTestCase(CategoriesCSVDataTests)
tc6 = unittest.TestLoader().loadTestsFromTestCase(NewStrategyCSVDataTests)
#tc7 = unittest.TestLoader().loadTestsFromTestCase(AllIntelligenceCSVDataTests)
#tc8 = unittest.TestLoader().loadTestsFromTestCase(ResourcesCSVDataTests)
#tc9 = unittest.TestLoader().loadTestsFromTestCase(SolutionsCSVDataTests)

SanitySuite = unittest.TestSuite([tc3,tc4,tc6])
unittest.TextTestRunner(verbosity=2).run(SanitySuite)