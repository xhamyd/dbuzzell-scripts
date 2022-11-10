#!/usr/bin/env bash

# EXAMPLE 1
# Simple prefix/suffix subsitution
string="hello-world"
prefix="hell"
suffix="ld"

foo=${string#$prefix}
foo=${foo%$suffix}
echo "${foo}"
#OUTPUT: o-wor

# EXAMPLE 2
# URL parsing
# extract the protocol
proto="$(echo $1 | grep :// | sed -e's,^\(.*://\).*,\1,g')"
# remove the protocol
url="$(echo ${1/$proto/})"
# extract the user (if any)
user="$(echo $url | grep @ | cut -d@ -f1)"
# extract the host
host="$(echo ${url/$user@/} | cut -d/ -f1)"
# by request - try to extract the port
port="$(echo $host | sed -e 's,^.*:,:,g' -e 's,.*:\([0-9]*\).*,\1,g' -e 's,[^0-9],,g')"
# extract the path (if any)
path="$(echo $url | grep / | cut -d/ -f2-)"

echo "url: $url"
echo "  proto: $proto"
echo "  user: $user"
echo "  host: $host"
echo "  port: $port"
echo "  path: $path"
