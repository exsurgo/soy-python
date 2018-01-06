#!/usr/bin/env bash

set -e

# Location of required python compiler runtime files
RUNTIME_DIR="runtime"

# Location of .soy templates
TEMPLATE_DIR="$PWD/templates/"

# Location of compiled .py files
OUTPUT_DIR="$PWD/templates/"

echo "Compiling all Soy files in $TEMPLATE_DIR"

for path in $TEMPLATE_DIR/*.soy; do

    file="$(basename $path)"
    name="${file%.soy}"
    echo "Compiling $file to python"

    # Run closure compiler in template directory, and compile all .soy files
    # into .py files to output directory. Both the python compiler
    # jar and the plugins jar must be included in the classpath
    java -classpath "compiler/SoyToPySrcCompiler.jar:compiler/out/Plugins.jar" \
        "com.google.template.soy.SoyToPySrcCompiler" \
        --pluginModules "PluginsModule" \
        --outputPathFormat "$OUTPUT_DIR/$name.py" \
        --runtimePath "$RUNTIME_DIR" \
        --inputPrefix "$TEMPLATE_DIR" \
        --srcs "$name.soy"

done

echo "Complete"

