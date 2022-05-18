# gtool

toolbelt for developers

## how to use

whichever process u use to download stuff

save the file
`wget <raw_github_url>`

print result from file to stdout with wget
`wget -qO- <raw_github_url>`

run file with a given process

`wget -qO- *.py | python3`
`wget -qO- *.sh | bash`
`wget -qO- *.js | node`

and so on
