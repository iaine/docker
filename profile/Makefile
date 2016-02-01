lib = ./templates

dockerfile: $(lib)/*.m4
	m4 -I $(lib) ./$(lib)/Dockerfile.m4 > Dockerfile

build: dockerfile
	docker build -t profile .

clean:
	rm -rf Dockerfile
