INC_DIR := .
SRC_DIR := .
OBJ_DIR := obj
OUT_DIR := out

C_FILES = cfunc.c
O_FILES := $(patsubst %.c, $(OBJ_DIR)/%.o, $(C_FILES))

TARGET = cfunc

# Compiler configuration
CC = g++

# Compiler warnings
C_DEF += -DDEBUG
C_WARN += -Wall -Wextra -Wconversion -Wsign-conversion -Weffc++ -Wno-unused-function
C_PARAMS += -fpic

# Linker parameters
L_PARAMS += -flto
L_PARAMS += -Wl,--gc-sections

.PHONY: all
all: static dynamic

prepare:
	mkdir -p $(OBJ_DIR)
	mkdir -p $(OUT_DIR)

list_out:
	ls -lh $(OUT_DIR)

$(OBJ_DIR)/%.o: $(C_FILES)
	@echo "# $<:"
	$(CC) $(C_PARAMS) $(C_DEF) $(C_WARN) -I$(INC_DIR) -c -o $@ $<

.PHONY: static
static: prepare $(O_FILES)
# Link object files
	@echo "# Linking $(TARGET).a"
	ar rcs $(OUT_DIR)/$(TARGET).a $(O_FILES)

# Create .S and .sym files
	@echo "# Disassembling $(TARGET).a"
	objdump -dS $(OUT_DIR)/$(TARGET).a > $(OUT_DIR)/$(TARGET).S
	objdump -t  $(OUT_DIR)/$(TARGET).a > $(OUT_DIR)/$(TARGET).sym

# Show sections size
	@echo "# Information for $(TARGET).a"
	size $(OUT_DIR)/$(TARGET).a

.PHONY: dynamic
dynamic: prepare $(O_FILES)
# Link object files
	@echo "# Linking $(TARGET).so"
	$(CC) -shared -o $(OUT_DIR)/$(TARGET).so $(O_FILES)

.PHONY: clean
clean:
	@echo "Cleaning generated files"
	rm -f $(OBJ_DIR)/*.o
	rm -f $(OUT_DIR)/$(TARGET).a
	rm -f $(OUT_DIR)/$(TARGET).so
	rm -f $(OUT_DIR)/$(TARGET).sym
	rm -f $(OUT_DIR)/$(TARGET).S
