# CMake generated Testfile for 
# Source directory: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step3
# Build directory: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step3/build
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(TutorialRuns "Tutorial" "25")
add_test(TutorialUsage "Tutorial")
set_tests_properties(TutorialUsage PROPERTIES  PASS_REGULAR_EXPRESSION "Usage:.*number")
add_test(TutorialComp4 "Tutorial" "4")
set_tests_properties(TutorialComp4 PROPERTIES  PASS_REGULAR_EXPRESSION "The square root of 4 is 2")
add_test(TutorialComp9 "Tutorial" "9")
set_tests_properties(TutorialComp9 PROPERTIES  PASS_REGULAR_EXPRESSION "The square root of 9 is 3")
add_test(TutorialComp25 "Tutorial" "25")
set_tests_properties(TutorialComp25 PROPERTIES  PASS_REGULAR_EXPRESSION "The square root of 25 is 5")
add_test(TutorialComp-25 "Tutorial" "-25")
set_tests_properties(TutorialComp-25 PROPERTIES  PASS_REGULAR_EXPRESSION "The square root of -25 is 0")
add_test(TutorialComp0.0001 "Tutorial" "0.0001")
set_tests_properties(TutorialComp0.0001 PROPERTIES  PASS_REGULAR_EXPRESSION "The square root of 0.0001 is 0.01")
subdirs(MathFunctions)
