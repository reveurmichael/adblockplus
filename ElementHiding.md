https://adblockplus.org/filter-cheatsheet

https://help.eyeo.com/adblockplus/how-to-write-filters

## Medium 

### Working:
```text
medium.com#?#div:-abp-has(>div:-abp-has(>div:-abp-has(>div:-abp-has(> div:-abp-has(> div:-abp-has(> p:-abp-contains(expert and undiscovered voices alike dive into)))))))
medium.com#?#div:-abp-has(>div:-abp-has(> div:-abp-has(> div:-abp-has(> p:-abp-contains(expert and undiscovered voices alike dive into)))))
medium.com#?#div:-abp-has(>div:-abp-has(>div:-abp-has(> div:-abp-has(> div:-abp-has(> p:-abp-contains(expert and undiscovered voices alike dive into))))))
medium.com#?#div:-abp-has(> div:-abp-has(> div:-abp-has(> p:-abp-contains(expert and undiscovered voices alike dive into))))
medium.com#?#div:-abp-has(> div:-abp-has(> p:-abp-contains(expert and undiscovered voices alike dive into)))
medium.com#?#p:-abp-contains(expert and undiscovered voices alike dive into)
medium.com#?#div:-abp-properties(background-color: rgb(0, 0, 0))
medium.com#?#div:-abp-properties(will-change: opacity, transform)
medium.com#?#h2:-abp-contains(More From Medium)
medium.com#?#div:-abp-properties(max-width: 25%)
medium.com#?#div:-abp-has(> div > div > div > div > span > div > div > span >  button)

```
### Not working:
```text
medium.com#?#div:-abp-properties(background-color: rgba(0, 0, 0, 0.9))
medium.com#?#div:-abp-properties(border-top: 1px solid rgb(230, 230, 230))
medium.com#?#div:-abp-properties(border-top: 1px solid rgba(230, 230, 230, 1))


```