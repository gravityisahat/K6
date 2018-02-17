#!/bin/bash
ps -ef | grep "ringmido.py" | awk '{print $2}' | xargs sudo kill
