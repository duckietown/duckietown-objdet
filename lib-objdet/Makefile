all:


bump-upload:
	$(MAKE) bump
	$(MAKE) upload
	
bump:
	bumpversion patch

upload:
	git push --tags
	git push
	rm -f dist/*
	python setup.py sdist
	twine upload dist/*


comptest_package=duckietown_objdet_tests
out=out-comptests
coverage_dir=out-coverage
coverage_include='*src/duckietown_objdet*'
coveralls_repo_token=HadPvWiCB5xwwbdcqYVBPyKe7GV0DR3it
coverage_run=coverage run

tests-clean:
	rm -rf $(out) $(coverage_dir) .coverage .coverage.*

junit:
	mkdir -p $(out)/junit
	comptests-to-junit $(out)/compmake > $(out)/junit/junit.xml

tests:
	comptests --nonose $(comptest_package)

tests-contracts:
	comptests --contracts --nonose  $(comptest_package)

tests-contracts-coverage:
	$(MAKE) tests-coverage-single-contracts
	$(MAKE) coverage-report
	$(MAKE) coverage-coveralls

tests-coverage:
	$(MAKE) tests-coverage-single-nocontracts
	$(MAKE) coverage-report
	$(MAKE) coverage-coveralls


tests-coverage-single-nocontracts:
	-DISABLE_CONTRACTS=1 comptests -o $(out) --nonose -c "exit"  $(comptest_package)
	-DISABLE_CONTRACTS=1 $(coverage_run)  `which compmake` $(out)  -c "rmake"

tests-coverage-single-contracts:
	-DISABLE_CONTRACTS=1 comptests -o $(out) --nonose -c "exit"  $(comptest_package)
	-DISABLE_CONTRACTS=0 $(coverage_run)  `which compmake` $(out) --contracts -c "rmake"

tests-coverage-parallel-contracts:
	-DISABLE_CONTRACTS=1 comptests -o $(out) --nonose -c "exit" $(package)
	-DISABLE_CONTRACTS=0 $(coverage_run)  `which compmake` $(out) --contracts -c "rparmake"

coverage-report:
	coverage combine
	coverage html -d $(coverage_dir)

coverage-coveralls:
	COVERALLS_REPO_TOKEN=$(coveralls_repo_token) coveralls





#branch=$(shell git rev-parse --abbrev-ref HEAD)
#
#tag_rpi=duckietown/rpi-duckietown-shell:$(branch)
#tag_x86=duckietown/duckietown-shell:$(branch)
#
#build: build-rpi build-x86
#
#push: push-rpi push-x86
#
#build-rpi:
#	docker build -t $(tag_rpi) -f Dockerfile.rpi .
#
#build-x86:
#	docker build -t $(tag_x86) -f Dockerfile .
#
#build-x86-no-cache:
#	docker build -t $(tag_x86) -f Dockerfile --no-cache .
#
#push-rpi:
#	docker push $(tag_rpi)
#
#push-x86:
#	docker push $(tag_x86)
#
#test:
#	make -C testing
