# CLI to generate code files with given name and functions


## Installation

```shell
$ git clone https://github.com/QxEcR/cpp-newfile-CLI.git
$ cd cpp-newfile-CLI
$ pip3 install .
```

## Usage c++

### Case 1. create a cpp file with no functions
#### Command -> cpp-nf {filename with no extension}
```shell
$ cpp-nf main
```

### Case 2. create a cpp file with one functions
#### Command -> cpp-nf {filename with no extension} {function name:function type}
```shell
$ cpp-nf main print:void
```


### Case 3. create a cpp file with n number of functions
#### Command -> cpp-nf {filename with no extension} {function name:function type} {function name:function type} ...
```shell
$ cpp-nf main print:void getNum:int getChar:char
```

## Usage Java

### Case 1. create a java file with no functions
#### Command -> jv-nf {filename with no extension}
```shell
$ jv-nf main
```

### Case 2. create a java file with one functions
#### Command -> jv-nf {filename with no extension} {function name:function type}
```shell
$ cpp-nf main print:void
```


### Case 3. create a java file with n number of functions
#### Command -> jv-nf {filename with no extension} {function name:function type} {function name:function type} ...
```shell
$ jv-nf main print:void getNum:int getChar:char
```

