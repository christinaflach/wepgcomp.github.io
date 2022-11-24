#!/bin/bash
for x in *.jpg; do convert -resize 140x140 $x ../$x; done
