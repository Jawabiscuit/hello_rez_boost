# hello_rez_boost

A [rez](https://github.com/nerdvegas/rez) package which contains a small bit of code from `boost`'s getting started page for testing a new [rez boost package](https://github.com/Jawabiscuit/rez-packages/tree/main/boost) installation or trying out boost for the first time.

[boost Getting Started](https://www.boost.org/doc/libs/1_78_0/more/getting_started/index.html)


## Building

`cd` to the `src` directory


### Windows

The walk-through below is focused on Windows but building on another platform should be very similar. Testing and feedback using a Linux or Mac is welcome!


__Without rez__

Open an x64 developer command prompt with boost variables (`BOOST` and `BOOST_INCLUDEDIR`) configured, see "Getting Started".

Continue with the next steps, omitting rez commands.


__With rez__

The examples below use either the `msvc` or the `vs` package [here](https://github.com/Jawabiscuit/rez-packages)


__MSVC Build Tools rez pkg__

1. Rez Env - `rez env msvc-14.16 boost`

2. Configure - `cmake -H. -Bbuild -G "Ninja"`

3. Build - `cmake --build build --config Debug`


__Visual Studio IDE rez pkg__

1. Rez Env - `rez env vs-15 boost -- devenv .`

VS UI should launch. Using the menus...

CMake cache should generate automatically when project is opened with the above rez command

1. If you need to manually generate, right-click CMakeLists.txt -> Cache... -> Generate Cache

2. Right-click CMakeLists.txt -> build -> hello_boost.exe


__Building rez package__

cd to root package dir and...

`rez build -i`


## Running

**With rez**
`rez env hello_boost`

**On Windows**
`pwsh` (if not already in a pwsh)

**pwsh or bash**
`echo 1 2 3 | hello_boost`
