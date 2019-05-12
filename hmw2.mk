Resultados_hw2.pdf: EspecTemblor.pdf TransformadaTemblor.pdf temblor.pdf EspectroSignal.pdf EspectroSum.pdf transformadasOndas.pdf ondas.pdf uvsw.pdf uw1.pdf uw2.pdf uw3.pdf uw4.pdf uvswf.pdf uw1f.pdf uw2f.pdf uw3f.pdf uw4f.pdf Resultados_hw2.tex
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

uvsw.pdf uw1.pdf uw2.pdf uw3.pdf uw4.pdf : Plots_hw2.py umax.dat uw1.dat uw2.dat uw3.dat uw4.dat
	python3 Plots_hw2.py

umax.dat uw1.dat uw2.dat uw3.dat uw4.dat: Edificio.cpp
	g++ Edificio.cpp
	./a.out

uvswf.pdf uw1f.pdf uw2f.pdf uw3f.pdf uw4f.pdf : Plots_hw2.py umaxf.dat uw1f.dat uw2f.dat uw3f.dat uw4f.dat
	python3 Plots_hw2.py

umaxf.dat uw1f.dat uw2f.dat uw3f.dat uw4f.dat: EdificioGamma.cpp
	g++ EdificioGamma.cpp
	./a.out
