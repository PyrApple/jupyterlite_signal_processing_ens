rm -Rf ./dist/*
jupyter lite build --config=jupyter_lite_config.json --output-dir=./dist/
jupyter lite serve --config=jupyter_lite_config.json --output-dir=./dist/