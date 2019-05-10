Resultados_hw2.pdf: EspecTemblor.pdf TransformadaTemplor.pdf temblor.pdf EspectroSignal.pdf EspectroSum.pdf transformadasOndas.pdf ondas.pdf uvsw.pdf umax.dat
	pdflatex Resultados_hw2.tex
EspecTemblor.pdf TransformadaTemplor.pdf temblor.pdf EspectroSignal.pdf EspectroSum.pdf transformadasOndas.pdf ondas.pdf: Fourier.py temblor.txt signal.dat signalSuma.dat
	python3 Fourier.py

uvsw.pdf : Plots_hw2.py umax.dat
	python3 Plots_hw2.py

umax.dat : Edificio.cpp
	g++ Edificio.cpp
	./a.out
