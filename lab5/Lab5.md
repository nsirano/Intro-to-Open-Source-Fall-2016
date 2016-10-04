# Lab 5: Build Systems - CMake Tutorial

##Step 1:
`cmake ..`
>-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step1/build

`make`
>Scanning dependencies of target Tutorial
[ 50%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
[100%] Linking CXX executable Tutorial
[100%] Built target Tutorial


##Step 2:
`cmake ..`
>-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step2/build

`make`
>Scanning dependencies of target MathFunctions
[ 25%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
[ 50%] Linking CXX static library libMathFunctions.a
[ 50%] Built target MathFunctions
Scanning dependencies of target Tutorial
[ 75%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
[100%] Linking CXX executable Tutorial
[100%] Built target Tutorial


##Step 3:
`cmake ..`
>-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step3/build

`make`
>Scanning dependencies of target MathFunctions
[ 25%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
[ 50%] Linking CXX static library libMathFunctions.a
[ 50%] Built target MathFunctions
Scanning dependencies of target Tutorial
[ 75%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
[100%] Linking CXX executable Tutorial
[100%] Built target Tutorial

`ctest ..`
>Test project /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step3/build
    Start 1: TutorialRuns
1/7 Test #1: TutorialRuns .....................   Passed    0.00 sec
    Start 2: TutorialUsage
2/7 Test #2: TutorialUsage ....................   Passed    0.00 sec
    Start 3: TutorialComp4
3/7 Test #3: TutorialComp4 ....................   Passed    0.00 sec
    Start 4: TutorialComp9
4/7 Test #4: TutorialComp9 ....................   Passed    0.00 sec
    Start 5: TutorialComp25
5/7 Test #5: TutorialComp25 ...................   Passed    0.00 sec
    Start 6: TutorialComp-25
6/7 Test #6: TutorialComp-25 ..................   Passed    0.00 sec
    Start 7: TutorialComp0.0001
7/7 Test #7: TutorialComp0.0001 ...............   Passed    0.00 sec
100% tests passed, 0 tests failed out of 7
Total Test time (real) =   0.03 sec


##Step 4:
`cmake ..`
>-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for log
-- Looking for log - not found
-- Looking for exp
-- Looking for exp - not found
-- Configuring done
-- Generating done
-- Build files have been written to: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step4/build

`make`
>Scanning dependencies of target MathFunctions
[ 25%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
[ 50%] Linking CXX static library libMathFunctions.a
[ 50%] Built target MathFunctions
Scanning dependencies of target Tutorial
[ 75%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
[100%] Linking CXX executable Tutorial
[100%] Built target Tutorial

`ctest ..`
>Test project /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step4/build
    Start 1: TutorialRuns
1/7 Test #1: TutorialRuns .....................   Passed    0.00 sec
    Start 2: TutorialUsage
2/7 Test #2: TutorialUsage ....................   Passed    0.00 sec
    Start 3: TutorialComp4
3/7 Test #3: TutorialComp4 ....................   Passed    0.00 sec
    Start 4: TutorialComp9
4/7 Test #4: TutorialComp9 ....................   Passed    0.00 sec
    Start 5: TutorialComp25
5/7 Test #5: TutorialComp25 ...................   Passed    0.00 sec
    Start 6: TutorialComp-25
6/7 Test #6: TutorialComp-25 ..................   Passed    0.00 sec
    Start 7: TutorialComp0.0001
7/7 Test #7: TutorialComp0.0001 ...............   Passed    0.00 sec
100% tests passed, 0 tests failed out of 7
Total Test time (real) =   0.04 sec


##Step 5:
`cmake ..`
>-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for log
-- Looking for log - not found
-- Looking for exp
-- Looking for exp - not found
-- Configuring done
-- Generating done
-- Build files have been written to: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step5/build

`make`
>Scanning dependencies of target MakeTable
[ 14%] Building CXX object MathFunctions/CMakeFiles/MakeTable.dir/MakeTable.cxx.o
[ 28%] Linking CXX executable MakeTable
[ 28%] Built target MakeTable
[ 42%] Generating Table.h
Scanning dependencies of target MathFunctions
[ 57%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
[ 71%] Linking CXX static library libMathFunctions.a
[ 71%] Built target MathFunctions
Scanning dependencies of target Tutorial
[ 85%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
[100%] Linking CXX executable Tutorial
[100%] Built target Tutorial

`ctest ..`
>Test project /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step5/build
    Start 1: TutorialRuns
1/7 Test #1: TutorialRuns .....................   Passed    0.00 sec
    Start 2: TutorialUsage
2/7 Test #2: TutorialUsage ....................   Passed    0.00 sec
    Start 3: TutorialComp4
3/7 Test #3: TutorialComp4 ....................   Passed    0.00 sec
    Start 4: TutorialComp9
4/7 Test #4: TutorialComp9 ....................   Passed    0.00 sec
    Start 5: TutorialComp25
5/7 Test #5: TutorialComp25 ...................   Passed    0.00 sec
    Start 6: TutorialComp-25
6/7 Test #6: TutorialComp-25 ..................   Passed    0.00 sec
    Start 7: TutorialComp0.0001
7/7 Test #7: TutorialComp0.0001 ...............   Passed    0.00 sec
100% tests passed, 0 tests failed out of 7
Total Test time (real) =   0.04 sec

##Step 6:
`cmake ..`
>-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for log
-- Looking for log - not found
-- Looking for exp
-- Looking for exp - not found
-- Configuring done
-- Generating done
-- Build files have been written to: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step6/build

`make`
>Scanning dependencies of target MakeTable
[ 14%] Building CXX object MathFunctions/CMakeFiles/MakeTable.dir/MakeTable.cxx.o
[ 28%] Linking CXX executable MakeTable
[ 28%] Built target MakeTable
[ 42%] Generating Table.h
Scanning dependencies of target MathFunctions
[ 57%] Building CXX object MathFunctions/CMakeFiles/MathFunctions.dir/mysqrt.cxx.o
[ 71%] Linking CXX static library libMathFunctions.a
[ 71%] Built target MathFunctions
Scanning dependencies of target Tutorial
[ 85%] Building CXX object CMakeFiles/Tutorial.dir/tutorial.cxx.o
[100%] Linking CXX executable Tutorial
[100%] Built target Tutorial

`ctest ..`
>Test project /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step6/build
    Start 1: TutorialRuns
1/7 Test #1: TutorialRuns .....................   Passed    0.00 sec
    Start 2: TutorialUsage
2/7 Test #2: TutorialUsage ....................   Passed    0.00 sec
    Start 3: TutorialComp4
3/7 Test #3: TutorialComp4 ....................   Passed    0.00 sec
    Start 4: TutorialComp9
4/7 Test #4: TutorialComp9 ....................   Passed    0.00 sec
    Start 5: TutorialComp25
5/7 Test #5: TutorialComp25 ...................   Passed    0.00 sec
    Start 6: TutorialComp-25
6/7 Test #6: TutorialComp-25 ..................   Passed    0.00 sec
    Start 7: TutorialComp0.0001
7/7 Test #7: TutorialComp0.0001 ...............   Passed    0.00 sec
100% tests passed, 0 tests failed out of 7
Total Test time (real) =   0.04 sec

`cpack --config CPackConfig.cmake`
>CPack: Create package using STGZ
CPack: Install projects
CPack: - Run preinstall target for: Tutorial
CPack: - Install project: Tutorial
CPack: Create package
CPack: - package: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step6/build/Tutorial-1.0.1-Linux.sh generated.
CPack: Create package using TGZ
CPack: Install projects
CPack: - Run preinstall target for: Tutorial
CPack: - Install project: Tutorial
CPack: Create package
CPack: - package: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step6/build/Tutorial-1.0.1-Linux.tar.gz generated.
CPack: Create package using TZ
CPack: Install projects
CPack: - Run preinstall target for: Tutorial
CPack: - Install project: Tutorial
CPack: Create package
CPack: - package: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step6/build/Tutorial-1.0.1-Linux.tar.Z generated.

`cpack --config CPackSourceConfig.cmake`
>CPack: Create package using TBZ2
CPack: Install projects
CPack: - Install directory: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step6
CPack: Create package
CPack: - package: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step6/build/Tutorial-1.0.1-Source.tar.bz2 generated.
CPack: Create package using TGZ
CPack: Install projects
CPack: - Install directory: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step6
CPack: Create package
CPack: - package: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step6/build/Tutorial-1.0.1-Source.tar.gz generated.
CPack: Create package using TXZ
CPack: Install projects
CPack: - Install directory: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step6
CPack: Create package
CPack: - package: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step6/build/Tutorial-1.0.1-Source.tar.xz generated.
CPack: Create package using TZ
CPack: Install projects
CPack: - Install directory: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step6
CPack: Create package
CPack: - package: /home/nick/School/Open_Source/Labs/My_Labs--CSCI2961_Fall_2016/lab5/Tutorial/Step6/build/Tutorial-1.0.1-Source.tar.Z generated.
