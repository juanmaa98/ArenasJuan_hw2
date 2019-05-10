uvsw.pdf : Plots_hw2.py umax.dat
	python3 Plots_hw2.py

umax.dat : Edificio.cpp
	g++ Edificio.cpp
	./a.out
