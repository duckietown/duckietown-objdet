
targets=$(addprefix handle-,$(patsubst .ipynb,,$(wildcard *.ipynb)))

all: $(targets)


handle-%:
	jupyter nbconvert --to html --execute "$*"
	jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace "$*"

