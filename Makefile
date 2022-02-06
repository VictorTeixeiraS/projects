all: lint

lint:
	# yarn lint
	black . --check
	cd projects && gofmt -l `find . -name '*.go' | grep -v vendor` 2>&1
	cd projects && test -z $$(gofmt -l `find . -name '*.go' | grep -v vendor` 2>&1)
