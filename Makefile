# Objects & binary
OBJ    = $(patsubst %.c, %.o, $(wildcard src/*.c))
TARGET = main

# Tools
CC      ?= gcc
CFLAGS  ?= -Wall -Wextra -Wpedantic -Wshadow -Wconversion -g -O0 -std=c17 -Iinclude

# Default: build
all: $(TARGET).exe

$(TARGET).exe: $(OBJ)
	$(CC) $(OBJ) -o $(TARGET).exe

# Compile .c -> .o
src/%.o: src/%.c
	$(CC) $(CFLAGS) -c $< -o $@

# Housekeeping
clean:
	$(RM) src/*.o $(TARGET).exe

.PHONY: all clean
