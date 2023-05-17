OBJS = main.o addition.o subtraction.o multiplication.o division.o

calculator: $(OBJS)
	cc -o calculator $(OBJS)

%.o: %.c
	cc -c $^ -o $@

clean:
	rm -f $(OBJS) calculator
.PHONY: all
