###############################################################################
#
# dev commands
#
test:
	pytest .

###############################################################################
#
# release
#
release: release.applytag release.check release.build release.upload

release.applytag:
	echo $$(git describe --tags --abbrev=0 ) > finx_spreads_fx_ib/version.txt

release.check:
	pre-commit run -a
	git diff --quiet

release.build:
	python setup.py sdist bdist_wheel

release.upload:
	twine upload dist/*
