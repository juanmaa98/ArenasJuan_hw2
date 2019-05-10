Resultados_hw2.pdf: EspecTemblor.pdf TransformadaTemblor.pdf temblor.pdf EspectroSignal.pdf EspectroSum.pdf transformadasOndas.pdf ondas.pdf uvsw.pdf Resultados_hw2.tex
	pdflatex Resultados_hw2.tex
EspecTemblor.pdf : Fourier.py temblor.txt signal.dat signalSuma.dat
	python3 Fourier.py
TransformadaTemblor.pdf : Fourier.py temblor.txt signal.dat signalSuma.dat
	python3 Fourier.py
temblor.pdf : Fourier.py temblor.txt signal.dat signalSuma.dat
	python3 Fourier.py
EspectroSignal.pdf : Fourier.py temblor.txt signal.dat signalSuma.dat
	python3 Fourier.py
EspectroSum.pdf : Fourier.py temblor.txt signal.dat signalSuma.dat
	python3 Fourier.py
transformadasOndas.pdf : Fourier.py temblor.txt signal.dat signalSuma.dat
	python3 Fourier.py
ondas.pdf: Fourier.py temblor.txt signal.dat signalSuma.dat
	python3 Fourier.py

uvsw.pdf : Plots_hw2.py umax.dat
	python3 Plots_hw2.py

umax.dat : Edificio.cpp
	g++ Edificio.cpp
	./a.out
