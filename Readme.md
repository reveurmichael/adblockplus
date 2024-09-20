https://reveurmichael.github.io/adblockplus/list.txt

How to write filters 

- https://help.eyeo.com/adblockplus/how-to-write-filters

How to create your own personal filter list 

- https://help.getadblock.com/support/solutions/articles/6000165012-how-to-create-your-own-personal-filter-list

##  sed remove 
- Linux

sed -i '/bilibili/d' list.txt

- MacOS

sed -i '' '/bilibili/d' list.txt

## powershell arguments
function fBB { bbdown -p ALL $args } 
Set-Alias bb fBB