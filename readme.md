# ocetesto

Program for automaticly run K.M Ocetkwieicz tests for
Algorithms and data strucutres exercises

(!important - program tests only output not execution time)

## Getting Started
Clone the repo
```
https://github.com/szymon6927/ocetesto.git
```
Next
```
cd ocetesto
```
After cloning I propose to set directory structure like bellow
![Example directory strucutre](/img/structure.JPG) 

So just create `externals` directory copy your .exe program and directory
with tests to previously created `externals` directory 

With strucutre like this one usage is:
```
python ocetesto.py -tests externals/tests/ -bin externals/main.exe
```

Generally:
* -tests path to directory with tests
* -bin path to executable program


### Prerequisites

Only required Python3


## License

This project is licensed under the MIT License
