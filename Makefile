test:
	python3 -m unittest

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
.PHONY: clean

clean:
	@rm -f $(TARGET) $(OBJECTS) core

